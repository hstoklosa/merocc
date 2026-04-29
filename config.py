import os
import dotenv

dotenv.load_dotenv()


MEROSS_EMAIL = os.getenv("MEROSS_EMAIL")
MEROSS_PASSWORD = os.getenv("MEROSS_PASSWORD")