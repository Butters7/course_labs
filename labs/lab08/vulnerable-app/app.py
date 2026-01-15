from flask import (
    Flask,
    request,
    make_response,
    render_template_string,
    redirect,
    url_for,
)
import sqlite3
import os
from html import escape

app = Flask(__name__)

DB_PATH = os.environ.get("APP_DB_PATH", "app.db")


# Security headers middleware
@app.after_request
def add_security_headers(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self'"
    )
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
        """
    )
    cur.execute("DELETE FROM users")
    cur.execute(
        "INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin')"
    )
    cur.execute(
        "INSERT INTO users (username, password, role) VALUES ('user', 'user123', 'user')"
    )
    conn.commit()
    conn.close()


def set_secure_cookie(response, name, value):
    """Set cookie with security flags"""
    response.set_cookie(
        name,
        value,
        httponly=True,
        samesite="Lax",
        secure=False,  # Set True in production with HTTPS
    )


@app.route("/")
def index():
    html = """
    <h1>Secure DAST Demo App</h1>
    <p>Исправленное приложение для лабораторной по DAST.</p>
    <ul>
      <li><a href="/echo?msg=Hello">Echo (XSS fixed)</a></li>
      <li><a href="/search?username=admin">Search (SQLi fixed)</a></li>
      <li><a href="/login">Логин (SQLi fixed)</a></li>
      <li><a href="/profile">Профиль</a></li>
      <li><a href="/admin">Админка</a></li>
      <li><a href="/files/">Files</a></li>
    </ul>
    """
    resp = make_response(html)
    set_secure_cookie(resp, "session", "guest-session-id")
    return resp


@app.route("/echo")
def echo():
    msg = request.args.get("msg", "")
    # FIX: Escape user input to prevent XSS
    safe_msg = escape(msg)
    template = """
    <h2>Echo</h2>
    <p>Сообщение: {{ msg }}</p>
    <p>XSS исправлен - ввод экранируется.</p>
    <a href="/">Назад</a>
    """
    return render_template_string(template, msg=safe_msg)


@app.route("/search")
def search():
    username = request.args.get("username", "")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # FIX: Use parameterized query to prevent SQL Injection
    query = "SELECT id, username, role FROM users WHERE username = ?"
    rows = []
    error = None
    try:
        for row in cur.execute(query, (username,)):
            rows.append(row)
    except Exception as e:
        error = str(e)

    conn.close()

    template = """
    <h2>Поиск пользователя</h2>
    <p>Поиск: <code>{{ username }}</code></p>
    {% if error %}
      <p style="color:red;">Error: {{ error }}</p>
    {% endif %}
    {% if rows %}
      <ul>
      {% for id, username, role in rows %}
        <li>{{ id }} – {{ username }} ({{ role }})</li>
      {% endfor %}
      </ul>
    {% else %}
      <p>Ничего не найдено</p>
    {% endif %}
    <p>SQL Injection исправлен - используются параметризованные запросы.</p>
    <a href="/">Назад</a>
    """
    return render_template_string(
        template, username=escape(username), rows=rows, error=error
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = """
        <h2>Логин</h2>
        <form method="post">
          <label>Username: <input type="text" name="username"></label><br>
          <label>Password: <input type="password" name="password"></label><br>
          <button type="submit">Login</button>
        </form>
        <p>Попробуйте: admin / admin123 или user / user123</p>
        <a href="/">Назад</a>
        """
        return render_template_string(form)

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # FIX: Use parameterized query to prevent SQL Injection
    query = "SELECT id, username, role FROM users WHERE username = ? AND password = ?"
    row = cur.execute(query, (username, password)).fetchone()
    conn.close()

    if row:
        _, uname, role = row
        resp = make_response(
            f"<h2>Добро пожаловать, {escape(uname)} ({escape(role)})!</h2><a href='/'>На главную</a>"
        )
        # FIX: Set secure cookies
        set_secure_cookie(resp, "user", uname)
        set_secure_cookie(resp, "role", role)
        return resp
    else:
        return render_template_string(
            "<h2>Неверные учетные данные</h2><a href='/login'>Попробовать снова</a>"
        )


@app.route("/profile")
def profile():
    username = request.cookies.get("user", "guest")
    role = request.cookies.get("role", "guest")

    template = """
    <h2>Профиль пользователя</h2>
    <p>Имя: {{ username }}</p>
    <p>Роль: {{ role }}</p>
    <a href="/">Назад</a>
    """
    return render_template_string(
        template, username=escape(username), role=escape(role)
    )


@app.route("/admin")
def admin():
    role = request.cookies.get("role", "guest")
    if role != "admin":
        return (
            "<h2>Доступ запрещён: вы не admin</h2><a href='/'>Назад</a>",
            403,
        )

    template = """
    <h2>Admin panel</h2>
    <p>Секретные настройки приложения (демо).</p>
    <ul>
      <li>DEBUG: false</li>
      <li>FEATURE_FLAG: production_mode</li>
    </ul>
    <a href="/">Назад</a>
    """
    return render_template_string(template)


@app.route("/files/")
@app.route("/files/<path:subpath>")
def files(subpath=""):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    target_dir = os.path.join(base_dir, "files")

    full_path = os.path.realpath(os.path.join(target_dir, subpath))

    # FIX: Prevent path traversal
    if not full_path.startswith(target_dir):
        return "<h2>Доступ запрещён</h2><a href='/'>Назад</a>", 403

    if not os.path.exists(full_path):
        return "<h2>Путь не найден</h2><a href='/'>Назад</a>", 404

    if os.path.isdir(full_path):
        entries = os.listdir(full_path)
        items = "".join(
            f"<li><a href='/files/{subpath}{'' if subpath.endswith('/') or subpath == '' else '/'}{escape(e)}'>{escape(e)}</a></li>"
            for e in entries
        )
        html = f"""
        <h2>Files under /files/{escape(subpath)}</h2>
        <ul>{items}</ul>
        <a href="/">Назад</a>
        """
        return html

    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    return f"<pre>{escape(content)}</pre>"


if __name__ == "__main__":
    init_db()
    # FIX: Disable debug mode in production
    app.run(host="0.0.0.0", port=8080, debug=False)
