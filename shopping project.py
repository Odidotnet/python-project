print()
print("welcome to wired connect! electronic store\n")

items = []
prices = []
total = 0

wallet = 0

while wallet != "" and True:
    print()
    deposit = int(input("Hello client kindly deposit a taken into your wallet to begin shopping €"))
    token = (deposit + wallet)
    print("deposit successful, your token is now €", token, "\n")
    break

while True:
    product = str(input("enter the product of the shopping items.. NB:empty choices will terminate shopping!!"))
    if product == "":
        break
    else:
        price = float(input(f"enter the price € {product}"))
        items.append(product)
        prices.append(price)

for product in items:
    print(product)

choice = str(input("input yes if you are done shopping to calculate the total"))
for price in prices:
    total += price

print(f"dear customer your total is €: {total}")
print("thanks for shopping with us....")

