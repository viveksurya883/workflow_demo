import os
from dotenv import load_dotenv
load_dotenv()

name = os.getenv("MY_NAME", "No name found")
age = os.getenv("MY_AGE", "Age not found")
marks = float(os.getenv("MARKS", "No marks recorded"))
print(f"Hello, {name} from Kaiser and my present age is {age} with productivity of {marks:.2f}%!")
