import os
from dotenv import load_dotenv
from fastapi import FastAPI
import requests

app = FastAPI()

load_dotenv()

NINJA_API_KEY = os.getenv("NINJA_API_KEY")
if not NINJA_API_KEY:
    raise EnvironmentError("NINJA_API_KEY environment variable is not set.")

@app.get("/api/search/{query}")
def recipe(query: str):
    # Make a request to the Ninja API with the API key to get random recipes
    url = f"https://api.api-ninjas.com/v1/recipe?query={query}"
    headers = {"X-Api-Key": NINJA_API_KEY}
    resp = requests.get(url, headers={'X-Api-Key': NINJA_API_KEY}).json()
    return {"recipes":resp}

