str='hello world'

print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+" TESE")

list=['abc',786,2.23,'json',7.32]
tinylist=[123,'json']


print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list+tinylist)

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print(tuple) # 输出完整元组
print(tuple[0]) # 输出元组的第一个元素
print(tuple[1:3]) # 输出第二个至第三个的元素
print(tuple[2:]) # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2) # 输出元组两次
print(tuple + tinytuple) # 打印组合的元组


dict={}

dict['one']='this is one'
dict[2]='this is two'

tinydict={'name': 'john','code':6734, 'dept': 'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())