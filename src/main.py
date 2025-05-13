import os

from database import establish_connection

def get_expired_uploads():
    try:
        conn, cursor = establish_connection()

        cursor.execute("SELECT upload_id, name FROM uploads WHERE DATEDIFF(NOW(), upload_date) > 1")
        expired_uploads = cursor.fetchall()

        cursor.close()
        conn.close()

        return expired_uploads
    except:
        raise
    finally:
        cursor.close()
        conn.close()

def delete_upload(upload_id):
    try:
        conn, cursor = establish_connection()

        cursor.execute("DELETE FROM uploads WHERE upload_id = %d", (upload_id,))
        conn.commit()
    except:
        raise
    finally:
        cursor.close()
        conn.close()

def delete_expired_uploads():
    try:
        uploads = get_expired_uploads()

        for upload in uploads:
            upload_id = upload[0]
            upload_name = upload[1]

            delete_upload(upload_id)
            os.remove(f"/srv/share/uploads/{upload_name}")
    except Exception as e:
        print(f"Error: {e}")

delete_expired_uploads()