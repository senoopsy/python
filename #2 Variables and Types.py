Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 5
7
>>> x = 2
>>> x + 6
8
>>> y = 4
>>> x + y
6
>>> x = 6
>>> x + y
10
>>> _ + y
14
>>> abc
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> name = 'senoopsy'
>>> name
'senoopsy'
>>> name + 'tech'
'senoopsytech'
>>> name + ' tech'
'senoopsy tech'
>>> name 'tech'
SyntaxError: invalid syntax
>>> name[0]
's'
>>> name[9]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name[9]
IndexError: string index out of range
>>> name[-1]
'y'
>>> name[-4]
'o'
>>> name[0:3]
'sen'
>>> name[4:]
'opsy'
>>> name[0:]
'senoopsy'
>>> name[3:]
'oopsy'
>>> name[0:1]
's'
>>> name[:4]
'seno'
>>> name[:3]
'sen'
>>> name[3:10]
'oopsy'
>>> name[0:3] + 'oopsy'
'senoopsy'
>>> myname = 'senoopsy'
>>> len(myname)
8
>>> name[-1:-4]
''
>>> name = 'senoopsy'
>>> name[-1:]
'y'
>>> name[-1:-4]
''
>>> name[:-4]
'seno'
>>> 
