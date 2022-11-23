import threading

import requests
import json


class ImageDownloader:
    def __init__(self, json_path):
        with open(json_path) as file:
            self.image_list = json.load(file)

    def png_download(self, url, name):
        response = requests.get(url)
        with open(f"{name}.png", "wb") as photo:
            photo.write(response.content)
            print(f"Image {name} is downloaded!")

    def download_all(self):
        for image in self.image_list:
            self.png_download(url=image["image_url"], name=image["url_name"])

    def download_with_threads(self):
        thread_list = []
        for image in self.image_list:
            x = threading.Thread(target=self.png_download, args=(image["image_url"], image["url_name"]))
            thread_list.append(x)
            x.start()

        for td in thread_list:
            td.join()

        print("Downloaded with threads!")


a = ImageDownloader(json_path="images.json")
# print(a.download_all())
a.download_with_threads()
a.download_all()
