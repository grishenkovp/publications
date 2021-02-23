import pandas as pd
import numpy as np
import datetime as dt

pd.set_option('display.max_columns', 10)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('dataset.csv', sep=',', index_col=[0])

#Приводим названия столбцов датасета к нижнему регистру
df.columns = [_.lower() for _ in df.columns.values]
#Трансформируем строку-дату в правильный формат и избавляемся от времени
df['invoicedate'] = pd.to_datetime(df['invoicedate'], format='%m/%d/%Y %H:%M')
df['invoicedate'] = df['invoicedate'].dt.normalize()
#Удаляем строки с пропусками и возвратами
df_for_report = df.loc[(~df['description'].isnull()) &
                       (~df['customerid'].isnull()) &
                       (~df['invoiceno'].str.contains('C', case=False))]
#Назначаем всем числовым столбцам правильные форматы
convert_dict = {'invoiceno': int, 'customerid': int, 'quantity': int, 'unitprice': float}
df_for_report = df_for_report.astype(convert_dict)

#Контроль проведенных преобразований
# print(df_for_report.head(3))
# print(df_for_report.dtypes)
# print(df_for_report.isnull().sum())
# print(df_for_report.info())

#Выгружаем датасет в новый файл формата csv
df_for_report.to_csv('dataset_for_report.csv', sep=";", index=False)
