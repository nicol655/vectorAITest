from starlette.applications import Starlette
from starlette.responses import JSONResponse

from blueprints.albums.routes import routes
from settings import database, metadata


app = Starlette(
    routes=routes,
    on_startup=[database.connect],
    on_shutdown=[database.disconnect]
)

@app.route("/")
async def homepage(request):
    return JSONResponse({"message": "Hello World!"})