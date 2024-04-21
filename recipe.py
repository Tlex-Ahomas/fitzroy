import datetime
import dateparser
import urllib.request
import requests

class Recipe:
    def __init__(self, name, desc, img_url, _yield, cook_t, prep_t, ingredients):
        self.name = name
        self.description = desc
        self.recipie_yield = _yield
        self.prep_time = prep_t
        self.cook_time = cook_t
        self.ingredients = ingredients
        self.image_url = img_url
        img_name = img_url.split("/") # image name is end of url
        self.image = img_name[len(img_name)-1]

    def get_name(self):
        return self.name

    def get_prep_time(self):
        return self.prep_time

    def get_cook_time(self):
        return self.cook_time

    def get_recipe_yield(self):
        return self.recipie_yield

    # downloads image from url
    def set_image(self, url):
        try:
            bytes = requests.get(url).content
            img_file = open(self.image, "wb")
            img_file.write(bytes)
        except Exception as e:
            self.image = "img_not_found.png"

    def get_image(self):
        return self.image
