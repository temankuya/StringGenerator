import os

# Optional: load dotenv hanya jika ENV=dev (buat local dev)
if os.getenv("ENV", "prod") != "prod":
    from dotenv import load_dotenv
    load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
MONGO_URI = os.getenv("MONGO_URI")

# Optional debug print
print(f"✅ [DEBUG] MONGO_URI = {repr(MONGO_URI)}")
