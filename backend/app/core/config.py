from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Backend"
    debug: bool = True
    
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "fastapi_db"
    
    openai_api_key: str = ""
    
    class Config:
        env_file = ".env"
        

settings = Settings()