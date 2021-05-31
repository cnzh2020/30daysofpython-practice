# built-in functions <https://docs.python.org/2/library/functions.html>

# 常用函数说明

'''
print() 输出print函数中内部数据的计算结果
len() 计算len函数中内部数据的字符长度
type() 检查type函数内部数据的数据格式
str() 将str函数内的数字转换为文字
int() 将int函数内的文字转化为整数
float() 将float函数内的数字转化为浮点型
input() 以文字型输出用户输入的内容

help('keywords') 向用户展示所有关键字函数的使用方法
help() 在help函数中输入关键字,将展示关键字对应函数的使用说明

'''

# variable declaration 变量赋值

'''
python的变量赋值必须有以下要求:
1. 起始字符只能是字母或者下划线 '_'
2. 起始字符不能是数字
3. 内含的字符只能是字母/数字/下划线(A-z,0-9,_)
4. 变量区分大小写;firstname,Firstname,firstName,FIRSTNAME均是不同的变量

变量通过 等号'=' 进行赋值
'''
# variables in python 

from typing import AsyncGenerator


first_name = 'Xu' # 将Xu这个值赋予给变量 first_name
last_name = 'zhihao'
country = 'China'
city = 'Hangzhou'
age = 1000000000000
is_married = True
skills = ['accounting','product_design','project_management'] # list 有序数组, ()是不可修改数组 {}是无序数组
person_info = {
    'firstname':'Xu',
    'lastname':'zhihao',
    'country':'China',
    "city":'Hangzhou'
}

'''
print函数

print函数可以输出单一值,也可以针对多个值合并输出.当输出多个值时,中间会用空格隔开.
print函数内部也可以嵌套其他函数.
'''
print('hello,world.')
print('Hello',',','world')
print(len('hello,world.'))

'''
赋值成功后,通过print函数即可直接输出变量当前的值.
'''

print(first_name)
print(last_name)

# 变量也可以在一行内直接输出

print(first_name,last_name,country,age,is_married)

# 通过input()函数,可以直接向变量赋值.

first_name = input('What is your name?')
age = input('How old are you?')

print(first_name)
print(age)

# data type 数据格式

# 数据格式检查 type() 通过type函数检查type函数内部数据的格式

first_name = 'Xu'
last_name = 'zhihao'
country = 'China'
city = 'Hangzhou'
age = 10000000000

# 输出数据格式

print(type(first_name))
print(type(True))

# 数据格式硬转

'''
int() 强制转换为整数型
float() 强制转换为浮点型
str() 强制转换为字符型
list() 强制转换为list型
'''

# int to float 整数转换为浮点型
num_int = 10
print('num_int:',num_int) # 10
num_float = float(num_int)
print('num_float:',num_float) # 10.0

# float to int 浮点型转换为整数

# int to str 整数转换为字符型

# str to int 字符型转换为整数

# str to list 字符型转换为有序列表

# Numbers type 数字类型
'''
1. int_integer: 整数型 例: -3,-2,-1,0,1,2,3
2. float_floating Point numbers : 浮点型 例: -3.5,-3.25,-1.0,0.0,0.1
3. complex_numbers: 复杂数,带参数的式子 例:1+j,2+4j,1-1j
'''

