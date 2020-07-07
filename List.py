cars = ["BMW", "Mercides", " Honda", "toyota", "KIA", "Ford"]

#print(cars[2])  #this will print 3rd index object
cars[5]= ("blue berry") #this will replace the index 5 value however replace function do not replace it permanently

#print(cars)

#2D lists
matrix = [
    ["hello","world","of"],
    ["python","are","you"],
    ["doing","good","work"]
]

#print(matrix[0][1])         #this will get me second word of first list

for rows in matrix:
    for item in rows:
        print(item)

numbers = [1,2,2,3,4,5,5,6,7,8,8]

sole_numbers = []

for number in numbers:
    if number not in sole_numbers:
        sole_numbers.append(number)

print(sole_numbers)