age1=int(input("enter your age"))
if age1>=18:
    print("you are a adult")
else:
    print("you are not a adult yet")
score1=int(input("please enter you test score in percent"))
if score1>=90:
    print("you got a A")
elif score1<90 and score1>=80:
    print("you got a B")
elif score1<80 and score1>=70:
 print("you got a C")
if score1<70:
   print("you failed")
age2=int(input("how old are you"))
driver1=(input("do you have a valid drivers licence"))
if driver1=="yes" and age2>=16:
   print("you can drive")
else:
   print("you cannot drive")