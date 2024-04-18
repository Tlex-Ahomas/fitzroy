from recipie import Recipie
import json

class RecipieProcessor:
    def load_recipies(self, json_file):
        # opens json file
        js = open(json_file, encoding="utf-8")
        recipie_data = json.load(js, )
        recipies = []
        # stores each recipie in json in the recipies list
        for i in recipie_data:
            recipies.append(Recipie(*i.values()))

        # characters for loading bar
        bar = "█"
        rem_bar = "░"
        green = "\33[32m"
        reset = "\33[0m"
        # loops through recipes, downloads images with loading bar to keep track
        for r in range(len(recipies)):
            bar_count = int(((r+1)/len(recipies)) * 75)
            print(f"Downloading image {r+1} of {len(recipies)} {green}{bar*bar_count}{rem_bar*(75-bar_count)}{reset}", end="\r")
            recipies[r].set_image(recipies[r].image_url)
        print("")
