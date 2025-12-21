#!/usr/bin/env python3
"""Hello appsec world server application.

Author: Butters7
"""

import os

from flask import Flask, Response

APP_NAME: str = "Hello appsec world"
app = Flask(__name__)


def colorful_text(text: str) -> str:
    """Generate colorful HTML text."""
    colors = ["red", "green", "yellow", "blue", "purple"]
    spans = []
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        spans.append(f'<span style="color:{color}">{char}</span>')
    return "".join(spans)


@app.route("/")
def index() -> Response:
    """Return greeting message as HTML."""
    name = os.environ.get("GREETING_NAME", "World")
    message = f"{APP_NAME} from @{name}"
    colored_message = colorful_text(message)
    html = f"""
    <html>
    <head><title>{APP_NAME}</title></head>
    <body style="font-family: monospace; font-size: 24px;">
    {colored_message}
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")


@app.route("/api")
def api() -> Response:
    """Return greeting message as plain text."""
    name = os.environ.get("GREETING_NAME", "World")
    message = f"{APP_NAME} from @{name}"
    return Response(message, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # nosec B104
