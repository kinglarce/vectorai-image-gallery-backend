from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route, Mount
from starlette.requests import Request
from app.database import sqlalchemy, database, metadata, Bank
from sqlalchemy.sql.expression import bindparam

engine = sqlalchemy.create_engine(str(database.url))
metadata.create_all(engine)
middleware = [
    Middleware(
        CORSMiddleware, 
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

async def homepage(request):
    return JSONResponse({'message': 'Hello World!'})


async def get_bank(request: Request):
    query = Bank.select()
    contents = await database.fetch_all(query)
    response = [
        {
            '_id': content['_id'],
            'bank_type': content['bank_type'],
            'title': content['title'],
            'position': content['position'],
            'image': content['image']
        }
        for content in contents
    ]
    return JSONResponse(response)


async def update_bank(request: Request):
    return JSONResponse({'message': 'Successfully Updated'})

routes = [
    Route('/', endpoint=homepage),
    Mount('/bank', routes=[
        Route('/', get_bank, methods=['GET']),
        Route('/', update_bank, methods=['POST'])
    ])
]

app = Starlette(
    debug=True,
    routes=routes,
    on_startup=[database.connect],
    on_shutdown=[database.disconnect],
    middleware=middleware
)
