import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

name = os.getenv("MY_NAME", "No name found")
print(f"Hello, {name} from custom GitHub Action!")
