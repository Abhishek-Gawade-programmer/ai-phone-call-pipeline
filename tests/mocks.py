async def mock_post(endpoint, content):
    class MockResponse:
        def json(self):
            return {
                "results": {
                    "channels": [{"alternatives": [{"transcript": "Hello world"}]}]
                }
            }

    return MockResponse()


async def mock_post_openai(endpoint, content=None, json=None):
    class MockResponse:
        def json(self):
            return {"choices": [{"message": {"content": "Hello world"}}]}

    return MockResponse()


async def mock_post_openai_error(endpoint, content=None, json=None):
    class MockErrorResponse:
        def json(self):
            return {"error": "Invalid API key"}

        @property
        def status_code(self):
            return 401

    return MockErrorResponse()


async def mock_post_error(endpoint, content):
    class MockErrorResponse:
        def json(self):
            return {"error": "Invalid API key"}

        @property
        def status_code(self):
            return 401

    return MockErrorResponse()


async def mock_get(endpoint):
    class MockResponse:
        def json(self):
            return {}

        @property
        def status_code(self):
            return 200

    return MockResponse()


async def mock_get_error(endpoint):
    class MockErrorResponse:
        @property
        def status_code(self):
            return 401

    return MockErrorResponse()
