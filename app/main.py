import uvicorn
from typing import Optional
from fastapi import FastAPI

from common.config import conf


def create_app():

	app = FastAPI()

	return app 

app = create_app()

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)