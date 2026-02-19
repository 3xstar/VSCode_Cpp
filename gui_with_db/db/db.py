import psycopg2

def get_conn():
    return psycopg2.connect(
        host='localhost',
        port=5432,
        user='postgresql',
        password='200718za',
        database='restaurant_db',
        client_encoding='utf=8'
    )


'''
Пример

def get_conn():
    return psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password='password',
    database='db_name',
    client_encoding='utf=8')
'''