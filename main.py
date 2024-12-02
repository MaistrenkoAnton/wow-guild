from json import JSONDecodeError

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import requests

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/guild")
async def root(guild: str, realm: str):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    response = requests.get(
        f'https://armory.warmane.com/api/guild/{guild}/{realm}/summary',
        headers=headers,
    )
    try:
        return {"message": response.json()}
    except JSONDecodeError:
        return {"message": []}

