>>> v1 = {'name':a1[0], 'count':a1[1]}
>>>
>>>
>>> v1
{'name': 'Молоко', 'count': '3'}
>>> a2.append(v1)
>>>
>>> a2
[{'name': 'Молоко', 'count': '3'}]
>>>
>>> s = f.readline()
>>> s2 = s.replace('\n' , '')
>>> a1 = s2.split(':')
>>> v1 = {name:a1[0], count:a[1]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> v1 = {name:a1[0], count:a1[1]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> v1 = {'name':a1[0], 'count':a1[1]}
>>>
>>> a2.append(v1)
>>>
>>>
>>>
>>> a2
[{'name': 'Молоко', 'count': '3'}, {'name': 'Хлеб', 'count': '2'}]
>>>
>>>
>>>
>>> a2[0]
{'name': 'Молоко', 'count': '3'}
>>> a2[1]
{'name': 'Хлеб', 'count': '2'}

