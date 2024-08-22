from flask import Flask, request, jsonify
import linecache
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return {"message": "bruh"}


@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    print(jsonify({"received": data}))
    with open("file.txt", "a") as file:
        file.write(str(data)+str(random.random())+"\n")
    return {"status": 200}

@app.route("/get/<id>", methods=["GET"])
def get(id):
    id = int(id)
    data = linecache.getline("file.txt", id)
    return {"content": data}


if __name__ == '__main__':
    app.run(debug=True, port=5080)
