from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai import Agent
from pydantic_ai.providers.deepseek import DeepSeekProvider
import tools
from dotenv import load_dotenv
import os

load_dotenv()

provider = DeepSeekProvider()

model = OpenAIChatModel(model_name='deepseek-chat', provider=provider)

agent = Agent(  
    model=model,
    tools=[tools.write_file, tools.read_file, tools.list_directory],
)

def main():
    print('Hello from agen-demo!')
    while True:
        user_input = input('Input: ')
        result = agent.run_sync(user_input)
        print(result.output)

if __name__ == "__main__":
    main()