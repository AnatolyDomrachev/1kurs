class Roditel:

	__spisok = []

	def __init__(self, infile):
            read_file(self.__spisok, infile)

	def read_file(self, spisok, infile):
		conf_dir = 'conf/'
		stroka = ''
		f = open(conf_dir + infile)
		stroka = f.readline()

		while(stroka):
			#        spisok.append(stroka.replace('\n' , ''))

			stroka2 = stroka.replace('\n' , '')
			a1 = stroka2.split(':')
			count = int(a1[1])
			v1 = {'name':a1[0], 'count':count}
			self.spisok.append(v1)

			stroka = f.readline()

	def print_spisok(self):
            print(self.__spisok)

