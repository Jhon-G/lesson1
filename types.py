'''
Практика
'''
#Float
a = 2
b = 0.5
print(a + b)
#string
name = 'Иван'
print(f'Привет, {name}!')
#Приктика числа
v = int(input('Введите число от 1 до 10: ')) #Ввод целого числа
print(v + 10)
#Строки
name =  input('Введите имя: ')
name = name.capitalize() #Делаем первую букву большой
print(f'Привет, {name}! Как дела?')
#Приведение типов
print(float('1'))
print(int(2.5)) #При написании "2.5" выдаст ошибку
print(bool(1))
print(bool(''))
print(bool(0))