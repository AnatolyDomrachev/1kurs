
def read_file(arr, infile):

    conf_dir = 'conf/'
    stroka = ''
    f = open(conf_dir + infile)
    stroka = f.readline()

    while(stroka):
        arr.append(stroka.replace('\n' , ''))
        stroka = f.readline()
 
