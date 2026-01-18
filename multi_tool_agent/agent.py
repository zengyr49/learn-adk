import datetime
import os
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


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


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model=LiteLlm(model="dashscope/qwen-plus", api_base=DASHSCOPE_API_BASE, api_key=DASHSCOPE_API_KEY),
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)