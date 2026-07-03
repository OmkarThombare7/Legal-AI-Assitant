import os
from groq import Groq
from dotenv import load_dotenv


print("FINAL CHECK KEY:", repr(os.getenv("GROQ_API_KEY")))

# ✅ Force load .env from root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(BASE_DIR, ".env")

load_dotenv(env_path)

api_key = os.getenv("GROQ_API_KEY")

print("ENV PATH:", env_path)
print("FILE EXISTS:", os.path.exists(env_path))

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found. Check .env file")

# ✅ Single global client
client = Groq(api_key=api_key)