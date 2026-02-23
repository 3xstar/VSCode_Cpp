import sys
sys.path.append('c:/VSCODE/postgresql/dao(recipe_manager)')
from services.recipesService import RecipeRepository

recipe_service = RecipeRepository()

def refresh_recipes():
    global recipes
    recipes = recipe_service.get_all()
    
    if not recipes:
        print("\n📭 Список рецептов пуст")
        return
    
    print("\n" + "-"*100)
    print(f"{'ID':<3} {'Название':<15} {'Категория':<10} {'Сложность':<10} {'Описание'}")
    print("-"*100)
    
    # Словарь для соответствия id категории и названия
    categories = {1: "Супы", 2: "Салаты", 3: "Выпечка", 6: "Напитки"}
    
    for recipe in recipes:
        cat_name = categories.get(recipe[2], f"ID:{recipe[2]}")
        # Обрезаем описание если слишком длинное
        desc = recipe[4]
        
        print(f"{recipe[0]:<3} {recipe[1]:<15} {cat_name:<10} {recipe[3]:<10} {desc}")
    
    print("-"*100 + "\n")


try:
    while(True):
        print("===МЕНЮ ДЛЯ РАБОТЫ С БАЗОЙ ДАННЫХ RECIPE_MANAGER===")
        print("1 - Показать все рецепты\n"
        "2 - Добавить рецепт\n"
        "3 - Изменить рецепт\n"
        "4 - Удалить рецепт\n"
        "5 - Получить рецепты по категории\n"
        "0 - Выход")
        action = int(input("Введите номер действия: "))

        try:
            if action == 1:
                print("\nСписок рецептов:")
                refresh_recipes()

            if action == 2:
                name = input("\nВведите название рецепта: ")
                category = input("Введите название категории рецепта: ")
                level = input("Введите уровень сложности рецепта: ")
                description = input("Введите описание рецепта: ")

                recipe_service.add(name, category, level, description)
                refresh_recipes()

            if action == 3:
                category = input("\nВведите название категории рецепта для изменения: ")
                id = int(input("Введите id рецепта из категории: "))
                name = input("Введите новое название рецепта: ")
                level = input("Введите новый уровень сложности рецепта: ")
                description = input("Введите новое описание рецепта: ")

                recipe_service.edit(id, name, category, level, description)
                refresh_recipes()

            if action == 4:
                id = int(input("\nВведите id рецепта для удаления: "))
                recipe_service.drop(id)
                refresh_recipes()

            if action == 5:
                category = input("\nВведите название категории для получения рецептов: ")
                print(recipe_service.get_by_category(category), "\n")


            if action == 0:
                break

        except Exception as e:
            print("Неизвестная ошибка внутри выбора задач\n")

except Exception as e:
            print("Неизвестная ошибка внутри меню\n")