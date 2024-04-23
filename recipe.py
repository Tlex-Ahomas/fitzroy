from isoduration import parse_duration, format_duration
import requests

class Recipe:
    def __init__(self, name, desc, img_url, _yield, cook_t, prep_t, ingredients):
        self.name = name
        self.description = desc
        self.recipie_yield = _yield
        self.prep_time = self.parse_times(prep_t)
        self.cook_time = self.parse_times(cook_t)
        self.ingredients = ingredients
        self.image_url = img_url
        img_name = img_url.split("/") # image name is end of url
        self.image = img_name[len(img_name)-1]

    def parse_times(self, t):
        if len(t.strip()) == 0:
            return ""
        try:
            dur = parse_duration(t)
            return f"{dur.time.hours + dur.time.minutes//60}:{dur.time.minutes%60 + dur.time.seconds//60}"
        except Exception as e:
            return t

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_prep_time(self):
        return self.prep_time

    def get_cook_time(self):
        return self.cook_time

    def get_recipe_yield(self):
        return self.recipie_yield

    def get_ingredients(self):
        return self.ingredients

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
