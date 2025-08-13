import os
from dotenv import load_dotenv
load_dotenv()

name = os.getenv("MY_NAME", "No name found")
age = os.getenv("MY_AGE", "Age not found")
marks = os.getenv("MARKS", "No marks recorded")
print(f"Hello, {name} from custom GitHub Action!")
