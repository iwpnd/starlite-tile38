from typing import List, Optional

from pydantic import UUID4, BaseModel, Field


class Geometry(BaseModel):
    type: str = "Point"
    coordinates: List[float] = Field(..., min_items=2, max_items=2)


class Properties(BaseModel):
    id: UUID4


class Vehicle(BaseModel):
    type: str = "Feature"
    geometry: Geometry
    properties: Properties


class VehicleRequestBody(BaseModel):
    data: Vehicle


class VehicleObject(BaseModel):
    id: UUID4
    object: Vehicle
    distance: Optional[float] = None


class VehicleResponse(BaseModel):
    data: Vehicle


class VehiclesResponse(BaseModel):
    data: List[VehicleObject]
