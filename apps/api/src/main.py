from devtools import debug

from app import app
from config import app_config


def main() -> None:
    debug(app_config)

    app.start(host=app_config.api_host, port=app_config.api_port)


if __name__ == "__main__":
    main()
