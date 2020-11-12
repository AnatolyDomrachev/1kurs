def beru(slovar, tovar):
    if(slovar['count'] < tovar['count']):
    	count = slovar['count'] 
    else:
    	count = tovar['count']

    tovar['count'] -= count

    return {'name':tovar['name'], 'count':count}


