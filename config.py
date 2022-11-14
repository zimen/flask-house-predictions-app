from pydantic import BaseSettings
from functools import lru_cache


# load ENV settings and memorize it
@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    DBHOST: str
    DBPORT: int
    DBNAME: str
    DBUSER: str
    DBPASS: str
    
    class Config:
        env_file = ".env"

