Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = (13,14,15,16,17)
>>> tup
(13, 14, 15, 16, 17)
>>> tup[4]
17
>>> tup.append(12)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup.append(12)
AttributeError: 'tuple' object has no attribute 'append'
>>> tup[0] = 12
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup[0] = 12
TypeError: 'tuple' object does not support item assignment
>>> s = {13,14,15,16,17}
>>> s
{13, 14, 15, 16, 17}
>>> s[4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[4]
TypeError: 'set' object is not subscriptable
>>> s.appent(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.appent(1)
AttributeError: 'set' object has no attribute 'appent'
>>> 
