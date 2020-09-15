spisok = ['Молоко','Сметана','Соль']
polki = ['Молоко','Хлеб','Сметана','Соль']
korzina = []

def pokupka():
    for stroka in spisok: #Для каждого товара из списка
        for tovar in polki: #Просматриваем все полки
            if stroka == tovar:
                korzina.append(tovar)


pokupka()
print("Корзина: ", korzina)

