from litellm import completion
import os

os.environ["DASHSCOPE_API_KEY"] = ""

response = completion(model="dashscope/qwen-plus", 
messages=[{"role": "user", "content": "What is the current time in Tokyo?"}])

print(response)