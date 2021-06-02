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

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print('This is a program for you to calculate the perimeter of triangle.')
side_a = float(input('Please enter the 1st side of the triangle:'))
side_b = float(input('Please enter the 2nd side of the triangle:'))
side_c = float(input('Please enter the 3rd side of the triangle:'))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is',perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print('This is a program for you to calculate the area of rectangle.')
length = float(input('Please enter the length of rectangle:'))
width = float(input('Please enter the width of rectangle:'))
area = length*width
print('The area of the rectangle is',area)


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print('This is a program for you to calculate the area and circumference of a circle.')
import math
radius = float(input('Please enter the radius of this circle:'))
area = math.pi*radius**2
circumference = 2*math.pi*radius
print('The area of the circle is:','%.2f' % area)
print('The circumference of the circle is:','%.2f' % circumference)
'''

# Calculate the slope, x-intercept and y-intercept of y = 2x -2 计算y=2x-2的斜率，x轴截距和y轴截距
x = [0,1,2,3,4,5]
y = [2*num-2 for num in x] # 数组的函数运算，表示y=2x-2的函数值在x=[0,1,2,3,4,5]中的值。
slope = (y[2]-y[1])/(x[2]-x[1])
x0 = 0
y_intercept = 2*x0-2
y0 = 0
x_intercept = (y0+2)/2
print({'slope':slope,'y-intercept':y_intercept,'x-intercept':x_intercept})

# Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)

# Compare the slopes in tasks 8 and 9.

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
# Find the length of 'python' and 'jargon' and make a falsy comparison statement.

# Use and operator to check if 'on' is found in both 'python' and 'jargon'

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

# There is no 'on' in both dragon and python

# Find the length of the text python and convert the value to float and convert it to string

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

# The floor division of 7 by 3 is equal to the int converted value of 2.7.

# Check if type of '10' is equal to 10

# Check if int('9.8') is equal to 10

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
'''
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
'''

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume someone lives up to hundred years.
'''
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
'''

# Write a python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
