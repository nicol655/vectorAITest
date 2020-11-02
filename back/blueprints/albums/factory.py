"""Album factory ORM module."""
from settings import database
from .models import album

class AlbumFactory:

  """Album Factory class representation for all database querys."""

  model = album

  async def fetch_all_albums(self, request):
    """Fetch all albums from SQLAlchemy database."""
    query = self.model.select()
    albums = await database.fetch_all(query)
    return albums

  @database.transaction()
  async def create(self, request):
    """Create a new album from SQLAlchemy database."""
    query = self.model.insert().values(
      type=request.get('type'),
      title=request.get('title'),
      position=request.get('position'),
      img_src=request.get('img_src'),
    )
    await database.execute(query)
    raise RuntimeError()