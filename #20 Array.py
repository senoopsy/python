import array as arr

from array import *


vals = array('i',[5,9,-8,4,2])
print(vals.buffer_info())


vals = array('i',[5,9,8,4,2])
print(vals.typecode)


vals = array('i',[5,3,6,7,9])
vals.reverse()
print(vals)


vals = array('i',[2,3,5,7,9])
print(vals[3])


vals = array('i',[2,5,7,1,9])
for i in range(5):
    print(vals[i])


vals = array('i',[1,3,5,7,9])
for i in range(len(vals)):
    print(vals[i])


vals = array('i',[2,4,6,8,10])
for e in vals:
    print(e)


vals = array('u',['s','e','n'])
for e in vals:
    print(e)


vals = array('i',[2,5,6,7,9])
newarr = array(vals.typecode,(a*a for a in vals))

for e in newarr:
    print(e)


    # While loop

i = 0
while i<=len(newarr):
    print(newaarr[i]):
    i += 1
