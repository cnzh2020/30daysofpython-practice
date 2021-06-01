# day3 exercise
'''
# Declare your age as integer variable
age = int(25)
print(age)
# Declare your height as a float variable
height = float(1.83)
print(height)
# Declare a complex number variable
complex_num = 1+2j
print(complex_num)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
Print('This is a program for you the calculate the area of triangle')
base = float(input('Please enter the base:')) # input输出的数据格式是str,需要强制转换成float
height = float(input('Please enter the height:'))
area = 0.5*base*height
print('The area of the triangle is',area)
'''
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print('This is a program for you to calculate the perimeter of triangle')
side_a = float(input('Please input the 1st side of the triangle:'))
side_b = float(input('Please input the 2nd side of the triangle:'))
side_c = float(input('Please input the 3rd side of the triangle:'))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is',perimeter)

# 
