

spisok = ['Молоко','Сметана','Соль']
polki = ['Молоко','Хлеб','Соль']
korzina = []

def pokupka():
    for stroka in spisok: #Для каждого товара из списка
        korz_do_ob = len(korzina)

        for tovar in polki: #Просматриваем все полки
            if stroka == tovar:
                korzina.append(tovar)

        korz_posle_ob = len(korzina)

        if(korz_do_ob == korz_posle_ob):
            print("В магазине нет ", stroka)


pokupka()
print("Корзина: ", korzina)

