import numpy as np
import csv

products = []
price = []
stock = []
discount = []

# with文の余分な括弧を外し、スペースを調整しました
with open("Stock_1.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        products.append(row["Product"])
        price.append(float(row["Price"]))
        # stock_Bの後の閉じ括弧「)」を追加し、リストの構文エラーを修正しました
        stock.append([float(row["Stock_A"]), float(row["Stock_B"]), float(row["Stock_C"])])
        discount.append(float(row["Discount"]))

products = np.array(products)
price = np.array(price)
stock = np.array(stock)
# doscount のタイプミスを discount に修正しました
discount = np.array(discount)

total_stock = stock.sum(axis=1)
total_value = price * total_stock
discount_price = price * discount

hot = np.argmax(total_stock)
low = np.argmin(total_stock)

with open("Stock_OK.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["product", "stock", "Value", "Discount", "Hot", "Low"])

    for i in range(len(products)):
        w.writerow([
            products[i],
            total_stock[i],
            total_value[i],
            discount_price[i],
            # not はPythonの予約語であるため、変数 hot に修正しました
            i == hot,
            i == low
        # 括弧の閉じる順番「)]」を「])」に修正しました
        ])