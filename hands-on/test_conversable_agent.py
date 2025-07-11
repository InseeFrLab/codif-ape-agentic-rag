# 1. Import our agent class
from autogen import ConversableAgent, LLMConfig

# 2. Define our LLM configuration for OpenAI's GPT-4o mini
#    uses the OPENAI_API_KEY environment variable: export OPENAI_API_KEY=
llm_config = LLMConfig(
    api_type="openai",
    model="magistral:latest",
    base_url="https://llm.lab.sspcloud.fr/api",
)


# 3. Create our LLM agent
with llm_config:
    my_agent = ConversableAgent(
        name="helpful_agent",
        system_message="You are a poetic AI assistant, respond in rhyme.",
    )


# 4. Run the agent with a prompt
response = my_agent.run(
    message="In one sentence, what's the big deal about AI?",
    max_turns=3,
    user_input=True,
)


# 5. Iterate through the chat automatically with console output
response.process()


# 6. Print the chat
print(response.messages)
