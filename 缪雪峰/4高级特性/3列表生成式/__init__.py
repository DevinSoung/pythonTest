L=[x*x for x in range(1,11) if x%2==0]
print(L)

L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)

import os
l=[d for d in os.listdir('.')]
print(l)

