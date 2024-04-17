from recipie import Recipie
import json

class RecipieProcessor:
    def load_recipies(self, json_file):
        js = open(json_file, encoding="utf-8")
        recipie_data = json.load(js, )
        recipies = []
        for i in recipie_data:
            recipies.append(Recipie(*i.values()))

        bar = "█"
        rem_bar = "░"
        green = "\33[32m"
        reset = "\33[0m"
        for r in range(len(recipies)):
            bar_count = int(((r+1)/len(recipies)) * 75)
            print(f"Downloading image {r+1} of {len(recipies)} {green}{bar*bar_count}{rem_bar*(75-bar_count)}{reset}", end="\r")
            recipies[r].set_image(recipies[r].image_url)
        print("")
