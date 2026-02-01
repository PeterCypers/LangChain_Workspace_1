#################################################################
##                   Clone of langChain_02                     ##
##            but setting env-var at runtime(in python)        ##
#################################################################
# Setting the env-variable in the .py-file, technically even better
# so we don't need to set env-variable beforehand (and follows Course)

from keys.anthropic_key import get_claude_key
ANTHROPIC_KEY = get_claude_key()

import os
os.environ["ANTHROPIC_API_KEY"] = ANTHROPIC_KEY

# check api-key
def check_api_key():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    print(api_key)
#################################################################

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage#, SystemMessage

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-5-20250929",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

def run_agent():
    # Run the agent
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )

    # Human input
    human_texts = [m.content for m in result["messages"] if isinstance(m, HumanMessage)] # list
    print(f"Prompt: {human_texts}\n")

    # AI output
    ai_texts = [m.content for m in result["messages"] if isinstance(m, AIMessage)] # list

    # Final AI response
    final_ai_text = ai_texts[-1]
    print(final_ai_text)

# check_api_key()
run_agent()