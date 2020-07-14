char = input("For Sum please enter '+' sign : ")

if char == '+':
    def calc_sum (first_num, sec_num):
        return first_num + sec_num
        

    first_num = int(input("Enter first number : "))
    sec_num = int(input("Enter second number : "))
    res = calc_sum(first_num, sec_num)
    print(res)
else:
    print("Please enter the right sign")



def email_storage (email):
    emails = {
    "Bot's Email": "no-reply@gmail.com",
    "Service Email": "customer-service@gmail.com",
    "Recipient's email": ""
    }
    emails["Recipient's email"] += email
    return emails

email = input("Enter your email :  ")
emails = email_storage(email)
print(emails)
    

