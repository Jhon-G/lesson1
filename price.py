def format_price(price):
    price = abs(int(price))
    return f'Цена: {price} руб.'

print(format_price(56.24))