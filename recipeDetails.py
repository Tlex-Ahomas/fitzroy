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
        self.scroll_area.setGeometry(0, 130, 591, 161)
        self.scroll_area.setWidgetResizable(True)

        self.grid = QGridLayout()
        self.grid.addWidget(self.scroll_area)

        self.labels()

        self.setLayout(self.grid)

    def displayRecipe(self, recipe_num):
        self.clear()
        self.labels()
        currentRecipe = self.recipe_processor.get_recipe(recipe_num)
        recipe_img = currentRecipe.get_image()
        recipe_img = open(recipe_img, "rb").read()
        my_image = QImage()
        my_image.loadFromData(recipe_img)
        recipe_img2 = QPixmap(currentRecipe.get_image())
        label = QLabel(self)
        label.setPixmap(recipe_img2)
        #recipe_img = QLabel(recipe_img)
        num = QLabel(str(recipe_num + 1))
        name = QLabel(str(currentRecipe.get_name()))
        prep = QLabel(str(currentRecipe.get_prep_time()))
        cook = QLabel(str(currentRecipe.get_cook_time()))
        description = QLabel(str(currentRecipe.get_description()))
        description.setWordWrap(True)
        scroll_desc = QScrollArea()
        scroll_desc.setWidget(description)
        ingredients = ""
        for item in currentRecipe.get_ingredients():
            ingredients = ingredients + item + "\n"
        ingredients = QLabel(ingredients)
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
    gui.displayRecipe(2)
    gui.show()
    sys.exit(app.exec_())
