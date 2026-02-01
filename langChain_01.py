# from keys.anthropic_key import get_claude_key
# ANTHROPIC_KEY = get_claude_key()
# Above method is not how it works in practice...see info.txt
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
