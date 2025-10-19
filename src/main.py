import time
from uploads import get_expired_uploads, delete_upload_from_database, delete_upload_from_storage

def main():
    print("Retrieving expired uploads...")

    uploads = get_expired_uploads()

    print(f"Attempting to delete {len(uploads)} uploads...")

    for upload in uploads:
        print(f"Deleting upload: {upload['title']} ({upload['upload_id']})...")

        delete_upload_from_database(upload['upload_id'])
        delete_upload_from_storage(upload['upload_id'])

        print(f"Upload deleted successfully.")

    print("All uploads deleted successfully.")

if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(86400)