from starlite import OpenAPIConfig, Starlite

from app.controllers.vehicles import VehicleController
from app.services.tile38 import tile38

APP_NAME = "starlite-tile38"


async def shutdown_tile38() -> None:
    """Closes the tile38 connection"""
    await tile38.quit()


app = Starlite(
    route_handlers=[VehicleController],
    openapi_config=OpenAPIConfig(title=f"{APP_NAME}", version="1.0.0"),
    on_shutdown=[shutdown_tile38],
)
