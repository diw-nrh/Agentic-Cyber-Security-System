import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    class Memory:
        URL = "http://localhost:1000"
        DATABASE_URL = os.getenv("MEMORY_DB_URL")

    @classmethod
    def validate(cls):
        if not cls.Memory.DATABASE_URL:
            raise ValueError("Memory database URL is not set in environment variables.")

Config.validate()