# comments - 注释:在内容前面打 # 表示单行注释
# This is the simple comment

""" multiline comment 多行注释:用两组3个双引号括起来的部分,整个括起来的部分全部都是注释
multiline comment takes multiple lines.
"""

# data types:数据类型介绍
"""
number:数字型
1. integer:整数,如1,2,3,-1,-2,-3
2. float:浮点型,如-3.5,2.25,-1,0.0
3. complex example:数式,如:1+j,2+4j

string: 文字型,一句话或一个单独的单词,如:'python','I love teaching'

booleans:判断
1. true-正确
2. false-错误

list:有序数组
数组里面可以是number,也可以是string.用中括号括起来.
1. list of number - [0,1,2,3,4,5]
2. list of string - ['banana','mango']

dictionary:键值对
key:value 的数组组合.
如: {'name':'Zhihao','country':'China','age':25,'is_married:true'}

tuple:初始数组
初始数组与list类似,但创建后不能修改,用小括号括起来.
如: (0,1,2,3,4,5)

set:无序数组
无序数组与list类似,但是set里面的数据本身没有先后关系,用大括号括起来.
如:{0,1,2,3,4,5}

"""

# 检查数据类型的函数:type()
"""
在type()函数中,系统会检测type()函数括号中的数据所属的数据类型

例如:
type(10)
type(1+3j)
type('10')
type(3.14)
type({2,3,4,5})
type([1,2,3])
type({'name':'Xuzhihao'})
type((1,2,3,4))

需要在.py文件中输出结果,需要额外嵌套print()函数.
"""
# python file- day1:helloworld.py