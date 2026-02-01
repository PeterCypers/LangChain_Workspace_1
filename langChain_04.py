############################################################################
##                            TOKEN USAGE(check)                          ##
##  https://docs.langchain.com/oss/python/langchain/messages#token-usage  ##
############################################################################

from langchain.chat_models import init_chat_model

model = init_chat_model("claude-sonnet-4-5-20250929")

response = model.invoke("Hello!")
print(response.usage_metadata)