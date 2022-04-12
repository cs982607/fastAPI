import uvicorn
from dataclasses import asdict
from typing import Optional
from fastapi import FastAPI

from common.config import conf
from database.database import db
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)
    # 데이터 베이스 이니셜라이즈

    # 미들웨어 정의
    app.add_middleware(CORSMiddleware, 
                allow_credentials=True, 
                allow_origins=conf().ALLOW_SITE, 
                allow_methods = ["*"], 
                allow_headers = ["*"]
            )
    app.include_router("/users", )
    app.include_router("/rules", )
    app.include_router("/logs", )


@app.get("/")
def root():
    return {"Hello": "API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


