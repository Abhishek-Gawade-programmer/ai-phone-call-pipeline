from interfaces.tts import BaseTTSProvider
from utils.http_client import HttpClient


class ElevenLabsTTS(BaseTTSProvider):
    """
    ElevenLabsTTS is a concrete implementation of the BaseTTSProvider interface
    that uses the ElevenLabs API to synthesize text into speech.
    """

    def __init__(self, api_key: str):
        """
        Initializes the ElevenLabsTTS instance with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the ElevenLabs API.
        """
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"
        self.voice_id = "9BWtsMINqrJLrRacOk9x"
        self.http_client = HttpClient(
            base_url=self.base_url, headers={"xi-api-key": self.api_key}
        )

    async def synthesize(self, text: str) -> bytes:
        """
        Synthesizes the given text into speech using the ElevenLabs API.

        Args:
            text (str): The text to be synthesized into speech.

        Returns:
            bytes: The synthesized speech audio data.
        """
        response = await self.http_client.post(
            endpoint=f"/text-to-speech/{self.voice_id}",
            json={
                "text": text,
                "voice_settings": {"stability": 0.75, "similarity_boost": 0.75},
            },
        )
        return response.content

    async def health_check(self) -> bool:
        try:
            response = await self.http_client.get(endpoint="/voices")
            return response.status_code == 200
        except Exception:
            return False
