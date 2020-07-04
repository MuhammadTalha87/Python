
#String code is below
lang = "Hello" 
print(lang[0:4])  #this will show only hell
print(lang[0])    #this will show only H
print(lang[:])          #this will show whole string
print(lang[:4])         #this will assume starting index from 0 and will print all characters till hell
print(lang[1:-1])       #this will show all characters from second index to the second last index.
second_str = lang[:]    #this will copy whole string in second_str variable
print(second_str)

first_name ="MUHAMMAD"
last_name = "talha"
age = 24

print(first_name.title())  #this will print only first character of name as capital
print(first_name.find("A")) #this will print only index of character A
print(first_name.replace("MUHAMMAD", "Talha")) #this will replace MUHAMMAD with Talha
print("HAMMAD" in first_name)   #this will produce a boolean value which will show if these characters exist or not in first_name

msg = f"{first_name} {last_name} is " +str(age)+ " years old"  #concatenation of a variable type int and Strings
print(msg)


#This is type conversion code
weight_pounds = int(input("Enter your weight in pounds : "))
weight_kgs=weight_pounds*0.45
print(weight_kgs)


