import os
import pandas as pd
from config.settings import settings

def load_data(code, date_from, date_to, ver='v4'):
    if ver in ['v3', 'v4']:
        return load_data_v3_v4(code, date_from, date_to, ver)

    df = pd.read_csv(
        os.path.join(settings.DATA_DIR, ver, f'{code}.csv'),
        parse_dates=['date'],
        thousands=',',
        converters={'date': lambda x: pd.to_datetime(x, format='%Y%m%d')})

    # 날짜 오름차순 정렬
    df = df.sort_values(by='date').reset_index(drop=True)

    # 기간 필터링
    df = df[(df['date'] >= date_from) & (df['date'] <= date_to)]
    df = df.fillna(method='ffill').reset_index(drop=True)

    return df

def load_data_v3_v4(code, date_from, date_to, ver):
    # 시장 데이터
    df_marketfeatures = pd.read_csv(
        os.path.join(settings.DATA_DIR, ver, 'marketfeatures.csv'), 
        parse_dates=['date'],
        thousands=',')
    
    # 종목 데이터
    df_stockfeatures = pd.read_csv(
        os.path.join(settings.DATA_DIR, ver, f'{code}.csv'), 
        parse_dates=['date'],
        thousands=',')

    # 시장 데이터와 종목 데이터 합치기
    df = pd.merge(df_stockfeatures, df_marketfeatures, on='date', how='left', suffixes=('', '_dup'))
    df = df.drop(df.filter(regex='_dup$').columns.tolist(), axis=1)

    # 날짜 오름차순 정렬
    df = df.sort_values(by='date').reset_index(drop=True)

    # 기간 필터링
    df = df[(df['date'] >= date_from) & (df['date'] <= date_to)]
    df = df.fillna(method='ffill').reset_index(drop=True)

    return df