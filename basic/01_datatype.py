# ***********************
# *******Data type*******
# ***********************

'''
Python has Five standard types
Scalar
    Numbers : int, float, complex
    String : str
Vector : List, Tuple, Dictionary, Set

print('hello')

Python List
'''
# List CRUD Example

ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']

# Create: ls 에 '100'을 추가 Create
ls.append(100)
print(ls)

# Read: ls 의 목록을 출력
for i in ls:
    print(i)
# Update: ls와 tinyls 의 결합
#result = ls + tinyls
ls.extend(tinyls)
#ls.append(tinyls)
print(ls)

# Delete: ls 에서 786을 제거
del ls[1]
print(ls)

# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'jhon', 70.2)
tinytp = (123, 'jhon')

# Create : tp에 '100'을 추가 Create
tp += (100, )
print(tp)

# Read : tp의 목록을 출력
for i in tp:
    print(i)

# Update : tp 와 tinytp 의 결합
tp += tinytp
print(tp)

# dictionary CRUD Example
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍': 284, '30세':123}

# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt['tom'] = 100

# Read: dt 의 목록을 출력
for i in dt:
    print(i)

# Update: dt와 tinydt 의 결합
dt.update(tinydt)
print(dt)

# Delete: dt 에서 'abcd' 제거
# del(dt['abcd'])
print(dt.pop('abcd'))
print(dt)

