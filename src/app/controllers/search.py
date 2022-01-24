from typing import Optional

from pyle38.responses import ObjectsResponse
from starlite import Controller, Parameter, get

from app.models.vehicle import Vehicle, VehiclesResponse
from app.services.tile38 import tile38


class SearchController(Controller):
    path = "/search"
    collection = "fleet"

    @get()
    async def get_within(
        self,
        lat: float = Parameter(gt=-90, le=90),
        lon: float = Parameter(gt=-180, le=180),
        radius: Optional[float] = Parameter(),
    ) -> VehiclesResponse:

        radius = radius if radius else 0
        vehicles: ObjectsResponse[Vehicle] = (
            await tile38.within(self.collection).circle(lat, lon, radius).asObjects()
        )

        return VehiclesResponse(**{"data": [o.object for o in vehicles.objects]})
