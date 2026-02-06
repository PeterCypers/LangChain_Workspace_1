### By GPT:

```py
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# 1. Load or index your document chunks
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local("oas_index", embeddings)

# 2. Build the RAG chain
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":3})
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    chain_type="stuff",
    retriever=retriever
)

# 3. Ask a question
query = "Does this commit comply with best practices?"
result = qa.run(query)
print(result)
```

### Notes:

It is pointless to question GPT or ask it about implementation of RAG... it just suggests deprecated packages and requires
me to install many pointless packages, the docs on langchain are where I should get my info from

https://stackoverflow.com/questions/79807773/using-create-retrieval-chain-due-to-retrievalqa-deprecation

there are different ways to do this these days

from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

are deprecate, so just for this demo we'll use a project which keeps alive these deprecated packages

https://docs.langchain.com/oss/python/releases/langchain-v1#langchain-classic
Legacy functionality has moved to langchain-classic to keep the core packages lean and focused.


OpenAI API-pricing
https://platform.openai.com/docs/pricing

### The situation before giving up on GPT-questioning:

The below code has already been adapted quite a bit, the Agentic Course by IBM also used a specific version
of LangChain, much of which is already changed/deprecated, things are done differently now...

```py
# my added method:
from keys.openai_key import get_gpt_key
OPENAI_KEY = get_gpt_key()

import os
os.environ["OPENAI_API_KEY"] = OPENAI_KEY

# check api-key
def check_api_key():
    api_key = os.environ.get("OPENAI_API_KEY")
    print(api_key)

check_api_key()
# code by GPT:

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1) Load or build your FAISS index
# If you already saved the index:
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local("oas_index", embeddings, allow_dangerous_deserialization=True)

# 2) Create a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 3) Build the RAG chain
llm = ChatOpenAI(temperature=0)
system_prompt = """
Use the following context to answer the question.  
If you don't know the answer, say you don't know.
Context: {context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
    ]
)

rag_chain = create_retrieval_chain(
    llm=llm,
    retriever=retriever,
    chain=create_stuff_documents_chain(llm=llm, prompt=prompt),
)

# 4) Execute a query
query = "Does this commit comply with best practices?"
result = rag_chain.invoke({"query": query})

print(result["text"])
```