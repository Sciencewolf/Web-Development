from flask import Flask, jsonify, Response
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def home() -> Response:
    return jsonify({"timestamp": datetime.now().__str__()})

@app.route("/get", methods=['GET'])
def get() -> Response:
    return jsonify({})


def main() -> None:
    try:
        app.run(port=8081, host="0.0.0.0")
    except Exception as ex:
        print(ex.__str__())


if __name__ == "__main__":
    main()
