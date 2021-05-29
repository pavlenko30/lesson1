prices = [42.17, 84.9, 116.15, 32.11, 52, 4.50, 18.3, 145.74, 97.50, 62.13, 25.2]
for exact_price in prices:
    rub = int(exact_price)
    kop = (exact_price - rub) * 100
    #print(f'{rub} рублей {kop:02.0f} копеек')

prices = [42.17, 84.9, 116.15, 32.11, 52, 4.50, 18.3, 145.74, 97.50, 62.13, 25.2]
print(id(prices))
prices.sort()
print(id(prices))
for exact_price in prices:
    rub = int(exact_price)
    kop = (exact_price - rub) * 100
    #print(f'{rub} рублей {kop:02.0f} копеек')

prices = [42.17, 84.9, 116.15, 32.11, 52, 4.50, 18.3, 145.74, 97.50, 62.13, 25.2]
for exact_price in sorted(prices)[::-1][:5]:
    rub = int(exact_price)
    kop = (exact_price - rub) * 100
    print(f'{rub} рублей {kop:02.0f} копеек')
