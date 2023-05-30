import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os

# загружаем переменные окружения из файла .env
#load_dotenv()

# подключениe к базе данных
#user = os.getenv("POSTGRES_USER")
#password = os.getenv("POSTGRES_PASSWORD")
#host=os.getenv("POSTGRES_HOST")
#port = os.getenv("POSTGRES_PORT")
#database = os.getenv("POSTGRES_DB")

user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
host = os.environ.get('POSTGRES_HOST')
port = os.environ.get('POSTGRES_PORT')
database = os.environ.get('POSTGRES_DB')

print(user)
print(password)


# устанавливаем соединение с базой данных
def get_users():
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)

    # создаем таблицу users
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE IF NOT EXISTS users
                            (ID SERIAL PRIMARY KEY     NOT NULL,
                            NAME  TEXT NOT NULL,
                            SURNAME TEXT NOT NULL,
                            AGE INT NOT NULL); '''
    cursor.execute(create_table_query)
    connection.commit()

    select_query = "SELECT COUNT(*) FROM users"
    cursor.execute(select_query)
    result = cursor.fetchone()
    
    if result[0] == 0:
        # если таблица пустая, добавляем пользователей
        insert_query = "INSERT INTO users (name, surname, age) VALUES (%s, %s, %s)"
        users_to_insert = [("John", "Doe", 30), ("Jane", "Smith", 25), ("Bob", "Johnson", 40)]
        cursor.executemany(insert_query, users_to_insert)
        connection.commit()
        print("Пользователи добавлены в таблицу")

    # выводим все записи из таблицы users
    select_query = "SELECT * from users"
    cursor.execute(select_query)
    records = cursor.fetchall()
    connection.close()
    return records 

if __name__ == '__main__':
    users = get_users()
    print("Все записи в таблице users:")
    for record in users:
        print(record)
