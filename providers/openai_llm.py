from interfaces.llm import BaseLLMProvider
from utils.http_client import HttpClient


class OpenAILLM(BaseLLMProvider):
    """
    OpenAILLM is a concrete implementation of the LLMProvider interface
    that uses the OpenAI API to generate text responses based on a given prompt.
    """

    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        """
        Initializes the OpenAILLM instance with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the OpenAI API.
        """
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1"
        self.model = model
        self.http_client = HttpClient(
            base_url=self.base_url, headers={"Authorization": f"Bearer {self.api_key}"}
        )

    async def generate_response(self, prompt: str) -> str:
        """
        Generates a text response based on the given prompt using the OpenAI API.

        Args:
            prompt (str): The prompt to generate a response for.

        Returns:
            str: The generated text response.
        """

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant on a phone call.",
                },
                {"role": "user", "content": prompt},
            ],
        }

        response = await self.http_client.post(
            endpoint="/chat/completions",
            json=payload,
        )
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]

    async def health_check(self) -> bool:
        try:
            response = await self.http_client.get(endpoint="/models")
            return response.status_code == 200
        except Exception:
            return False
