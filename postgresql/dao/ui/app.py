import sys
sys.path.append('c:/VSCODE/postgresql/dao')
from services.recipesService import RecipeService

recipe_service = RecipeService()

recipes = recipe_service.get_all()

name = input('Введите название рецепта: ')
category = input('Тут будет select/combo box, а пока что напишите название: ')
level = input('Тут будет select/combo box, а пока что напишите уровень сложности: ')
description = input('Введите описание или впишите 0, если хотите оставить его пустым: ')

if description == '0':
    description = None

recipe_service.add(name, category, level, description)