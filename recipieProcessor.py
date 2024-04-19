from recipie import Recipie
import json


class RecipieProcessor:
    def __init__(self):
        self.recipies = []

    def load_recipies(self, json_file):
        # opens json file
        js = open(json_file, encoding="utf-8")
        recipie_data = json.load(js, )
        # stores each recipie in json in the recipies list
        for i in recipie_data:
            self.recipies.append(Recipie(*i.values()))

        # characters for loading bar
        bar = "█"
        rem_bar = "░"
        green = "\33[32m"
        reset = "\33[0m"
        # loops through recipes, downloads images with loading bar to keep track
        for r in range(len(self.recipies)):
            bar_count = int(((r+1)/len(self.recipies)) * 75)
            print(f"Downloading image {r+1} of {len(self.recipies)} {green}{bar*bar_count}{rem_bar*(75-bar_count)}{reset}", end="\r")
            self.recipies[r].set_image(self.recipies[r].image_url)
        print("")

    def recipies(self):
        return self.recipies

    def get_num_recipies(self):
        return len(self.recipies)

    def get_recipie(self, ind):
        if 0 <= ind < len(self.recipies):
            return self.recipies[ind]
        raise Exception('index out of bounds')
