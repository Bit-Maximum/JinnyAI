from .llm_driver import LLMDriver


class LLMWorker:
    """
    LLMWorker class that utilizes an LLMDriver to send messages and receive responses.

    Attributes:
        llm_driver (LLMDriver): An instance of LLMDriver used to interact with the LLM service.

    Methods:
        get_response(message: str) -> str:
            Sends a single message to the LLM and returns the response text.

        get_responses_stream(messages: str):
            Sends a list of messages to the LLM and returns the response stream.
    """

    def __init__(self, llm_driver: LLMDriver):
        self.llm_driver = llm_driver

    @staticmethod
    def rug_message(message_raw) -> str:
        return f"User: {message_raw.author}\n{message_raw.content}"

    def get_response(self, message: str) -> str:
        return self.llm_driver.get_response(message)

    def get_responses_stream(self, messages: str):
        return self.llm_driver.get_response_stream(messages)
