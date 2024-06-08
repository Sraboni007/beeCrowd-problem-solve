product1_code, product1_units, product1_price = input().split()
product2_code, product2_units, product2_price = input().split()
product1_units = int(product1_units)
product1_price = float(product1_price)
product2_units = int(product2_units)
product2_price = float(product2_price)

total = (product1_units * product1_price) + (product2_units * product2_price)

print(f"VALOR A PAGAR: R$ {total:.2f}")