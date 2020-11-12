class Magazin:

	tovary = []

	def __init__(self, infile):

		conf_dir = 'conf/'
		stroka = ''
		f = open(conf_dir + infile)
		stroka = f.readline()

		while(stroka):
			#        tovary.append(stroka.replace('\n' , ''))

			stroka2 = stroka.replace('\n' , '')
			a1 = stroka2.split(':')
			count = int(a1[1])
			v1 = {'name':a1[0], 'count':count}
			self.tovary.append(v1)

			stroka = f.readline()


#Mag = Magazin('magazin.conf')
#print(Mag.tovary)
