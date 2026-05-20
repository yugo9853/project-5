import pandas as pd

# 1. リストからstock1を作成（pandasのSeriesに変換）
stock_list = [120, 80, None, 60, 95, None, 110]
stock1 = pd.Series(stock_list)

# 2. インデックスを指定してstock2を作成
index_names = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series(stock_list, index=index_names)

# 3. stock2を辞書型に変換してstock3を作成
stock3 = stock2.to_dict()

# --- 4. 指定された通りの形式で出力する処理 ---

print("stock1")
print(stock1)
print()  # 改行を入れる

print("stock2")
print(stock2)
print()

print("stock3")
print(stock3)
print()

# Bananaの庫存値を出力
print(f"Banana 庫存： {stock2['Banana']}")
print()

# 缺失値（欠損値）のチェック
print("缺失值檢查：")
print(stock2.isna())
print()

# 缺失値の合計数を計算して出力
print(f"缺失值數量： {stock2.isna().sum()}")

# 5. stock2を「0520_stock.csv」として保存
# header=Falseにすることで出力範例と同じ純粋なデータのみを保存します
stock2.to_csv("0520_stock.csv", header=False)