#BASIC MATH FUNCTIONS IN PYTHON :

# ==>Arithmatic Operators

x = 10

x += 5 #Add and Assign --> x = x + 5
print(x) #15

x -= 5 #Subtract and Assign --> x = x - 5
print(x) #5 

x *= 5 #Multiply and Assign --> x = x * 5
print(x) #50 

x /= 5 #Divide and Assign --> x = x / 5 __Division(/) operator always returns a float value
print(x) #2.0 

x %= 5 #Perform Modulo operation and Assign --> x = x % 5 __Modulo(%) operator returns the remainder value
print(x) #0 

x **= 5 #Perform exponentiation and Assign --> x = x ** 5
print(x) #100000 

# ==>Built In Math functions

x = 9
y = 9.4
z = -10

print(round(y)) #Rounds off the value
#9 

print(abs(z)) #Return the absolute value of the argument
#10

print(pow(x,2)) #Exponentiation
#81 

print(max(x,y,z)) #return the largest argument
#9.4 

print(min(x,y,z)) #return the smallest argument
#-10 

# ==>Math Module 
# Keyword --> import math (imports math library)
 
import math

print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045 

x = 9
y = 3.3

print(math.sqrt(x)) #returns square root value which is of float data type
#3.0 
print(math.ceil(y)) #returns nearby largest integer value
#4 
print(math.floor(y)) #returns nearby smallest integer value
#3 

#Exercises :

# Circumference of a circle = 2*pi*r

r = float(input("Enter radius of a circle : "))
circumference  = 2 * math.pi * r
print(f"Circumference of a circle is {round(circumference,2)} cm")
'''
O/P:
r = 5
Circumference of a circle is 31.42 cm '''

#Area of a circle = pi*r^2
import math
r = float(input("Enter radius of a circle : "))
area = math.pi * pow(r,2)
print(f"Area of a circle is {round(area,2)} cm^2")
'''
O/P:
r = 5
Area of a circle is 78.54 cm^2'''


#Hypotenuse Calculator (c = sqrt(a^2 + b^2))

import math
a = float(input("Enter side 'a' : "))
b = float(input("Enter side 'b' : "))

#Hypotenuse = c
c = math.sqrt(pow(a,2) + pow(b,2)) 
print(f"Hypotenuse of a triangle is {c}")
'''
O/P:
Enter side 'a' : 3
Enter side 'b' : 4
Hypotenuse of a triangle is 5.0 '''




 
