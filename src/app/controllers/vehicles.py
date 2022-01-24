from typing import Optional

from pyle38.errors import Tile38IdNotFoundError, Tile38KeyNotFoundError
from pyle38.responses import ObjectResponse, ObjectsResponse
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from starlite import Controller, HTTPException, Parameter, get, post

from app.models.vehicle import (
    Vehicle,
    VehicleRequestBody,
    VehicleResponse,
    VehiclesResponse,
)
from app.services.tile38 import tile38


class VehicleController(Controller):
    path = "/vehicles"
    collection = "fleet"

    @post(status_code=HTTP_201_CREATED)
    async def upsert_vehicle(self, data: VehicleRequestBody) -> VehicleResponse:
        vehicle = data.data
        vehicle_id = vehicle.properties.id
        await tile38.set(self.collection, vehicle_id).object(vehicle.dict()).exec()

        return VehicleResponse(**{"data": vehicle})

    @get(path="/search")
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

    @get()
    async def list_vehicles(self) -> VehiclesResponse:
        vehicles: ObjectsResponse[Vehicle] = await tile38.scan(
            self.collection
        ).asObjects()

        return VehiclesResponse(**{"data": [o.object for o in vehicles.objects]})

    @get(path="/{vehicle_id:str}")
    async def get_vehicle(self, vehicle_id: str) -> VehicleResponse:
        try:
            vehicle: ObjectResponse[Vehicle] = await tile38.get(
                self.collection, vehicle_id
            ).asObject()

            response = {"data": vehicle.object}
            return VehicleResponse(**response)

        except (Tile38KeyNotFoundError, Tile38IdNotFoundError):
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail=f"vehicle with id '{vehicle_id}' not found",
            )
