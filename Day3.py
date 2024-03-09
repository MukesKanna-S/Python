'''User Input :
   Syntax --> input(___) "User input always act as a string
   We can also use typecasting in getting user inputs 
   Eg : *int(input(___))
        *float(input(___)) '''

name = input("Enter your name :")
print("Hello " + name ) #Hello Mukes
'''
We can also use f string in printing user inputs.
f strings are a literal string prefixed with 'f', which contains expressions inside braces.'''

print(f"Hello {name}") #Hello Mukes
age = int(input("Enter your age : "))
print(f"You are {age} years old") #You are 19 years old 


#MADLIBS GAME :

name1 = input("Enter the name of a beach : ")
adj1 = input("Enter an adjective : ")
adj2 = input("Enter an adjective : ")
char = input("With whom have you hanged out ?")
food = input("Select Breakfast/Lunch/Dinner : ")
adj3 = input("Enter an adjective : ")
print(f"Last Sunday, I went to {name1} beach.")
print(f"I saw such a {adj1} scenery.")
print(f"So I took some {adj2} pictures with my {char}.")
print(f"Then we had a {food} together and returned home safely.")
print(f"Overall it was such an {adj3} experience.")
'''O/P : Last Sunday, I went to Marina beach.
I saw such a beautiful scenery.
So I took some goodlooking pictures with my friends.
Then we had a lunch together and returned home safely.
Overall it was such an amazing experience.'''

#AREA CALCULATION :
l = float(input("Enter length : "))
b = float(input("Enter breadth :"))
area = l*b
print(f"Area is {area} cm^2")

 
#VOLUME CALCULATION :
l = float(input("Enter length : "))
b = float(input("Enter breadth : "))
h = float(input("Enter height : "))
v = l*b*h
print(f"Volume is {v} cm^3") 

#SHOPPING CART :
item = input("Select an item : ")
price = float(input("Enter price : "))
quant = int(input("Enter quantity : "))
tot = price*quant
print(f"You purchased {quant} x {item}.")
print(f"Your total is ${round(tot,2)}")
'''O/P:
Select an item : Pizza
Enter price : 4.99
Enter quantity : 7
You purchased 7 x Pizza.
Your total is $34.93'''