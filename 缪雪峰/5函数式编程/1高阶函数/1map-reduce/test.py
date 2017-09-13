def normalize(name):
  return name[0].upper()+name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)





from functools import reduce


def prod(L):
    return reduce(lambda x,y:x*y,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2float(s):
   return reduce(fn,map(char2num,s.split('.')[0]))+reduce(fn,map(char2num,s.split('.')[1]))/10**len(s.split('.')[1])




print('str2float(\'123.456\') =', str2float('123.456'))