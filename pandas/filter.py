import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/postgres')

query = "SELECT * FROM recipes.recipes"
df = pd.read_sql(query, engine)

name = input("Введите названия блюда: ");

# По категории
soups = df[df["category_id"] == 5] # Получаю все супа
borsh = df[df["name"].str.contains(name)] # Получаю все борщи

print(soups)
print(borsh)

# Альтернативный способ через SQL-запрос
query = "SET search_path to postgres, recipes;\nSELECT name, category_id FROM recipes GROUP BY category_id, name HAVING category_id = 5;"
df = pd.read_sql(query, engine)
print(df)