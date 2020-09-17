swap = [['В гору','C горы'],['Налево','Направо']]

def reverse(path):

    path.reverse()
    back_path = path.copy()

    for i in range(len(back_path)):
        for word in swap:
            if(back_path[i] == word[0]):
                back_path[i] = word[1]



    return back_path 
