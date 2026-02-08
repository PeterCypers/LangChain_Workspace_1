'''
Retrievers query indexed data to return relevant documents for a given query.
A retriever does not need to be able to store documents, only to return (or retrieve) them.
Retrievers can be created from Vector stores.

https://docs.langchain.com/oss/python/integrations/retrievers

Retrieval of a corpus of documents, some examples:

VertexAISearchRetriever / ElasticsearchRetriever / ArxivRetriever /
WikipediaRetriever / ChatGPT Plugin / Google Drive / IBM watsonx.ai / 
Activeloop Deep Memory
'''
############### Key Setup ####################
from keys.langsmith_key import get_langsmith_key
from keys.openai_key import get_gpt_key
LANGSMITH_KEY = get_langsmith_key()
GPT_KEY = get_gpt_key()

import os
os.environ["LANGSMITH_API_KEY"] = LANGSMITH_KEY
# os.environ["LANGSMITH_TRACING"] = "true"
os.environ["OPENAI_API_KEY"] = GPT_KEY
#############################################

##############################################################################
##                     Wikipedia Retriever Example:                         ##
## https://docs.langchain.com/oss/python/integrations/retrievers/wikipedia  ##
##############################################################################
# wiki quiet install may have been faster... -> python -m pip install -Uq wikipedia
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    load_max_docs=5,
    top_k_results=1,
    doc_content_chars_max=1000
)
# https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.wikipedia.WikipediaRetriever.html#langchain-community-retrievers-wikipedia-wikipediaretriever

# in comment: didn't work -> http 403
# docs = retriever.invoke("TOKYO GHOUL")
# print(docs[0].page_content[:400])

from langchain_core.output_parsers import StrOutputParser  
from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.runnables import RunnablePassthrough  
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(  
"""Answer the question based only on the context provided.  
Context: {context}  
Question: {question}"""  
)  
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")  
def format_docs(docs):  
    return "\n\n".join(doc.page_content for doc in docs)  
chain = (  
{"context": retriever | format_docs, "question": RunnablePassthrough()}  
| prompt  
| llm  
| StrOutputParser()  
)  
chain.invoke(  
"Who is the main character in `Tokyo Ghoul` and does he transform into a ghoul?"  
)

# IMPORTANT: the Wiki part of this file may work. But I can't test it because I don't have GPT-credits



##############################################################################
# Amazon Kendra Retriever Example:
# https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html
# python -m pip install -qU  boto3

from langchain_community.retrievers import AmazonKendraRetriever

retriever = AmazonKendraRetriever(index_id="c0806df7-e76b-4bce-9b5c-d5582f6b1a03")

# retriever.invoke("what is langchain")

# this doesn't work, the documentation is not 100% complete to get this working
# also AWS credentials (api-key etc) are required
#############################################################################