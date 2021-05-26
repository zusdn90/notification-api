import uvicorn
from dataclasses import asdict
from fastapi import FastAPI

from app.database.conn import db
from app.common.config import conf
from app.routes import index


def create_app():
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)
    # 데이버베이스 초기화
    # 레디스 초기화
    # 미들웨어 정의
    # 라우터 정의
    app.include_router(index.router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=conf().PROJ_RELOAD)
