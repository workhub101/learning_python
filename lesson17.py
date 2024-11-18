def my_function():
    print("hello from a function")
my_function()
def greet():
    print("hello,welcome!")
greet()
def sing_song():
    print("I'm singing in the rain")
    print("Just singing in the rain")
sing_song()
def countdown():
    for i in range(10,0,-1):
        print(i)
countdown()

def print_odd_even():
    for i in range(1,11):
        if i % 2 == 0:

            print(i)
            print("number is even" )
        elif i % 2 != 0:
            print(i)
        
            print("number is odd")
print_odd_even()
def number_pattern():
    for i in range(1,7):
        for i in range(1,i):
            print(i,end="")
        print("")
number_pattern()
def print_multiplication_table():
    num1=int(input("please enter a number to make a multiplication table"))
    for i in range(num1,num1*6,num1):
        print(i)
print_multiplication_table()

def divisble_numbers():
    for l in range(1,21):
        print(l)
        if l % 3 == 0:
            print("number is divisble by 3")
            
        if l % 5 == 0:
            print("number is divisble by 5")
            
        if l% 3 == 0 and l % 5 == 0:
            print(" so number is divisble by 3 and 5")
        
            
        elif l % 3 != 0 and l % 5 != 0:
            print("number is not divisble by 3 and 5")
            
divisble_numbers()


def print_square_numbers():
    for k in range(1,6):
        print(k * k)
print_square_numbers()






        
    
