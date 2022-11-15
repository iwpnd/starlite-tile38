import pytest
from httpx import AsyncClient
from pyle38 import Tile38
from starlite.status_codes import HTTP_200_OK

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
async def test_within_empty(test_client: AsyncClient):
    response = await test_client.get(
        "/search", params={"lon": 1, "lat": 1, "radius": 1000}
    )

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"data": []}


@pytest.mark.asyncio
async def test_within(test_client: AsyncClient, tile38: Tile38):
    await tile38.set(key, id).object(feature).exec()

    response = await test_client.get(
        "/search", params={"lon": lon, "lat": lat, "radius": 100}
    )

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"data": [feature]}


@pytest.mark.asyncio
async def test_within_no_radius(test_client: AsyncClient, tile38: Tile38):
    await tile38.set(key, id).object(feature).exec()

    lon, lat = feature["geometry"]["coordinates"]

    response = await test_client.get(
        "/search", params={"lon": lon, "lat": lat, "radius": 0}
    )

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"data": [feature]}
