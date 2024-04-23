from recipe import Recipe
import json


class RecipeProcessor:
    #recipes = []
    def __init__(self):
        self.recipes = []

    def load_recipes(self, json_file):
        # opens json file
        js = open(json_file, encoding="utf-8")
        recipie_data = json.load(js, )
        # stores each recipie in json in the recipes list
        for i in recipie_data:
            self.recipes.append(Recipe(*i.values()))

        # characters for loading bar
        bar = "█"
        rem_bar = "░"
        green = "\33[32m"
        reset = "\33[0m"
        # loops through recipes, downloads images with loading bar to keep track
        for r in range(len(self.recipes)):
            bar_count = int(((r+1) / len(self.recipes)) * 75)
            print(f"Downloading image {r+1} of {len(self.recipes)} {green}{bar * bar_count}{rem_bar * (75 - bar_count)}{reset}", end="\r")
            self.recipes[r].set_image(self.recipes[r].image_url)
        print("")

    def get_recipe_list(self):
        return self.recipes

    def get_num_recipes(self):
        return len(self.recipes)

    def get_recipe(self, ind):
        if 0 <= ind < len(self.recipes):
            return self.recipes[ind]
        raise Exception('index out of bounds')

#recipeProcessor = RecipeProcessor()
