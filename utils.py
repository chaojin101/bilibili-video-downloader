import requests


def download(url: str, filename: str, headers={}):
    with requests.get(url, headers=headers) as response:
        with open(filename, "wb") as file:
            file.write(response.content)
