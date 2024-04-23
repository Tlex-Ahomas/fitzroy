from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from recipeProcessor import RecipeProcessor
import sys

class RecipeDetails(QDialog):

    def __init__(self, recipe_processor, parent=None, ):
        super(RecipeDetails, self).__init__(parent)
        self.recipe_processor = recipe_processor
        self.setWindowTitle("Recipe Details")
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.grid = QGridLayout()
        self.grid.addWidget(self.scroll_area)

        self.labels()

        self.setLayout(self.grid)

    def display_recipe(self, recipe_num):
        self.clear()
        self.labels()
        current_recipe = self.recipe_processor.get_recipe(recipe_num)
        recipe_img = QPixmap(current_recipe.get_image())
        label = QLabel(self)
        label.setPixmap(recipe_img)
        num = QLabel(str(recipe_num + 1))
        name = QLabel(str(current_recipe.get_name()))
        prep = QLabel(str(current_recipe.get_prep_time()))
        cook = QLabel(str(current_recipe.get_cook_time()))
        description = QLabel(str(current_recipe.get_description()))
        description.setWordWrap(True)
        scroll_desc = QScrollArea()
        scroll_desc.setWidget(description)
        ingredients = ""
        for item in current_recipe.get_ingredients():
            ingredients = ingredients + item + "\n"
        ingredients = QLabel(ingredients)
        recipe_yield = QLabel(str(current_recipe.get_recipe_yield()))
        
        scroll_ing = QScrollArea()
        scroll_ing.setWidget(ingredients)
        recipe_yield = QLabel(str(currentRecipe.get_recipe_yield()))


        self.grid.addWidget(label, 0, 0, 1, 0)
        self.grid.addWidget(num, 1, 1)
        self.grid.addWidget(name, 2, 1)
        self.grid.addWidget(prep, 3, 1)
        self.grid.addWidget(cook, 4, 1)
        self.grid.addWidget(scroll_desc, 5, 1)
        self.grid.addWidget(scroll_ing, 6, 1)
        self.grid.addWidget(recipe_yield, 7, 1)

        self.setLayout(self.grid)
        self.show()

    def clear(self):
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

    def labels(self):
        num_label = QLabel("Recipe #: ")
        name_label = QLabel("Recipe Name: ")
        prep_label = QLabel("Prep Time: ")
        cook_label = QLabel("Cook Time: ")
        description_label = QLabel("Description: ")
        ingredients_label = QLabel("Ingredients: ")
        recipe_yield_label = QLabel("Recipe Yield: ")

        self.grid.addWidget(num_label, 1, 0)
        self.grid.addWidget(name_label, 2, 0)
        self.grid.addWidget(prep_label, 3, 0)
        self.grid.addWidget(cook_label, 4, 0)
        self.grid.addWidget(description_label, 5, 0)
        self.grid.addWidget(ingredients_label, 6, 0)
        self.grid.addWidget(recipe_yield_label, 7, 0)

def main():
    app = QApplication(sys.argv)
    rp = RecipeProcessor()
    rp.load_recipes("recipes.json")
    gui = RecipeDetails(rp)
    gui.display_recipe(2)
    gui.show()
    sys.exit(app.exec_())
