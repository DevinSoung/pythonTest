def foo(s):
    n=int(s)
    assert n!=0,'n is zero'
    return 10/n

def mian():
    foo('0')




import pdb

s='0'
n=int(s)
pdb.set_trace()
print(10/n)