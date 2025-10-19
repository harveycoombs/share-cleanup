import os
import psycopg
import yaml

CONFIG = yaml.safe_load(open(f"{os.getcwd().replace("\\", "/")}/config.yaml"))

def get_connection():
    return psycopg.connect(
        host=CONFIG["database"]["host"],
        user=CONFIG["database"]["user"],
        password=CONFIG["database"]["password"],
        dbname=CONFIG["database"]["schema"]
    )