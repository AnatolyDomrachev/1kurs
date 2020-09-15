

spisok = ['Молоко','Сметана','Соль']
polki = ['Молоко','Хлеб','Сметана','Соль']
korzina = []

def pokupka():
    i = 0
    for stroka in spisok: #Для каждого товара из списка
        for tovar in polki: #Просматриваем все полки
            if stroka == tovar:
                korzina.append(tovar)
                spisok.pop(i)#Вычеркиваем строкó из списка
        i+=1


pokupka()
print("Корзина: ", korzina)
print("Не было: ", spisok)

