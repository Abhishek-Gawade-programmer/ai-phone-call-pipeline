import pytest
import httpx
from providers.openai_llm import OpenAILLM
from tests.mocks import (
    mock_get,
    mock_get_error,
    mock_post_openai,
)


@pytest.mark.asyncio
async def test_openai_llm_health_check(mocker):
    mock_client = httpx.AsyncClient()
    mocker.patch.object(mock_client, "get", side_effect=mock_get)
    llm_provider = OpenAILLM(api_key="fake_key")
    llm_provider.http_client = mock_client  # Mocking HTTP client

    assert await llm_provider.health_check() is True


@pytest.mark.asyncio
async def test_openai_llm_health_check_error(mocker):
    mock_client = httpx.AsyncClient()
    mocker.patch.object(mock_client, "get", side_effect=mock_get_error)
    llm_provider = OpenAILLM(api_key="invalid_key")
    llm_provider.http_client = mock_client  # Mocking HTTP client

    assert await llm_provider.health_check() is False


@pytest.mark.asyncio
async def test_openai_llm_generate_response(mocker):
    mock_client = httpx.AsyncClient()
    mocker.patch.object(mock_client, "post", side_effect=mock_post_openai)
    llm_provider = OpenAILLM(api_key="fake_key")
    llm_provider.http_client = mock_client  # Mocking HTTP client

    response = await llm_provider.generate_response("Hello world")
    assert response == "Hello world"
