#swap = [['В гору','C горы'],['Налево','Направо']]

swap = {'В гору':'C горы','Налево':'Направо'}

def reverse(path):

    path.reverse()
    back_path = path.copy()

    for i in range(len(back_path)):
       # for word in swap:
            if swap.get(back_path[i]):
                back_path[i] = swap.get(back_path[i])



    return back_path 
