import random
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    if random.random() < 0.5:  # 50% probabilidad de fallo
        return "Internal Server Error", 500
    return "Hello from HelloService!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)