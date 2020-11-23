#Задание списки
my_list = [3, 5, 7, 9, 10.5]
print(my_list)
#Добавляем пайтон в список. Выводим длинну списка
my_list.append('Python')
print(len(my_list))
#Выводим начальный и послоедний элемент списка
print(my_list[0])
print(my_list[5])
#Делаем срез списка со 2 по 4 эелемент включительно 
print(my_list[2:5])
#Удаляем из списка строчку "Python" del my_list[5] или 
# my_list.remove('Python')
my_list.remove('Python')
print(my_list)

#Задание словари
ct = {'city': 'Москва',
'temperature': 20,
}

#Выводим на экран значение ключа city
print(ct['city'])

#Уменьшаем значение temperature
ct['temperature'] -= 5
print(ct)

#Проверяем есть ли в словаре ключ country
print(ct.get('country'))

#Добавляем значение по умолчанию для ключа get
print(ct.get('country', 'Россия'))

#Добавляем в словарь ключь date  датой 
ct['date'] = '22.11.2020'
print(len(ct))