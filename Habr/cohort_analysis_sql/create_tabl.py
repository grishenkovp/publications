import psycopg2

# Подключение к БД
conn = psycopg2.connect("dbname='db' user='postgres' password='gfhjkm' host='localhost' port='5432'")

print("Database opened successfully")

# Создаем курсор
cursor = conn.cursor()

with conn:
    cursor.execute("""
            DROP TABLE IF EXISTS sales;
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
              id SERIAL PRIMARY KEY,
              date DATE NOT NULL, 
              promo TEXT NOT NULL,
              site TEXT NOT NULL,
              user_id TEXT NOT NULL,
              transaction_id INTEGER NOT NULL,
              amount INTEGER NOT NULL);
        """)


print("Operation done successfully")

# Закрываем соединение и курсор
cursor.close()
conn.close()
