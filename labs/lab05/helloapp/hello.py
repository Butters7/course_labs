#!/usr/bin/env python3
"""Hello appsec world application.

Author: Butters7
"""

import typer

APP_NAME: str = "Hello appsec world"


def main(name: str = typer.Option(..., prompt="Enter your name")) -> None:
    """
    Greet the user with a personalized message.

    Args:
        name: The name of the user to greet.
    """
    print(f"{APP_NAME} from @{name}")


if __name__ == "__main__":
    typer.run(main)
