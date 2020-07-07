price_of_car = 30000

has_good_credit = 2000

#int(input("enter marks percentage achieved:  ")) 

if has_good_credit >= 2000:

    down_payment = price_of_car * 0.20
    print("Payment to be paid is : " +str(down_payment) +"dollars")
else: 
    down_payment = price_of_car * 0.50
    print("Payment to be paid is : "+str(down_payment) +"dollars")

#print(round(number))        #this function is used to round the value

#print(abs(number))          #this function will always return the round value   

