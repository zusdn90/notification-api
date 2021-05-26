from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

# 딕셔너리 형식으로 가져오기 위해 dataclass를 사용
@dataclass
class Config:
    """
    기본 Configuration용
    """

    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = environ.get(
        "DB_URL", "mysql+pymysql://travis@localhost/notification_api?charset=utf8mb4"
    )
    print(DB_URL)


def conf():
    """
    환경 불러오기
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))
