import os
import requests


def download(url: str, dest_folder: str, dest_file: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = dest_file.replace(" ", "_").replace(
        "/", " "
    )  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 8):
            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())
