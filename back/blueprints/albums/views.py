"""Album views module."""
from starlette.responses import JSONResponse

from .factory import AlbumFactory


class AlbumViews:

  """Albun Views class representation for all album's requests."""

  factory = AlbumFactory()

  async def list(self, request):
    """Retreieve all albums.
    
    Returns
    -------
      list of all albums.
    """
    albums = await self.factory.fetch_all_albums(request)
    response = [
      {
        "type": album.get("type"),
        "title": album.get("title"),
        "position": album.get("position"),
        "img_src": album.get("img_src"),
      }
      for album in albums
    ]
    return JSONResponse(response)

  async def create(self, request):
    """Create new album object based on the request data.

    Arguments
    ---------
      request - object
        request[type] - string
          containing the album's type.
        request[title] - string
          containing the album's title.
        request[position] - interger
          containing the ordering album's position.
        request[img_src] - string
          containing the album's source image.

    Returns
    -------
      created album's object.
    """
    data = await request.json()
    await self.factory.create(request)
    response = {
      "type": data.get("type"),
      "title": data.get("title"),
      "position": data.get("position"),
      "img_src": data.get("img_src"),
    }
    return JSONResponse(response)

  async def update(self, request):
    """Update existing album based on the request data."""
    pass

  async def delete(self, request):
    """Delete existing album based on the request data."""
    pass