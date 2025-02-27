# JinnyAI Discord bot

## Installation
In order to record & play audio you need to install FFMPEG and add it to PATH
See installation guide: https://ffmpeg.org/download.html

In order to have a chat with JinnyAI you should connect to OpenApi model or run LLM locally (f.e. using LM Studio).
Then in `` src/utils/service/openapi_driver.py `` you need to specify how to connect to your LLM.
Default is local setup:
```
class OpenAIDriver(LLMDriver):

    def __init__(self):
        self.client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
        self.model = "qwen2.5-7b-instruct-1m"
```