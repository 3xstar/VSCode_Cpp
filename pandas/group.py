import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/public')

query = "SELECT * FROM public.recipes"
df = pd.read_sql(query, engine)

new_recipes = pd.DataFrame({
    'name': ["Паста", "Стейк из Лосося"],
    "category_id": [3,2],
    "characters": ["Харауктеристкиа 7", "Характеристика 8"],
    "duration": ["00:30:00", "01:10:00"]
})

df.groupby("category_id").size()
print(df)