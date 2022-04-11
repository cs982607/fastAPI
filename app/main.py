import uvicorn
from typing import Optional
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "API"}


# @app.post("/user/", response_model=User)
# def create_user(user: User):
#     return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


