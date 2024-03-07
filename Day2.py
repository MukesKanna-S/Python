#Multiple Assignment
var1 = var2 = var3 = 10
print(var1) #10
print(var2) #10
print(var3) #10

var1, var2, var3 = 10, 20, 30
print(var1) #10
print(var2) #20
print(var3) #30

#String Methods 
#Syntax --> var_name.fn_name() Eg : name1.upper()
name1 = "mukes Kanna"
name2 = "12345"
print(len(name1)) #11
print(len(name2)) #5
print(name1.capitalize()) #Mukes Kanna
print(name2.capitalize()) #12345
print(name1.upper()) #MUKES KANNA
print(name1.lower()) #mukes kanna
print(name1.find("s")) #4 
print(name1.count("a")) #2
print(name1.isdigit()) #False 
print(name1.isalpha()) #False
print(name1.isalnum()) #False 
print(name1.isupper()) #False 
print(name1.islower()) #False 
print(name2.isdigit()) #True
print(name2.isalpha()) #False 
print(name2.isalnum()) #True
print(name2.isupper()) #False 
print(name2.islower()) #False 
print(name1.replace("a" , "i")) #mukes Kinni
print(name1.replace("a" , "i",)) #mukes Kinna Here 1 represents the attribute
'''(__old: LiteralString, __new: LiteralString, __count: SupportsIndex = -1, /) -> LiteralString
Return a copy with all occurrences of substring old replaced by new.

  count
    Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.''' 
print(name2.replace("1" , "0")) #02345
print(name1*3) #mukes Kannamukes Kannamukes Kanna
print(name2*5) #1234512345123451234512345
#Type casting --> Convert one data type into another data type
x = 10
y = 123.45
z = "25"

print(int(x)) #10
print(int(y)) #123
print(int(z)) #25

print(float(x)) #10.0
print(float(y)) #123.45
print(float(z)) #25.0

print(str(x)) #10
print(str(y)) #123.45
print(str(z)) #25

print(z*3) #252525 Because z is a str since enclosed in quotationsS
print(int(z)*3) #75



