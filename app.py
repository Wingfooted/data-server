from flask import Flask, request, jsonify
import linecache

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return {"message": "bruh"}


@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    print(jsonify({"received": data}))
    with open("store.txt", "a") as file:
        if data["vector"]:
            vector = data["vector"]
        else:
            return {"status": 201}
        file.write(str(vector)+"\n")
    return {"status": 200}


@app.route("/analytics", methods=["GET"])
def analytics():
    with open('store.txt', 'r') as file:
        return {sum(1 for line in file)}
    


@app.route("/get/<id>", methods=["GET"])
def get(id):
    id = int(id)
    data = linecache.getline("store.txt", id):
    return {"content": data}


if __name__ == '__main__':
    app.run(debug=True, port=5080, host="0.0.0.0")
