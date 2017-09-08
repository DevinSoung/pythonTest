def f(x):
   return x * x


m=map(f,[1,3,4,5,6])
print(list(m))

from functools import reduce

def add(x,y):
    return x+y

r=reduce(add,[1,3,5,7,9])

print(r)


def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


re=reduce(fn,map(char2num,'13579'))

print(re)



def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
