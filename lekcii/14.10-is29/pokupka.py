magazin  = ['Молоко','Хлеб','Соль','Курица','Колбаса']
korzina = []
net_v_magazine = []

def pokupka(spisok):
    for stroka in spisok:
        est_v_mag = 'No'
        for tovar in magazin:
            if stroka == tovar:
                korzina.append(tovar)
                est_v_mag = 'Yes'

        if est_v_mag == 'No':
            print(stroka," нет в магазине")

    print("Купили: ",korzina)


