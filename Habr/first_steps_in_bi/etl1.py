# импорт библиотек
import pandas as pd

# опции отображения
pd.set_option('display.max_columns', 10)
pd.set_option('display.expand_frame_repr', False)

path_dataset = 'dataset/ecommerce_data.csv'


# Предварительная обработка датасета
def func_main(path_dataset: str):
    # Считываем датасет
    df = pd.read_csv(path_dataset, sep=',')
    # Приводим названия столбцов датасета к нижнему регистру
    list_col = list(map(str.lower, df.columns))
    df.columns = list_col
    # Избавляемся от времени и трансформируем строку-дату в правильный формат
    df['invoicedate'] = df['invoicedate'].apply(lambda x: x.split(' ')[0])
    df['invoicedate'] = pd.to_datetime(df['invoicedate'], format='%m/%d/%Y')
    # Рассчитываем сумму покупки по каждому товару
    df['amount'] = df['quantity'] * df['unitprice']
    # Удаляем ненужные для дальнейшего анализа столбцы
    df_result = df.drop(['invoiceno', 'quantity', 'unitprice', 'customerid'], axis=1)
    # Задаем порядок вывода столбцов для визуального контроля результата
    df_result = df_result[['invoicedate', 'country', 'stockcode', 'description', 'amount']]
    return df_result


# Таблица Продажи
def func_sale():
    tbl = func_main(path_dataset)
    df_sale = tbl.groupby(['invoicedate', 'country', 'stockcode'])['amount'].sum().reset_index()
    return df_sale


# Таблица Страны
def func_country():
    tbl = func_main(path_dataset)
    df_country = pd.DataFrame(sorted(pd.unique(tbl['country'])), columns=['country'])
    return df_country


# Таблица Товары
def func_product():
    tbl = func_main(path_dataset)
    df_product = tbl[['stockcode','description']].\
        drop_duplicates(subset=['stockcode'], keep='first').reset_index(drop=True)
    return df_product

