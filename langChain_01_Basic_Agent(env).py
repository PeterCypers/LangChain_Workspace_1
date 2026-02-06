# from keys.anthropic_key import get_claude_key
# ANTHROPIC_KEY = get_claude_key()
# Above method is not how it works in practice...see info.txt

'''
Note: the way API-keys for a specific LLM-service work is via your project .env-variables,
or OS-environment, for instance the claude_agent implicitly tries to match with this
exact name in the env-variables: ... and it expects a valid API-key before running the AI(for cost-tracking)

for this demo only: run the code 1x, then use below code, but replace the string with the one found in file: anthropic_key.py
once that is set, it'll remain in OS-env vars until the terminal is closed. Run again, It worked if no errors happen.

$env:ANTHROPIC_API_KEY="sk-ant-XXXXXXXXXXXXXXXX"
'''
######################################################################################
##                             BUILD BASIC AGENT                                    ##
##  https://docs.langchain.com/oss/python/langchain/quickstart#build-a-basic-agent  ##
######################################################################################
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-5-20250929",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
########################################################################################
