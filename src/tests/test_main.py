import pytest
from httpx import AsyncClient
from starlette import status


@pytest.mark.asyncio
async def test_ping(test_client: AsyncClient):
    response = await test_client.get("/healthz")
    assert response.status_code == status.HTTP_200_OK
