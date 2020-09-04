import random

f1 = open('is29.list')
strk = '1'
while(strk):
	print()
	strk = f1.readline()
	tmp = strk.split('\n')
	print(tmp[0])

	f2 = open('z4')
	strk2 = '1'

	while(strk2):
		strk2 = f2.readline()
		tmp = strk2.split('\n')
		tmp2 = tmp[0]
		arr = tmp2.split(' ')
		
		if(arr[0]):
			for i in range(int(arr[2])):
				print(arr[0], random.randint(1,int(arr[1])))

	
