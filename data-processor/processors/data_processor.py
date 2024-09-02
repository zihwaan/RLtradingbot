import pandas as pd
import numpy as np
from utils.data_loader import load_data
from .feature_calculator import calculate_features

COLUMNS_CHART_DATA = ['date', 'open', 'high', 'low', 'close', 'volume']

def process_data(code, date_from, date_to, ver='v4'):
    # 데이터 로드
    df = load_data(code, date_from, date_to, ver)
    
    # 특성 계산
    df = calculate_features(df)
    
    # 차트 데이터와 학습 데이터 분리
    chart_data = df[COLUMNS_CHART_DATA]
    
    training_columns = [
        'open_lastclose_ratio', 'high_close_ratio', 'low_close_ratio',
        'close_lastclose_ratio', 'volume_lastvolume_ratio',
        'close_ma5_ratio', 'volume_ma5_ratio',
        'close_ma10_ratio', 'volume_ma10_ratio',
        'close_ma20_ratio', 'volume_ma20_ratio',
        'close_ma60_ratio', 'volume_ma60_ratio',
        'close_ma120_ratio', 'volume_ma120_ratio',
    ]
    
    if ver in ['v1.1', 'v2', 'v3', 'v4']:
        training_columns += [
            'inst_lastinst_ratio', 'frgn_lastfrgn_ratio',
            'inst_ma5_ratio', 'frgn_ma5_ratio',
            'inst_ma10_ratio', 'frgn_ma10_ratio',
            'inst_ma20_ratio', 'frgn_ma20_ratio',
            'inst_ma60_ratio', 'frgn_ma60_ratio',
            'inst_ma120_ratio', 'frgn_ma120_ratio',
        ]
    
    if ver in ['v2', 'v3', 'v4']:
        training_columns += ['per', 'pbr', 'roe']
        df.loc[:, ['per', 'pbr', 'roe']] = df[['per', 'pbr', 'roe']].apply(lambda x: x / 100)
        training_columns += [
            'market_kospi_ma5_ratio', 'market_kospi_ma20_ratio', 
            'market_kospi_ma60_ratio', 'market_kospi_ma120_ratio', 
            'bond_k3y_ma5_ratio', 'bond_k3y_ma20_ratio', 
            'bond_k3y_ma60_ratio', 'bond_k3y_ma120_ratio',
        ]
    
    if ver in ['v3', 'v4']:
        training_columns += [
            'ind', 'ind_diff', 'ind_ma5', 'ind_ma10', 'ind_ma20', 'ind_ma60', 'ind_ma120',
            'inst', 'inst_diff', 'inst_ma5', 'inst_ma10', 'inst_ma20', 'inst_ma60', 'inst_ma120',
            'foreign', 'foreign_diff', 'foreign_ma5', 'foreign_ma10', 'foreign_ma20', 
            'foreign_ma60', 'foreign_ma120',
        ]
        training_columns = [col if col != 'close_lastclose_ratio' else 'diffratio' for col in training_columns]
    
    training_data = df[training_columns]
    
    return chart_data, training_data