from typing import List

from pydantic import UUID4
from pyle38.errors import Tile38IdNotFoundError, Tile38KeyNotFoundError
from pyle38.responses import ObjectResponse
from starlette.status import HTTP_404_NOT_FOUND
from starlite import Controller, HTTPException, delete, get, post, put

from app.models.vehicle import Vehicle, VehicleResponse
from app.services.tile38 import tile38


class VehicleController(Controller):
    path = "/vehicles"
    collection = "fleet"

    @post()
    async def create_vehicle(self, data: Vehicle) -> Vehicle:
        ...

    @get()
    async def list_vehicles(self) -> List[Vehicle]:
        ...

    @put(path="/{vehicle_id:uuid}")
    async def update_vehicle(self, vehicle_id: UUID4, data: Vehicle) -> Vehicle:
        ...

    @get(path="/{vehicle_id:uuid}")
    async def get_vehicle(self, vehicle_id: UUID4) -> VehicleResponse:
        try:
            vehicle: ObjectResponse[Vehicle] = await tile38.get(
                self.collection, vehicle_id
            ).asObject()

            response = {"data": vehicle.object}
            return VehicleResponse(**response)

        except (Tile38KeyNotFoundError, Tile38IdNotFoundError):
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail=f"vehicle with id '{id}' not found",
            )

    @delete(path="/{vehicle_id:uuid}")
    async def delete_vehicle(self, vehicle_id: UUID4) -> Vehicle:
        ...
