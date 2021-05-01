# импорт библиотек
import pandas as pd
import sqlite3 as sq
from etl1 import func_country,func_product,func_sale

con = sq.connect('sale.db')
cur = con.cursor()

## Таблица Страны
# cur.executescript('''DROP TABLE IF EXISTS country;
#                     CREATE TABLE IF NOT EXISTS country (
#                     country_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     country TEXT NOT NULL UNIQUE);''')
# func_country().to_sql('country',con,index=False,if_exists='append')

## Таблица Товары
# cur.executescript('''DROP TABLE IF EXISTS product;
#                     CREATE TABLE IF NOT EXISTS product (
#                     product_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     stockcode TEXT NOT NULL UNIQUE,
#                     description TEXT);''')
# func_product().to_sql('product',con,index=False,if_exists='append')

## Таблица Продажи (основная)
# cur.executescript('''DROP TABLE IF EXISTS sale;
#                     CREATE TABLE IF NOT EXISTS sale (
#                     sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     invoicedate TEXT NOT NULL,
#                     country_id INTEGER NOT NULL,
#                     product_id INTEGER NOT NULL,
#                     amount REAL NOT NULL,
#                     FOREIGN KEY(country_id)  REFERENCES country(country_id),
#                     FOREIGN KEY(product_id)  REFERENCES product(product_id));''')

## Таблица Продажи (временная)
# cur.executescript('''DROP TABLE IF EXISTS sale_data_lake;
#                     CREATE TABLE IF NOT EXISTS sale_data_lake (
#                     sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     invoicedate TEXT NOT NULL,
#                     country TEXT NOT NULL,
#                     stockcode TEXT NOT NULL,
#                     amount REAL NOT NULL);''')
# func_sale().to_sql('sale_data_lake',con,index=False,if_exists='append')

## Перегружаем данные из вспомогательной таблицы (sale_data_lake) в основную (sale)
# cur.executescript('''INSERT INTO sale (invoicedate, country_id, product_id, amount)
#                     SELECT  sdl.invoicedate, c.country_id, pr.product_id, sdl.amount
#                     FROM sale_data_lake as sdl LEFT JOIN country as c ON sdl.country = c.country
# 						                    LEFT JOIN product as pr ON sdl.stockcode = pr.stockcode
#                     ''')

## Очищаем вспомогательную таблицу
# cur.executescript('''DELETE FROM sale_data_lake''')

def select(sql):
  return pd.read_sql(sql,con)

sql = '''select *
        from (select s.invoicedate,
                      c.country,
                      pr.description,
                      round(s.amount,1) as amount
               from sale as s left join country as c on s.country_id = c.country_id
                            left join product as pr on s.product_id = pr.product_id)'''

print(select(sql))

cur.close()
con.close()