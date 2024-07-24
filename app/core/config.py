import sys


class Settings:

    LOGGING_CONFIG = {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": "{time:YYYY-MM-DD HH:mm:ss} {level} user:{extra[user]} func:{extra[func_name]}({extra[action]}) {message}",
            },
            {
                "sink": "./log/info.log",
                "serialize": True,
                "format": "{time:YYYY-MM-DD HH:mm:ss} {level} user:{extra[user]} func:{extra[func_name]}({extra[action]}) {message}",
                "rotation": "200kB",
                "compression": "zip",
            },
        ],
        "extra": {"user": "someone"},
    }

    DB_URL = "sqlite+aiosqlite://"
    DB_ECHO = True


settings = Settings()
