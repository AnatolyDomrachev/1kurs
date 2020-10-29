def beru(slovar, tovar):
    if(slovar['count'] < tovar['count']):
    	count = slovar['count'] 
    else:
    	count = tovar['count']

    tovar['count'] -= count

    return {'name':tovar['name'], 'count':count}

def read_file(arr, infile):

    conf_dir = 'conf/'
    stroka = ''
    f = open(conf_dir + infile)
    stroka = f.readline()

    while(stroka):
#        arr.append(stroka.replace('\n' , ''))

        stroka2 = stroka.replace('\n' , '')
        a1 = stroka2.split(':')
        count = int(a1[1])
        v1 = {'name':a1[0], 'count':count}
        arr.append(v1)

        stroka = f.readline()

