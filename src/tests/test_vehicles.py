import pytest
from httpx import AsyncClient
from pyle38 import Tile38
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


@pytest.mark.asyncio
async def test_get_vehicle(test_client: AsyncClient, tile38: Tile38):
    await tile38.set(key, id).object(feature).exec()

    response = await test_client.get(f"/vehicles/{id}")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_get_vehicle_notfound(test_client: AsyncClient):
    response = await test_client.get("/vehicles/banana")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "vehicle with id 'banana' not found",
        "extra": None,
    }


@pytest.mark.asyncio
async def test_set_vehicle(test_client: AsyncClient, tile38: Tile38):
    post = await test_client.post("/vehicles", json={"data": feature})

    assert post.status_code == status.HTTP_201_CREATED

    response = await tile38.get(key, id).asObject()

    assert response.object == feature
