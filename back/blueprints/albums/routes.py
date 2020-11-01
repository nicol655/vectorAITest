"""Album routes module."""
from starlette.routing import Route

from .views import list_albums

routes = [
    Route("/albums", endpoint=list_albums, methods=["GET"]),
]