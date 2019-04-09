import json

import requests
from flask import Flask, jsonify, Response

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/health.json")
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/check", methods=["GET"])
def check():
    r = requests.get("http://localhost:5678/hosts/sidecar-pdf")
    print(json.loads(r.text))
    js = json.dumps(json.loads(r.text))
    return Response(js, status=200, mimetype='application/json')


@app.route("/invoke-slug", methods=["GET"])
def invoke_slug():
    r = requests.get("http://localhost:5678/slug/this-is-a-sample-url-a5s6f8f9")
    # return Response(r.text, status=200, mimetype='application/json')
    return jsonify(r.json())


if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='0.0.0.0', port=8058)
