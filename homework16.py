num1=int(input("please enter a number"))
if num1>0:
    print("the number is positive")
if num1==0:
    print("the number is zero")
elif num1<0:
    print("the number is negitive ")
score1=int(input("please enter your score"))
if score1>60:
    print("passed")
    if score1>70:
        print("passed with distinction")
else:
    print("failed")

year1=int(input("print the year"))
if year1 % 4 ==0 :
    if year1 % 100 !=0:
        print("Its a leap year")
if year1 % 400 == 0:
    print("Its a leap year")
    
else:
    print("not a leap year")



age1=int(input("please enter your age"))
if age1<12:
    print("children ticket")
elif age1>12 and age1<18:
    print("teen ticket")
elif age1>18:
    print("adult ticket")
elif age1<0:
    print("not a valid age")

age2=int(input("please enter your age"))
drive1=input("do you have driving experience")
if age2>18:
    if drive1=="yes":
        print("elligible for drivers licence")
    else:
        print("not elligible for drivers licence due to experience")
elif age2<18:
    print("you are under aged to drive")

