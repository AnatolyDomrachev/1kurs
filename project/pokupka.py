import magazin
import etc

magazin =  magazin.Magazin('magazin.conf') 

korzina = []
net_v_magazine = []

def pokupka(spisok):
    for slovar in spisok:
        est_v_mag = 'No'
        for tovar in magazin.tovary:
            if slovar['name'] == tovar['name']:
         
                kupil = etc.beru(slovar, tovar)       

                korzina.append(kupil)
                est_v_mag = 'Yes'

        if est_v_mag == 'No':
            print(slovar," нет в магазине")

    print("Купили: ",korzina)
    print()
    print("Осталось: ",magazin.tovary)


