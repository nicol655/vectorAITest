"""Album views module."""
from starlette.responses import JSONResponse

from .models import album

async def list_albums(request):
  query = album.select()
  results = await database.fetch_all(query)
  content = [
    {
      "text": result["text"],
      "completed": result["completed"]
    }
    for result in results
  ]
  return JSONResponse(content)