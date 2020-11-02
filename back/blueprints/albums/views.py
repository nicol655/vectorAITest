"""Album views module."""
from json import loads
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
        "id": album.get("id"),
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

  async def update(self, album_id):
    """Update existing album based on the request data."""
    await self.factory.update(album_id)
    pass

  async def delete(self, album_id):
    """Delete existing album based on the request data."""
    await self.factory.delete(album_id)
    pass

  async def bulk_update(self, request):
    """Update existing albums based on the list request data."""
    data = await request.body()
    await self.factory.bulk_update(loads(data))
    return JSONResponse({"message": "Albums reordered"})