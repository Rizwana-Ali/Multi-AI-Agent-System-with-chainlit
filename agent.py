from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import os

load_dotenv()
set_tracing_disabled(True)
 
provider = AsyncOpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

 )

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=provider,
)

web_dev = Agent(
    name="web Developer",
    instructions=" Build responsive and performent website using modern frameworks.",
    model=model,
    handoff_description="Hand off to a web developer if the task is related to web development."
)

app_dev = Agent(
    name="App Developer",
    instructions=" Build mobile application using modern frameworks.",
    model=model,
    handoff_description="Hand off to app developer if the task is related to mobile app development."
)

marketing_agent = Agent(
    name="Marketing Expert Agent",
    instructions="Create and execute marketing strategies for product launches.",
    model=model,
    handoff_description="Hand off to marketing agent if the task is related to marketing."
)

async def myAgent(user_input):
   manager = Agent(
     name="Manager",
    instructions="You will chat with the user and deligates tasks to especialized agents based on their request.",
    model=model,
    handoff_description= [web_dev, app_dev, marketing_agent] 
   )

   response = await Runner.run(
      manager,
      input=user_input
   )  

   return response.final_output


