def get_summ(one, two, delimiter='&'): #Передаем функции 2 аргумента и 1 именованный
    return f'{one}{delimiter}{two}'.capitalize() #Приводдим к строке и делаем 1 букву заглавной 

print(get_summ('learn','python'))

