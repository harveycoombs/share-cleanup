import mysql.connector
import json

def establish_connection():
    with open("../config.json", "r") as f:
        config = json.load(f)

    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    cursor = conn.cursor()

    return conn, cursor