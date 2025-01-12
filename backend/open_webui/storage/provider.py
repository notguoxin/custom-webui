import os
from botocore.exceptions import ClientError
import shutil


from typing import BinaryIO, Tuple, Optional, Union

from open_webui.constants import ERROR_MESSAGES
from open_webui.config import (
    STORAGE_PROVIDER,
    UPLOAD_DIR,
)


from botocore.exceptions import ClientError
from typing import BinaryIO, Tuple, Optional


class StorageProvider:
    def __init__(self, provider: Optional[str] = None):
        self.storage_provider: str = provider or STORAGE_PROVIDER

    def _upload_to_local(self, contents: bytes, filename: str) -> Tuple[bytes, str]:
        """Handles uploading of the file to local storage."""
        file_path = f"{UPLOAD_DIR}/{filename}"
        with open(file_path, "wb") as f:
            f.write(contents)
        return contents, file_path

    def _get_file_from_local(self, file_path: str) -> str:
        """Handles downloading of the file from local storage."""
        return file_path

    def _delete_from_local(self, filename: str) -> None:
        """Handles deletion of the file from local storage."""
        file_path = f"{UPLOAD_DIR}/{filename}"
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            print(f"File {file_path} not found in local storage.")

    def _delete_all_from_local(self) -> None:
        """Handles deletion of all files from local storage."""
        if os.path.exists(UPLOAD_DIR):
            for filename in os.listdir(UPLOAD_DIR):
                file_path = os.path.join(UPLOAD_DIR, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Remove the file or link
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Remove the directory
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        else:
            print(f"Directory {UPLOAD_DIR} not found in local storage.")

    def upload_file(self, file: BinaryIO, filename: str) -> Tuple[bytes, str]:
        """Uploads a file either to S3 or the local file system."""
        contents = file.read()
        if not contents:
            raise ValueError(ERROR_MESSAGES.EMPTY_CONTENT)
        contents, file_path = self._upload_to_local(contents, filename)
        return contents, file_path

    def get_file(self, file_path: str) -> str:
        """Downloads a file either from S3 or the local file system and returns the file path."""
        return self._get_file_from_local(file_path)

    def delete_file(self, file_path: str) -> None:
        """Deletes a file either from S3 or the local file system."""
        filename = file_path.split("/")[-1]

        # Always delete from local storage
        self._delete_from_local(filename)

    def delete_all_files(self) -> None:
        """Deletes all files from the storage."""
        if self.storage_provider == "s3":
            self._delete_all_from_s3()

        # Always delete from local storage
        self._delete_all_from_local()


Storage = StorageProvider(provider=STORAGE_PROVIDER)
