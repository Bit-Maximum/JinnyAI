from .llm_driver import LLMDriver

from openai import OpenAI


class OpenAIDriver(LLMDriver):

    def __init__(self):
        self.client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
        self.model = "qwen2.5-7b-instruct-1m"

    def get_response(self, message: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": message,
                    }
                ],
            )
            if len(response.choices) == 0:
                raise Exception("No response")
            return response.choices[0].message.content

        except Exception as err:
            print("Someone tell Max there is a problem with my AI")
            print(err)

    def get_response_stream(self, messages: str):
        """
        Example usage of get_response_stream_generator
        result = ""
        for content in get_response_stream_generator():
            result += content
            print(result)
            # feed into tts

        print(f"Finished with message: {result}")
        """

        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": messages}],
            stream=True,
        )
        for chunk in stream:
            yield chunk.choices[0].delta.content or ""
