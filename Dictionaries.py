person = {
    "name" : "John Smith",
    "age" : "25",
    "gender": "Male",
"relationship_status" : "Single"
}
print(person["age"])

#To update a name 
person["name"] = "Muhammad talha"

print(person["name"])

#Exercise of converting digits in to text
numbers = input("Enter the numbers to be converted in to text : ")
#if numbers > 10:
# print("please enter the numbers in range between 0 to 10")
#else:
text = {
    "0": "zero",
    "1":  "one",
    "2": "two",
    "3": "three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7":  "Seven",
    "8": "eight",
    "9": "Nine",
    "10": "Ten"
   }

for number in numbers:
  print(text.get(number, "..." ) )

#Emoji Program

mesg = input("")
words = mesg.split(" ")

emoji_converter = {
    ":(": "\U0001F925",
    ":)": "\U0001F917",
    ":-D": "\U0001F61C",
    ":-p": "\U0001F61D"
}

output = ""
for word in words:
    output += emoji_converter.get(word, word) + " "
print(output)



