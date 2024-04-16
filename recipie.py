import datetime
import dateparser
import urllib.request
import requests

class Recipie:
    img_count = 0
    def __init__(self):
        self.name = ""
        self.description = ""
        self.recipie_yield = 0
        self.prep_time = datetime.datetime
        self.cook_time = datetime.datetime
        self.image = f"image{Recipie.img_count}.jpg"
        Recipie.img_count += 1

    def get_name(self):
        return self.name

    def get_prep_time(self):
        return self.prep_time

    def get_cook_time(self):
        return self.cook_time

    def get_recipie_yield(self):
        return self.recipie_yield

    def set_image(self, url):
        bytes = requests.get(url).content
        img_file = open(self.image, "wb")
        img_file.write(bytes)

    def get_image(self):
        return self.image
