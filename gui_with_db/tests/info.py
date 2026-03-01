'''
Mock - объект-заглушка, который производит имитацию реального объекта.

Подключаемые модули:
pytest
unittest.moc import patch, MagicMock

TestRecipeGetAll
Тестирует метод get_all() сервиса рецептов:

test_get_all_return_list - проверяет, что метод возвращает список рецептов и корректно обрабатывает данные из БД

test_get_all_calls_corret_query - проверяет, что выполняется правильный SQL запрос (SELECT из таблицы recipes)

test_get_all_handles_db_error - проверяет обработку ошибок БД (исключений)

test_get_all_closes_resources - проверяет, что ресурсы (курсор и соединение) корректно закрываются

TestRecipeAddRecipe
Тестирует метод add_recipe() сервиса рецептов:

test_add_recipe_success - проверяет успешное добавление рецепта и возврат ID новой записи

test_add_recipe_calls_correct_query - проверяет выполнение правильного SQL запроса (INSERT с параметрами)

test_add_recipe_rollback_on_error - проверяет откат транзакции при возникновении ошибки

test_add_recipe_closes_resources - проверяет закрытие ресурсов после операции

test_add_recipe_invalid_data - проверяет обработку некорректных входных данных

TestRecipeGetById
Тестирует метод get_by_id() сервиса рецептов:

test_get_by_id_return_recipe - проверяет получение рецепта по существующему ID

test_get_by_id_return_none_for_invalid_id - проверяет возврат None для несуществующего ID

test_get_by_id_calls_correct_query - проверяет выполнение правильного SQL запроса (SELECT с WHERE)

test_get_by_id_handles_db_error - проверяет обработку ошибок БД

test_get_by_id_closes_resources - проверяет закрытие ресурсов

test_get_by_id_validates_id_type - проверяет работу с разными типами ID (число, строка)


'''