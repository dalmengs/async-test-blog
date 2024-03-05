from dotenv import load_dotenv
import os

load_dotenv()


def env(key: str) -> str:
    return os.environ.get(key)