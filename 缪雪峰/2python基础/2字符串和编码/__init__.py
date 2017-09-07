print('包含中文的str')
print(ord('A'))
print('\u4e2d\u6587')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))


print('%2d-%02d' %(3,1))

print('%.2f' %(3.1415926))

print('growth rate: %d %%' % 7)