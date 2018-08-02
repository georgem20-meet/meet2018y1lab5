Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: /home/student/georgem20_lab5/meet2018y1lab5/Lab5.py ========
>>> 'by' in a
True
>>> [1,2,5] in c
False
>>> 'self' in b
True
>>> 'sh' in c
False
>>> a[2] == a[6]
True
>>> a[3] == b[8:13]
False
>>> dog = 'dalmatian'
len(dog)
dogs = [dog,'poodle','boxer'] len(dogs)
SyntaxError: multiple statements found while compiling a single statement
>>> dog = 'dalmatian'
>>> len(dog)
9
>>> dogs = [dog, 'poodle', 'boxer']
>>> len(dogs)
3
>>> one = [1,2,3,4]
>>> two = [7,6,5,4]
>>> three = ["y1","friends", "fun"]
>>> print (one + two)
[1, 2, 3, 4, 7, 6, 5, 4]
>>> print
<built-in function print>
>>> print(one[3])
4
>>> one.remove(4)
>>> print(one)
[1, 2, 3]
>>> one.append(4)
>>> print(one)
[1, 2, 3, 4]
>>> one.pop(1)
2
>>> print(one)
[1, 3, 4]
>>> four = one + three
>>> print (four)
[1, 3, 4, 'y1', 'friends', 'fun']
>>> 'fun' in three
True
>>> three.pop(2)
'fun'
>>> three.remove('fun')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    three.remove('fun')
ValueError: list.remove(x): x not in list
>>> 'fun' in three
False
>>> one[3] = two[0]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    one[3] = two[0]
IndexError: list assignment index out of range
>>> one[3] == two [0]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    one[3] == two [0]
IndexError: list index out of range
>>> one.sort 90
SyntaxError: invalid syntax
>>> print9one0
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print9one0
NameError: name 'print9one0' is not defined
>>> one.sort()
>>> print(one)
[1, 3, 4]
>>> two.sort()
>>> print (one)
[1, 3, 4]
>>> print(two)
[4, 5, 6, 7]
>>> three.sort()
>>> print(three)
['friends', 'y1']
>>> one[3]==two[0]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    one[3]==two[0]
IndexError: list index out of range
>>> five = two + three
>>> print(five)
[4, 5, 6, 7, 'friends', 'y1']
>>> 
