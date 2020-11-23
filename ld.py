'''
phones = ['iPhone Xs', 'Samsung 10s','Xiaomi Mi8']

print(phones)

phones_count = len(phones)
print(phones_count)

phones.append('iPhone 6')
print(phones)

print(phones.count('iPhone Xs'))

print(phones.count('iPhone 9'))

print(phones[1:3])

print(phones[:2])

print(phones[-1])

print(phones.index('Samsung 10s'))

phones.sort()

print(phones)

print('iPhone xs' in phones)
'''

stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 
     'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
]

stock[0]['price'] += 10000 #Прибавляем к изначальному значению 10000

print(stock[0]['recomended'][1])

print(type(stock))

print(type(stock[0]))