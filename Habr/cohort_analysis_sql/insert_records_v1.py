import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from datetime import datetime

start_time = datetime.now()

# Подключение к БД
engine = create_engine('postgresql://postgres:gfhjkm@localhost:5432/db')

print("Database opened successfully")

# Путь к исходнику с данными
path_to_data = "C:/Users/Pavel/PycharmProjects/database/"
# Считываем данные в датафрейм
sale_records = pd.read_csv(os.path.join(path_to_data, "СohortAnalysis_2016_2018.csv"),
                           sep=";", parse_dates=["date"], dayfirst=True)
postgresql_table = "sales"
# Записываем датасет в БД
sale_records.to_sql(postgresql_table, engine, if_exists='append', index=False)

print("Operation done successfully")

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
