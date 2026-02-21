from sqlalchemy import create_engine

def get_conn():
    return create_engine('postgresql+psycopg2://postgres:200718za@localhost:5432/recipe_manager_db')