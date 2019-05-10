Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 5
>>> type(num)
<class 'int'>
>>> num = 2.5
>>> type(num)
<class 'float'>
>>> num = 3+9j
>>> type(num)
<class 'complex'>
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> c = float(b)
>>> c
5.0
>>> c = 7
>>> k = complex(b,c)
>>> k
(5+7j)
>>> b < c
True
>>> bl = b < c
>>> type(bl)
<class 'bool'>
>>> bl
True
>>> b > c
False
>>> int(True)
1
>>> int(False)
0
>>> lst = [13,14,15,16,17]
>>> type(lst)
<class 'list'>
>>> t = (12,14,17,18,19)
>>> type(t)
<class 'tuple'>
>>> s = {13,12,15,14,17,15}
>>> s
{12, 13, 14, 15, 17}
>>> type(s)
<class 'set'>
>>> st = "sen"
>>> type(st)
<class 'str'>
>>> st = 'sen'
>>> type(st)
<class 'str'>
>>> s
{12, 13, 14, 15, 17}
>>> st
'sen'
>>> st = "sen"
>>> st
'sen'
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range)
<class 'type'>
>>> p = {'marques':'pixel','isaac':'iphone','shlok':'oneplus'}
>>> p['isaac']
'iphone'
>>> p['shlok']
'oneplus'
>>> p.get('marques')
'pixel'
>>> d.keys()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d.keys()
NameError: name 'd' is not defined
>>> p.keys
<built-in method keys of dict object at 0x10e401c60>
>>> p.keys()
dict_keys(['marques', 'isaac', 'shlok'])
>>> p.values()
dict_values(['pixel', 'iphone', 'oneplus'])
>>> 
