# импорт библиотек
import pandas as pd

# опции отображения
pd.set_option('display.max_columns', 10)
pd.set_option('display.expand_frame_repr', False)
# Путь к к обрабатываемому датасету с данными
path_data = 'ecommerce_data.csv'


def func_main(path: str) -> pd.DataFrame:
    """Предварительная обработка датасета"""
    # Считываем датасет
    df = pd.read_csv(path, sep=',')
    # Приводим названия столбцов датасета к нижнему регистру
    list_col = list(map(str.lower, df.columns))
    df.columns = list_col
    # Избавляемся от времени и трансформируем строку-дату в правильный формат
    df['invoicedate'] = df['invoicedate'].apply(lambda x: x.split(' ')[0])
    df['invoicedate'] = pd.to_datetime(df['invoicedate'], format='%m/%d/%Y')
    # Рассчитываем сумму покупки по каждому товару
    df['amount'] = df['quantity'] * df['unitprice']
    # Удаляем ненужные для дальнейшего анализа столбцы
    df = df.drop(['stockcode', 'description', 'quantity', 'unitprice'], axis=1)
    # Заполняем строки, где не указан номер покупателя, константой 777777
    values = {'customerid': 777777}
    df = df.fillna(value=values)
    df['customerid'] = df['customerid'].astype('int')
    # Округляем общую сумму покупки до целового числа
    df = df.round({'amount': 0})
    df['amount'] = df['amount'].astype('int')
    # Удаляем все строки, в которых есть пропуски перед группировкой
    df = df.dropna()
    # Группируем строки, чтобы прийти к детализации до уровня одного чека
    df_result = df.groupby(by=['invoiceno', 'invoicedate', 'customerid', 'country']).agg({'amount': sum}).reset_index()
    return df_result


if __name__ == "__main__":
    tbl = func_main(path_data)
    tbl.to_csv('ecommerce_data_new.csv', sep=',', index=False, date_format='%d.%m.%Y')
    print('A file is genereted!')
