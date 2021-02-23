import psycopg2

# Подключение к БД
conn = psycopg2.connect("dbname='db' user='postgres' password='gfhjkm' host='localhost' port='5432'")

print("Database opened successfully")

# Создаем курсор
cursor = conn.cursor()

with conn:
    cursor.execute("""
            DROP TABLE IF EXISTS dataset;
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS dataset (
              invoiceno INTEGER NOT NULL, 
              stockcode TEXT NOT NULL,
              description TEXT NOT NULL,
              quantity INTEGER NOT NULL,
              invoicedate DATE NOT NULL,
              unitprice REAL NOT NULL,
              customerid INTEGER NOT NULL,
              country TEXT NOT NULL);
        """)


print("Operation done successfully")

# Закрываем соединение и курсор
cursor.close()
conn.close()
