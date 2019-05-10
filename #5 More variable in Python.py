Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 5
>>> id(num)
4564704560
>>> name = 'sen'
>>> id(name)
4619913736
>>> a = 7
>>> b = a
>>> id(a)
4564704624
>>> id(b)
4564704624
>>> id(7)
4564704624
>>> c = 7
>>> id(c)
4564704624
>>> a = 5
>>> id(a)
4564704560
>>> id(b)
4564704624
>>> c = a
>>> id(c)
4564704560
>>> b = 4
>>> PI = 3.14
>>> PI
3.14
>>> type(PI)
<class 'float'>
>>> 
