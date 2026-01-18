import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import google_search

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "<请填入你的阿里云千问 appkey>")
DASHSCOPE_API_BASE = os.getenv(
    "DASHSCOPE_API_BASE", 
    "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 千问不支持google_search工具。这里纯用作展示罢了。

root_agent = Agent(
   # A unique name for the agent.
   name="basic_search_agent",
   # The Large Language Model (LLM) that agent will use.
   # Please fill in the latest model id that supports live from
   # https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/#supported-models
   model=LiteLlm(model="dashscope/qwen-plus", api_base=DASHSCOPE_API_BASE, api_key=DASHSCOPE_API_KEY),
   # A short description of the agent's purpose.
   description="Agent to answer questions using Google Search.",
   # Instructions to set the agent's behavior.
   instruction="You are an expert researcher. You always stick to the facts.",
   # Add google_search tool to perform grounding with Google search.
   tools=[google_search]
)