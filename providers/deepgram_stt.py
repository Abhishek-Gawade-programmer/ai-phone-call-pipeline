from interfaces.stt import BaseSTTProvider
from interfaces.tts import BaseTTSProvider
from utils.http_client import HttpClient


class DeepGramSTT(BaseSTTProvider, BaseTTSProvider):
    """
    DeepGramSTT is a concrete implementation of the STTProvider interface
    that uses the DeepGram API to transcribe audio data.
    """

    def __init__(self, api_key: str):
        """
        Initializes the DeepGramSTT instance with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the DeepGram API.
        """
        self.api_key = api_key
        self.base_url = "https://api.deepgram.com/v1"
        self.model = "aura-asteria-en"
        self.http_client = HttpClient(
            base_url=self.base_url, headers={"Authorization": f"Token {self.api_key}"}
        )

    async def transcribe(self, audio_data: bytes) -> str:
        """
        Transcribes the given audio data using the DeepGram API.

        Args:
            audio_data (bytes): The audio data to be transcribed.

        Returns:
            str: The transcribed text from the audio data.
        """
        response = await self.http_client.post(
            endpoint="/listen",
            content=audio_data,
        )
        response_data = response.json()
        return (
            response_data.get("results", {})
            .get("channels", [{}])[0]
            .get("alternatives", [{}])[0]
            .get("transcript", "")
        )

    async def synthesize(self, text: str) -> bytes:
        response = await self.http_client.post(
            endpoint=f"/speak?model={self.model}",
            json={"text": text},
        )
        return response.content

    async def health_check(self) -> bool:
        response = await self.http_client.get(
            endpoint="/projects",
        )
        return response.status_code == 200
