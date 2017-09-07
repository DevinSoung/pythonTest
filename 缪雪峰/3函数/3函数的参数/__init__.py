def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(3,4))

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(3))

def calc(*numbers):
    sum=0
    for n in numbers:
        sum =sum+n*n
    return sum

print(calc(1,2,3))

##关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)


person('Michael', 30,city='Beijing')

##命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)

person('Jack', 24, city='Beijing', job='Engineer')

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f2(1, 2, d=99, ext=None)