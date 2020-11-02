"""Album routes module."""
from starlette.routing import Route

from .views import AlbumViews

routes = [
    Route("/albums/", endpoint=AlbumViews().list, methods=["GET"]),
    Route("/albums/", endpoint=AlbumViews().create, methods=["POST"]),
    Route("/albums/<pk>/", endpoint=AlbumViews().update, methods=["PUT"]),
    Route("/albums/<pk>/", endpoint=AlbumViews().delete, methods=["DELETE"]),
]