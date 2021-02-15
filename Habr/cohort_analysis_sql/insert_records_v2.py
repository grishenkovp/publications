import os
import pandas as pd
import psycopg2
from datetime import datetime

start_time = datetime.now()

# Подключение к БД
conn = psycopg2.connect("dbname='db' user='postgres' password='gfhjkm' host='localhost' port='5432'")
print("Database opened successfully")

# Создаем курсор
cursor = conn.cursor()

# Путь к исходнику с данными
path_to_data = "C:/Users/Pavel/PycharmProjects/database/"
# Считываем данные в датафрейм
sale_records = pd.read_csv(os.path.join(path_to_data, "СohortAnalysis_2016_2018.csv"),
                           sep=";", parse_dates=["date"], dayfirst=True)

query = "INSERT INTO sales (date, promo, site, user_id, transaction_id, amount) values (%s, %s, %s, %s, %s, %s)"
dataset_for_db = sale_records.values.tolist()

cursor.executemany(query, dataset_for_db)
conn.commit()

print("Operation done successfully")

# Закрываем соединение и курсор
cursor.close()
conn.close()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
