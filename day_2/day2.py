# Day2: 30 Days of python programming

first_name = 'Xu'
last_name = 'Zhihao'
full_name = 'Xu Zhihao'
country = 'China'
city = 'HangZhou'
age = 26
year = '1995'
is_married = True 
is_true = True
# first_name,last_name,full_name = 'Xu','Zhihao','Xu Zhihao'
print(first_name)
print(last_name)
print(full_name)

# check data type
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))

# check length of name
print(len(first_name))

# compare the length of your first_name and your last_name
print(max(len(first_name),len(last_name)))

# 运算
num_one = 5
num_two = 4
variable_total = num_one+num_two
variable_diff = num_one-num_two
variable_product = num_one*num_two
variable_division = num_one/num_two
variable_remainder = num_one%num_two
variable_exp = num_one**num_two
variable_floor_division = num_one//num_two

print(variable_total)
print(variable_diff)
print(variable_product)
print(variable_division)
print(variable_remainder)
print(variable_exp)
print(variable_floor_division)

# 计算圆面积

The radius of a circle is 30 meters 一个圆的半径是30米
1. Calculate the area of a circle and assign the value to a variable area_of_circle. 计算圆面积
2. Calculate the circumference of a circle and assign the value to a variable circum_of_circle 计算周长

import math # 调用数学数据包,教学链接 https://blog.csdn.net/weixin_38256474/article/details/81228492
radius_of_circle = 30
area_of_circle = radius_of_circle*math.pi**2
circum_of_circle = 2*math.pi*radius_of_circle

print(area_of_circle)
print(circum_of_circle)

radius_of_circle = float(input("请输入圆半径:"))
area_of_circle = radius_of_circle*math.pi**2
b = ('%.2f' % area_of_circle) # ('%.nf' % m) 表示取m浮点型数据的小数点后n位
print(area_of_circle)
print(b)

# 保存用户的基础信息

first_name = input("please enter your first name:")
last_name = input("please enter your last name:")
country = input("please enter your country:")
age = input("please enter your age:")
dictionary_of_user = {'first_name': first_name,'last_name': last_name,'country':country,'age':age}
print(dictionary_of_user)

# 使用help('keywords')函数
help('keywords') #在help('keywords')函数下弹出的关键字大全中,输入相应的关键字帮助可以查看函数使用指南
help('def')
