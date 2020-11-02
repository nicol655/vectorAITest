"""Album factory ORM module."""
from settings import database
from .models import album

class AlbumFactory:

  """Album Factory class representation for all database querys."""

  model = album

  async def fetch_all_albums(self, request):
    """Fetch all albums from SQLAlchemy database."""
    query = self.model.select().order_by(self.model.c.position.asc())
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

  @database.transaction()
  async def update(self, album_id):
    """Update an album from SQLAlchemy database."""
    pass


  @database.transaction()
  async def delete(self, album_id):
    """Delete an album from SQLAlchemy database."""
    pass

  @database.transaction()
  async def bulk_update(self, data):
    """Update list albums from SQLAlchemy database."""
    for album in data:
      query = (
        self.model.update()
          .where(self.model.c.id == album.get('id'))
          .values(position=album.get('position'))
      )
      await database.execute(query)