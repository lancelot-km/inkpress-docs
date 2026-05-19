"""Minimal Flask server for docs.inkpress.zorohq.com.

Serves:
  GET /              → redirect to /readme.txt
  GET /readme.txt    → the operator's manual (one big text file)
  GET /health        → "ok"

No DB, no auth, no templates. The text file ships in the container.
"""
from pathlib import Path
from flask import Flask, send_from_directory, redirect

app = Flask(__name__)
ROOT = Path(__file__).parent


@app.get("/")
def home():
    return redirect("/readme.txt", code=302)


@app.get("/readme.txt")
def readme():
    return send_from_directory(ROOT, "readme.txt", mimetype="text/plain; charset=utf-8")


@app.get("/health")
def health():
    return "ok\n", 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8505)
