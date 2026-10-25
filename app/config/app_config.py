from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache



class AppConfig(BaseSettings):
    db_url :str
    secret_key : str
    algorithm : str
    token_expire_time : int

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def getApp_config():
    return AppConfig() #type: ignore