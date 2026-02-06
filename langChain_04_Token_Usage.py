############################################################################
##                            TOKEN USAGE(check)                          ##
##  https://docs.langchain.com/oss/python/langchain/messages#token-usage  ##
############################################################################
######### Set-API-Env-Variable ##############
from keys.anthropic_key import get_claude_key
ANTHROPIC_KEY = get_claude_key()

import os
os.environ["ANTHROPIC_API_KEY"] = ANTHROPIC_KEY
#############################################

from langchain.chat_models import init_chat_model

model = init_chat_model("claude-sonnet-4-5-20250929")

response = model.invoke("Hello!")
print(response.usage_metadata)