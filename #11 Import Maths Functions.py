Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>             # import math functions
            
>>> import math
>>> x = math.sqrt(9)
>>> x
3.0
>>> x = math.sqrt(676)
>>> x
26.0
>>> print(math.floor(2.9))
2
>>> print(math.ceil(4.5))
5
>>> 4**3
64
>>> print(pow(4,3))
64
>>> print(math.(pi))
SyntaxError: invalid syntax
>>> print(math.'pi')
SyntaxError: invalid syntax
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> import maths as m
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import maths as m
ModuleNotFoundError: No module named 'maths'
>>> math as m
SyntaxError: invalid syntax
>>> import math as m
>>> m.sqrt(36)
6.0
>>> print(m.sqrt(49))
7.0
>>> 
>>>             # if you want only some functions from math then
            
>>> from math import sqrt,pow
>>> pow(27)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    pow(27)
TypeError: pow() takes exactly 2 arguments (1 given)
>>> m.pow(27)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    m.pow(27)
TypeError: pow() takes exactly 2 arguments (1 given)
>>> math.pow(29)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    math.pow(29)
TypeError: pow() takes exactly 2 arguments (1 given)
>>> pow(29,2)
841.0
>>> 
