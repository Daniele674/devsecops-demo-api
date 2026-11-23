import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/ping")
def ping():
    target = request.args.get("host", "127.0.0.1")
    # Bug intenzionale (Command Injection) per testare Semgrep
    os.system(f"ping -c 1 {target}")
    return {"pinged": target}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
