import os
from typing import Optional

from autogen import AssistantAgent, UserProxyAgent
from autogen.interop import Interoperability
from pydantic import BaseModel
from pydantic_ai import RunContext
from pydantic_ai.common_tools.duckduckgo import duckduckgo_search_tool
from pydantic_ai.tools import Tool as PydanticAITool

# Put your key in the OPENAI_API_KEY environment variable
config_list = [
    {
        "api_type": "openai",
        "model": "gpt-4o",
        "base_url": "https://llm.lab.sspcloud.fr/api",
        "api_key": os.environ["OPENAI_API_KEY"],
    }
]


# 1. Define agents
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
)

chatbot = AssistantAgent(
    name="chatbot",
    llm_config={"config_list": config_list},
)


# 1. Structure input data - define a `Player`
class Player(BaseModel):
    name: str
    age: int


# 2. Define tool to get player
def get_player(ctx: RunContext[Player], additional_info: Optional[str] = None) -> str:
    # type: ignore[valid-type]
    """Get the player's name.

    Args:
        additional_info: Additional information which can be used.
    """
    return f"Name: {ctx.deps.name}, Age: {ctx.deps.age}, Additional info: {additional_info}"
    # type: ignore[attr-defined]


# 3. Define interoperablity object for pydantic AI
interop = Interoperability()
pydantic_ai_tool = PydanticAITool(get_player, takes_ctx=True)

# 4. Convert 2 tools: convert get_player tool and inject player as a dependency
# + convert search tool
# player = Player(name="Luka", age=25)
# player_tool = interop.convert_tool(tool=pydantic_ai_tool, type="pydanticai", deps=player)
duckduckgo_search_tool = interop.convert_tool(
    tool=duckduckgo_search_tool(), type="pydanticai"
)


# 5. Registers the tool with the agents, the description will be used by the LLM
duckduckgo_search_tool.register_for_execution(user_proxy)
duckduckgo_search_tool.register_for_llm(chatbot)
# duckduckgo_search_tool.register_for_llm(chatbot)

# 6. Two-way chat ensures the executor agent follows the suggesting agent
chat_result = user_proxy.initiate_chat(
    recipient=chatbot,
    message="Search for the best data scientist of the moment",
    max_turns=3,
    # recipient=chatbot, message="Get player, for additional information use 'goal keeper'",
    #  max_turns=3
)


print(chat_result.chat_history[-1]["content"])
