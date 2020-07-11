prices = [40,50,75,100]
i=0
res = 0
for item in prices:
    res = res+ item

print(res)

#Nested Loop

for y in range(4):
    for x in range(3):
        print(f"({x}, {y})")

#Exercise

numbers = [6,2,6,2,6]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output+= "*"
    print(output)