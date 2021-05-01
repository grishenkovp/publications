import pandas as pd
import sqlite3 as sq

con = sq.connect('C:/Users/Pavel/PycharmProjects/test/sale.db')
cur = con.cursor()

def select(sql):
  return pd.read_sql(sql,con)

sql = '''select *
        from (select s.invoicedate,
                      c.country,
                      pr.description,
                      replace(round(s.amount,1),'.',',') as amount
               from sale as s left join country as c on s.country_id = c.country_id
                            left join product as pr on s.product_id = pr.product_id)'''

tbl = select(sql)
print(tbl)