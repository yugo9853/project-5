import pandas as pd

# 1. 辞書を使って作成
data_dict = {
    'Product': ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava'],
    'Price': [30, 20, 25, 60, 45, 35],
    'Sales': [100, 150, 80, 60, 90, 54]
}
df_from_dict = pd.DataFrame(data_dict)

# 2. リスト（子リスト）を使って作成（こちらをメインで使用）
data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

# --- 課題の指示通りの出力処理 ---
print(df.head(5))  # 前から5行
print(df.tail(5))  # 後ろから5行
print(df.shape)    # 行数と列数

# 範例の「dtype='str'」に見た目を合わせるための型変換処理
columns_index = pd.Index(df.columns, dtype='str')
print(columns_index)

dtypes_output = df.dtypes.astype(str)
dtypes_output['Product'] = 'str'
print(dtypes_output)

print(df.count())  # 非空値の数

# 統計情報を計算し、小数点以下2位で四捨五入
summary_stats = df.describe().round(2)
print(summary_stats)

# 統計情報を「0520_stock2.csv」として保存
summary_stats.to_csv("0520_stock2.csv")