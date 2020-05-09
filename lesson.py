# 1
from collections import namedtuple

Stud = namedtuple('Student', 'name age group')
student = Stud('Abai', 21, 'M-33')
print(student.name, student.age, student.group)
student2 = Stud('Berik', 19, 'L-34')
print('Methods = ',  student.__class__, student.__add__(student2), student.__contains__(33),
      student.__delattr__, student.__dir__, student.__eq__, student.__len__,student.__getattribute__,student.count,
      student.__sizeof__, student.index(21), student._replace(name='Arai'))
student.__class__

kortezh = ('a', 'b', 'c', 'd',)
kortezh2 =('e', 'f',)
print(kortezh)
print('Methods = ',  kortezh.__class__, kortezh.__add__(kortezh2), kortezh.__contains__('d'),
      kortezh.__delattr__, kortezh.__dir__, kortezh.__eq__, kortezh.__len__, kortezh.__getattribute__, kortezh.count,
      kortezh.__sizeof__, kortezh.index('d'))

spisok = ["rock", 7, '12']
print(spisok)
spisok2 = ["yes", "no"]
print('Methods = ',  spisok.__class__, spisok.__add__(spisok2), spisok.__contains__("12"),
      spisok.__delattr__, spisok.__dir__, spisok.__eq__, spisok.__len__, spisok.__getattribute__, spisok.count,
      spisok.__sizeof__, spisok.index('12'))
print(dir(student))


# 2
A = {"chicken", "tiger", 1, 4, 8}
B = {"chicken", 6, 4, 3, 12}
print(type(A))
print(type(B))
print(B.union(A))
print(A.intersection(B))
print(A.difference(B))
# set изменяемый, frozenset неизменяемый(т.е. нель добавить)

# 3
dictionary = dict([(1,'name'), (2, 'surname'), (3, 'age')])
print(dictionary)
dictionary2 = {3:'green', 4:'yellow'}
print(dictionary2)
print(dir(dictionary))
print('Methods = ',  dictionary.__class__, dictionary.__contains__(3), dictionary.__delattr__, dictionary.__dir__,
      dictionary.__eq__, dictionary.__len__,dictionary.__getattribute__,
      dictionary.__sizeof__, dictionary.fromkeys('1'), dictionary.keys, dictionary.items,
      dictionary.values)