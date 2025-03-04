
from azure.storage.blob import BlobServiceClient
import os

from dotenv import load_dotenv
import os

load_dotenv()
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Azure Storage Account connection string
# AZURE_STORAGE_CONNECTION_STRING= "string connection from Azure..."
CONTAINER_NAME = "test"

# File to upload
LOCAL_FILE_PATH = r"D:\Antra\Advanced Training\Blob Sample.txt"

def upload_to_blob():
    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        
        # Get the container client
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        
        # Create blob client for the file
        blob_client = container_client.get_blob_client(os.path.basename(LOCAL_FILE_PATH))

        # Upload the file
        with open(LOCAL_FILE_PATH, "rb") as file:
            blob_client.upload_blob(file, overwrite=True)
        
        print(f"File '{LOCAL_FILE_PATH}' uploaded successfully to Azure Blob Storage!")
    
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the function
if __name__ == "__main__":
    upload_to_blob()
