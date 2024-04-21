from PyQt5.QtWidgets import *
import sys

class RecipeDetails(QDialog): # need to pass in recipe to get specific details

    def __init__(self, parent=None):
        super(RecipeDetails, self).__init__(parent)

        self.setWindowTitle("Recipe Details")

        num_label = QLabel("Recipe #: ")
        name_label = QLabel("Recipe Name: ")
        prep_label = QLabel("Prep Time: ")
        cook_label = QLabel("Cook Time: ")
        description_label = QLabel("Description: ")
        ingredients_label = QLabel("Ingredients: ")

        scroll_bar = QScrollBar(self)
        recipe_img = ""
        num = ""
        name = ""
        prep = ""
        cook = ""
        description = ""
        description.setVerticalScrollBar(scroll_bar)
        ingredients = ""

        grid = QGridLayout()
        grid.addWidget(recipe_img, 0, 0)
        grid.addWidget(num_label, 1, 0)
        grid.addWidget(num, 1, 1)
        grid.addWidget(name_label, 2, 0)
        grid.addWidget(name, 2, 1)
        grid.addWidget(prep_label, 3, 0)
        grid.addWidget(prep, 3, 1)
        grid.addWidget(cook_label, 4, 0)
        grid.addWidget(cook, 4, 1)
        grid.addWidget(description_label, 5, 0)
        grid.addWidget(description, 5, 1) # needs a scroll bar
        grid.addWidget(ingredients_label, 6, 0)
        grid.addWidget(ingredients, 6, 1)