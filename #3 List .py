Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [12,13,14,15,16]
>>> nums
[12, 13, 14, 15, 16]
>>> nums[:1]
[12]
>>> nums[0]
12
>>> nums[4]
16
>>> nums[-1]
16
>>> nums[-5]
12
>>> nums[2:]
[14, 15, 16]
>>> nums[-1:-3]
[]
>>> nums
[12, 13, 14, 15, 16]
>>> names = ['marques','ijustine','isaac']
>>> names
['marques', 'ijustine', 'isaac']
>>> values = [v2.0,'marques',25]
SyntaxError: invalid syntax
>>> values =[2.0,'marques',25]
>>> values
[2.0, 'marques', 25]
>>> mil = [names,nums]
>>> mil
[['marques', 'ijustine', 'isaac'], [12, 13, 14, 15, 16]]
>>> nums.append(17)
>>> nums
[12, 13, 14, 15, 16, 17]
>>> nums.insert(0,11)
>>> nums
[11, 12, 13, 14, 15, 16, 17]
>>> nums.pop(11)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    nums.pop(11)
IndexError: pop index out of range
>>> nums.remove(11)
>>> nums
[12, 13, 14, 15, 16, 17]
>>> nums.pop(5)
17
>>> nums
[12, 13, 14, 15, 16]
>>> del nums.[2:4]
SyntaxError: invalid syntax
>>> del nums[2:4]
>>> nums
[12, 13, 16]
>>> nums.extended[14,15]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    nums.extended[14,15]
AttributeError: 'list' object has no attribute 'extended'
>>> nums.extend[14,15]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    nums.extend[14,15]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.extend([14,15])
>>> nums
[12, 13, 16, 14, 15]
>>> nums.sort()
>>> nums
[12, 13, 14, 15, 16]
>>> 
