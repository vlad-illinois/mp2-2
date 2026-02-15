from flask import Flask, request, jsonify
import requests
import socket
import subprocess

app = Flask(__name__)


@app.route("/", methods=["POST"])
def route_post():
    print(f"Received a POST request")
    try:
        process = subprocess.Popen(['python3', 'stress_cpu.py'])
        return "OK", 200
    except Exception as e:
        return f"Error in processing request", 500
    
@app.route("/", methods=["GET"])
def route_get():
    print(f"Received a G request")
    try:
        host = socket.gethostname()
        return host,200
    except Exception as e:
        return f"Error in processing request", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
