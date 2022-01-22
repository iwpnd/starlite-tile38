import pytest
from httpx import AsyncClient
from starlette import status

key = "fleet"
id = "truck1"
lat = 52.25
lon = 13.37

feature = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [lon, lat]},
    "properties": {"id": id},
}

valid_key = {"x-api-key": "test"}
invalid_key = {"x-api-key": "invalid"}


@pytest.mark.asyncio
async def test_ping(test_client: AsyncClient):
    response = await test_client.get("/healthz")
    assert response.status_code == status.HTTP_200_OK
