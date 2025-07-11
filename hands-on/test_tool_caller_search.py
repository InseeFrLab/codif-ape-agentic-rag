import os

from autogen import AssistantAgent, LLMConfig, UserProxyAgent
from autogen.tools.experimental import DuckDuckGoSearchTool

# Configure your LLM settings
llm_config = LLMConfig(
    api_type="google", model="gemini-2.5-flash", api_key=os.environ["GEMINI_API_KEY"]
)


assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)


user_proxy = UserProxyAgent(name="user_proxy", human_input_mode="NEVER")


# Initialize the DuckDuckGoSearchTool. No API key is needed.
duckduckgo_search_tool = DuckDuckGoSearchTool()


# Register the tool for LLM recommendation and execution.
duckduckgo_search_tool.register_for_llm(assistant)
duckduckgo_search_tool.register_for_execution(user_proxy)


response = user_proxy.initiate_chat(
    recipient=assistant,
    message="Dis moi si l'activité de promoteur immobilier relève de l'intermédiation?"
    "Aide toi en utilisant DuckDuckGo.",
    max_turns=2,
)


print(f"Final Answer: {response.summary}")
