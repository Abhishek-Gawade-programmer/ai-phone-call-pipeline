import httpx
from typing import Any, Dict, Optional
import asyncio
import logging

logger = logging.getLogger(__name__)


class HttpClient:
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        self.headers = headers or {}

    async def post(
        self,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
        content: Optional[bytes] = None,
        retries: int = 3,
        delay: int = 2,
    ) -> httpx.Response:
        for attempt in range(retries):
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(
                        url=f"{self.base_url}{endpoint}",
                        headers=self.headers,
                        json=json,
                        content=content,
                    )
                    response.raise_for_status()
                    return response
                except (httpx.HTTPStatusError, httpx.RequestError) as e:
                    if attempt < retries - 1:
                        logger.warning(
                            f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds..."
                        )
                        await asyncio.sleep(delay)
                    else:
                        logger.error(f"Error: {e}")
                        raise

    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        retries: int = 3,
        delay: int = 2,
    ) -> httpx.Response:
        for attempt in range(retries):
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.get(
                        url=f"{self.base_url}{endpoint}",
                        headers=self.headers,
                        params=params,
                    )
                    response.raise_for_status()
                    return response
                except (httpx.HTTPStatusError, httpx.RequestError) as e:
                    if attempt < retries - 1:
                        logger.warning(
                            f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds..."
                        )
                        await asyncio.sleep(delay)
                    else:
                        logger.error(f"Error: {e}")
                        raise
