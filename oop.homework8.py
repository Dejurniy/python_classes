import threading
import json

import requests


class ImgDownloader:
    def __init__(self):
        self.images = []

    def read_json(self):
        with open("images.json") as img:
            json.load(img)
            self.images.append(img)

    def img_download(self):
        for url in self.images:
            data = requests.get(url)
            print(data)
            # with open("")


a = ImgDownloader()
print(a.img_download())
