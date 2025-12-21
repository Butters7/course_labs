#!/usr/bin/env python3
"""Hello appsec world application.

Author: Butters7
"""

import typer
import requests
from flask import Flask

APP_NAME: str = "Hello appsec world"
app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Return greeting message."""
    return f"{APP_NAME}!"


def main(name: str = typer.Option(..., prompt="Enter your name")) -> None:
    """
    Greet the user with a personalized message.

    Args:
        name: The name of the user to greet.
    """
    print(f"{APP_NAME} from @{name}")
    print(f"Flask version: {Flask.__name__}")
    print(f"Requests version: {requests.__version__}")


if __name__ == "__main__":
    typer.run(main)
