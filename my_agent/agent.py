from google.adk.agents.llm_agent import Agent, LlmAgent
from google.adk.models.lite_llm import LiteLlm
import os

# demo
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}


# 配置阿里云千问模型
# 请在这里填入你的阿里云千问 API Key (appkey)
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "<请填入你的阿里云千问 appkey>")

# 阿里云千问的 API 端点（根据你的地域选择）
# 北京（华北2）: "https://dashscope.aliyuncs.com/compatible-mode/v1"
# 新加坡: "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
# 美国弗吉尼亚: "https://dashscope-us.aliyuncs.com/compatible-mode/v1"
DASHSCOPE_API_BASE = os.getenv(
    "DASHSCOPE_API_BASE", 
    "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

root_agent = Agent(
    model=LiteLlm(model="dashscope/qwen-plus", api_base=DASHSCOPE_API_BASE, api_key=DASHSCOPE_API_KEY),
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)


# qwen_agent = LlmAgent(
#     model = LiteLlm(model="dashscope/qwen-plus", api_base=DASHSCOPE_API_BASE, api_key=DASHSCOPE_API_KEY),
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
#     tools=[get_current_time],
# )

