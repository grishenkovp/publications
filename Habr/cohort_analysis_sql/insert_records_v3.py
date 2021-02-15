import psycopg2
from datetime import datetime

start_time = datetime.now()

# Подключение к БД
conn = psycopg2.connect("dbname='db' user='postgres' password='gfhjkm' host='localhost' port='5432'")
print("Database opened successfully")

# Создаем курсор
cursor = conn.cursor()


# Открываем файл. Считываем его построчно с записью в БД
with open('СohortAnalysis_2016_2018.csv', 'r', encoding='UTF8') as f:
    next(f)
    cursor.copy_from(f, 'sales', sep=';', columns=('date','promo','site','user_id','transaction_id','amount'))
    conn.commit()

f.close()

print("Operation done successfully")

# Закрываем соединение и курсор
cursor.close()
conn.close()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))