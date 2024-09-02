import pandas as pd
import numpy as np

def calculate_features(df):
    windows = [5, 10, 20, 60, 120]
    for window in windows:
        df[f'close_ma{window}'] = df['close'].rolling(window).mean()
        df[f'volume_ma{window}'] = df['volume'].rolling(window).mean()
        df[f'close_ma{window}_ratio'] = (df['close'] - df[f'close_ma{window}']) / df[f'close_ma{window}']
        df[f'volume_ma{window}_ratio'] = (df['volume'] - df[f'volume_ma{window}']) / df[f'volume_ma{window}']
        
    df['open_lastclose_ratio'] = df['open'].pct_change()
    df['high_close_ratio'] = (df['high'] - df['close']) / df['close']
    df['low_close_ratio'] = (df['low'] - df['close']) / df['close']
    df['close_lastclose_ratio'] = df['close'].pct_change()
    df['volume_lastvolume_ratio'] = df['volume'].pct_change()

    # 추가 특성
    if 'inst' in df.columns and 'frgn' in df.columns:
        for window in windows:
            df[f'inst_ma{window}'] = df['inst'].rolling(window).mean()
            df[f'frgn_ma{window}'] = df['frgn'].rolling(window).mean()
            df[f'inst_ma{window}_ratio'] = (df['inst'] - df[f'inst_ma{window}']) / df[f'inst_ma{window}']
            df[f'frgn_ma{window}_ratio'] = (df['frgn'] - df[f'frgn_ma{window}']) / df[f'frgn_ma{window}']
        
        df['inst_lastinst_ratio'] = df['inst'].pct_change()
        df['frgn_lastfrgn_ratio'] = df['frgn'].pct_change()

    return df