
import os
from importlib import import_module

def get_connection():
    try:
        connector = import_module("mysql.connector")
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "MySQL connector is unavailable; install the 'mysql-connector-python' package."
        ) from exc

    return connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.environ["DB_PASSWORD"],
        database=os.getenv("DB_NAME", "ecommerce")
    )