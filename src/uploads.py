import psycopg
import boto3
import yaml
import os

from database import get_connection

CONFIG = yaml.safe_load(open(f"{os.getcwd().replace("\\", "/")}/config.yaml"))

def get_expired_uploads():
    connection = get_connection()

    cursor = connection.cursor(row_factory=psycopg.rows.dict_row)

    try:
        cursor.execute("SELECT title, upload_id FROM share.uploads WHERE EXTRACT(DAY FROM (NOW() - share.uploads.upload_date)) > 2")
        uploads = cursor.fetchall()

        return uploads
    except:
        raise
    finally:
        cursor.close()
        connection.close()

def delete_upload_from_database(upload_id):
    connection = get_connection()

    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM share.uploads WHERE upload_id = %s", (upload_id,))
        connection.commit()
    except:
        raise
    finally:
        cursor.close()
        connection.close()

def delete_upload_from_storage(upload_id):
    client = boto3.client(
        "s3", 
        endpoint_url=CONFIG["storage"]["endpoint_url"], 
        aws_access_key_id=CONFIG["storage"]["access_key_id"], 
        aws_secret_access_key=CONFIG["storage"]["secret_access_key"]
    )

    client.delete_object(Bucket="share", Key=f"uploads/{upload_id}")