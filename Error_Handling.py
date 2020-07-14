def calc_sum (first_num, sec_num):
    return first_num + sec_num

try:
    first_num = int(input("Enter first number : "))
    sec_num = int(input("Enter second number : "))
    res = calc_sum(first_num, sec_num)
    print(res)
except ValueError:
    print("Please enter the correct numbers")

