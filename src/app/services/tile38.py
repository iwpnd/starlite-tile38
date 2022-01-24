from pyle38 import Tile38

from app.config import Credentials

creds = Credentials()

tile38 = Tile38(url=creds.tile38_uri)
