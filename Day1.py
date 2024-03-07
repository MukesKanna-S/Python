'''Variable = acts as a container used for storing some values
 Syntax :
    var_name = value (to be stored)'''
#var1  = Mukes
#print(var1) #Error --> String should be enclosed in single or double quotes

var1 = "Mukes"
print(var1) # Mukes

var2 = 10 #Quotaions must not be used for int and float data types
var3 = 123.4567

print(var2) #10
print(var3) #123.4567

#If var2 and var3 are enclosed in quotions, then they act as string data type

# type() --> Function used for determining the data type of the variable

print(type(var1)) # <class 'str'>
print(type(var2)) # <class 'int'>
print(type(var3)) # <class 'float'>

var4 = "10"
var5 = '123.4567'
print(type(var4)) # <class 'str'>
print(type(var5)) # <class 'str'>

name1 = "Mukes"
name2 = "Kanna"
name = name1 + name2
print("name") #name (normal string)
print(name) #MukesKanna (a var is used. so no shouldn't use quotations)

name = name1 + " " + name2 # " " --> Used for creating blank spaces
print(name) #Mukes Kanna
print("Hello" + name1) #HelloMukes
print("Hello " + name1) #Hello Mukes
age = 19
#print ("My age is " + age) Error --> Cannot concatenate str with integer
#str(age) --> Used to convert int or float data type into string
print ("My age is " + str(age))

#Boolean Data type --> True or False
bool1 = True #No quotations should be used for Bool data type
bool2 = False
print(bool1) #True
print(bool2) #False
print(type(bool1)) #<class 'bool'>
print(type(bool2)) #<class 'bool'>

#If: bool1 = "True then, print(type(bool1)) --> <class 'str'>

