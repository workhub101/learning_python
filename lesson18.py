# def add_numbers(num1, num2):
#     sum_result = num1 + num2
#     return sum_result
# result = add_numbers(5,3)
# print(result)
# def concatenate_strings( str1 , str2):
#     result = str1 + " " +str2
#     return result
# output =concatenate_strings("Hello", "world!")
# print(output)
# def sum_digits(number):
#     total = 0
#     for digit in str(number):
#         total += int(digit)
#     return total
# num = 12345
# result = sum_digits(num)
# print(result)

def area(width,lenght):
    area_result = width * lenght
    return area_result
width1=int(input("please enter a number for a width of a rectangle"))
lenght1=int(input("please enter a number for a lenght of a rectangle"))
result= area(width1,lenght1)
print(result )

def is_even(num):
    if num % 2 == 0:
        print(True)
        return True
    elif num % 2 != 0:
        print ("false")
        return False
num100 = int(input("please enter a number"))
result= is_even(num100)
print(result)

def find_max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"{num1} is the most" )
        return num1
    elif num2>num1 and num2>num3:
        print is (f"{num2} is the most")
        return num2
    if num3>num1 and num3>num2:
        print(f"{num3} is the most")
        return num3
num1=int(input("please enter a number"))
num2=int(input("please enter a number"))
num3=int(input("please enter a number"))
result=find_max(num1,num2,num3)
print(result)
def is_prime(num1):
    I=2
    if num1<I:
        print("prime")
    if num1% I == 0:
        print("number is composite")
    elif num1 % I != 0 :
        I=I+1
        if num1 % I == 0:
           print("number is composite")
        if num1 % I != 0:
            print("number is prime")
    return num1
num1=int(input("please enter a number"))
result= is_prime(num1)
print(result)
    
 
def calculate_power(num1,num2,):
    result=num1
    for i in range(1,num2):
        result*=num1
    return result
num1=int(input("please enter a number for a base"))
num2=int(input("please enter a number with a exponent"))
result=calculate_power(num1,num2)
print(result)
