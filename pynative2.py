#Append new string in the middle of a given string

n1 = 'Rama'
n2 = 'Films'
len=int(len(n1)/2)
first = (n1[0::len+1])
last = (n1[len::1])
print(first+n2+last)