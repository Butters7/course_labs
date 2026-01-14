from flask import Flask, request, make_response
import sqlite3
import os
import subprocess
import json
import logging
import re
import ast
from html import escape

app = Flask(__name__)

# FIX: Disable debug mode
app.config["DEBUG"] = False

# FIX: Use environment variables for credentials
DB_USER = os.environ.get("DB_USER", "app_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "change_me")
DB_PATH = "app.db"

# FIX: Set logging to INFO instead of DEBUG
logging.basicConfig(level=logging.INFO)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


@app.route("/")
def index():
    # FIX: Remove version disclosure
    return "Application is running"


@app.route("/user")
def get_user():
    username = request.args.get("name", "")
    conn = get_db()
    cur = conn.cursor()
    # FIX: Use parameterized query to prevent SQL Injection
    query = "SELECT id, name, email FROM users WHERE name = ?"
    rows = cur.execute(query, (username,)).fetchall()
    conn.close()
    return {"result": rows}


@app.route("/search")
def search():
    q = request.args.get("q", "")
    # FIX: Escape HTML to prevent XSS
    safe_q = escape(q)
    html = f"<h1>Results for: {safe_q}</h1>"
    return make_response(html, 200)


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # FIX: Validate input and use subprocess with shell=False
    if not re.match(r'^[\d\.]+$', host):
        return "Invalid host format", 400
    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True,
            timeout=5
        )
        return f"Pinged {escape(host)}: {result.returncode}"
    except subprocess.TimeoutExpired:
        return "Ping timeout", 504


@app.route("/backup")
def backup():
    # FIX: Use fixed path, not user input
    target = "/tmp/backup.sql"
    try:
        result = subprocess.run(
            ["pg_dump", "mydb", "-f", target],
            capture_output=True,
            timeout=60
        )
        return f"Backup completed with code: {result.returncode}"
    except Exception as e:
        return f"Backup failed: {str(e)}", 500


# FIX: Removed /read endpoint - file reading functionality disabled for security


@app.route("/load")
def load():
    data = request.args.get("data", "")
    # FIX: Use JSON instead of pickle for deserialization
    try:
        obj = json.loads(data)
        return f"Loaded object: {obj}"
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}", 400


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    # FIX: Use ast.literal_eval for safe evaluation
    try:
        # Only allow simple numeric expressions
        result = ast.literal_eval(expr)
        if not isinstance(result, (int, float)):
            return "Only numeric results allowed", 400
        return str(result)
    except (ValueError, SyntaxError):
        return "Invalid expression", 400


@app.route("/debug")
def debug():
    # FIX: Remove sensitive information exposure
    return {"status": "ok", "debug": False}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
