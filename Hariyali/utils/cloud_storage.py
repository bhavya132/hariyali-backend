import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContentSettings, ContainerClient, __version__
connect_str = os.getenv('STORAGE_CONN')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_name = "imageanalysis"


class CloudStorage:
    @classmethod
    def upload(self, filepath, filename):
        my_content_settings = ContentSettings(content_type='image/jpg')
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
        with open(filepath, "rb") as data:
            blob_client.upload_blob(data, overwrite=True, content_settings=my_content_settings)
        return "https://profile2019uce0056.blob.core.windows.net/imageanalysis/" + filename

    @classmethod
    def delete(self, filename):
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
        blob_client.delete_blob()