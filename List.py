cars = ["BMW", "Mercides", " Honda", "toyota", "KIA", "Ford"]

#print(cars[2])  #this will print 3rd index object
cars[5]= ("blue berry") #this will replace the index 5 value however replace function do not replace it permanently
#we can unpack the tuple with this method
a,b,c,x,y,z = cars
print(y)   #this will print y = "KIA" in above List

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

#this is tuple
num = (1,3,6,8,9,12)
#we can unpack the tuple with this method
a,b,c,x,y,z = num
print(y)   #this will print y = 9 in above tuple
