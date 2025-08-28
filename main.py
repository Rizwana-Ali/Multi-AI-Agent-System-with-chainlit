from agent import myAgent
import chainlit as cl
import asyncio

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Welcome to the Multi-Agent System! How can I assist you today?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = asyncio.run(myAgent(user_input))
    await cl.Message(
        content=f"{response}"
    ).send()
    
       






















# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
# import os
# import streamlit as st
# import asyncio

# # Load environment variables
# load_dotenv()
# set_tracing_disabled(True)

# # Initialize the provider
# provider = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash-exp",
#     openai_client=provider,
# )

# # Define agents
# web_dev = Agent(
#     name="web Developer",
#     instructions="Build responsive and performant websites using modern frameworks.",
#     model=model,
#     handoff_description="Hand off to a web developer if the task is related to web development."
# )

# app_dev = Agent(
#     name="App Developer",
#     instructions="Build mobile applications using modern frameworks.",
#     model=model,
#     handoff_description="Hand off to app developer if the task is related to mobile app development."
# )

# marketing_agent = Agent(
#     name="Marketing Expert Agent",
#     instructions="Create and execute marketing strategies for product launches.",
#     model=model,
#     handoff_description="Hand off to marketing agent if the task is related to marketing."
# )

# async def myAgent(user_input):
#     manager = Agent(
#         name="Manager",
#         instructions="You will chat with the user and delegate tasks to specialized agents based on their request.",
#         model=model,
#         handoff_description=[web_dev, app_dev, marketing_agent] 
#     )

#     response = await Runner.run(
#         manager,
#         input=user_input
#     )  
#     return response.final_output

# # Streamlit app
# def main():
#     st.set_page_config(
#         page_title="Multi-Agent System",
#         page_icon="🤖",
#         layout="centered"
#     )
    
#     st.title("🤖 Multi-Agent System")
#     st.write("Welcome to the Multi-Agent System! How can I assist you today?")
    
#     # Initialize chat history
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
    
#     # Display chat messages from history
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])
    
#     # React to user input
#     if prompt := st.chat_input("Type your message here..."):
#         # Display user message in chat message container
#         st.chat_message("user").markdown(prompt)
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})
        
#         # Get assistant response
#         with st.spinner("Thinking..."):
#             response = asyncio.run(myAgent(prompt))
        
#         # Display assistant response in chat message container
#         with st.chat_message("assistant"):
#             st.markdown(response)
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": response})

# if __name__ == "__main__":
#     main()