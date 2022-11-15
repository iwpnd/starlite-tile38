import pytest
from httpx import AsyncClient
from starlite.status_codes import HTTP_200_OK


@pytest.mark.asyncio
async def test_ping(test_client: AsyncClient):
    response = await test_client.get("/healthz")
    assert response.status_code == HTTP_200_OK
