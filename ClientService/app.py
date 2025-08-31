from flask import Flask
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

app = Flask(__name__)

HELLO_SERVICE_URL = "http://localhost:5001/hello"

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
def call_hello_service():
    response = requests.get(HELLO_SERVICE_URL, timeout=2)
    response.raise_for_status()
    return response.text

@app.route("/call")
def call():
    try:
        result = call_hello_service()
        return f"Response from HelloService: {result}"
    except Exception as e:
        return f"Failed after retries: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
