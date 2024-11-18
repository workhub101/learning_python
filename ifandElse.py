counter=0
for i in range(4):
 password1=(input("Please enter a password"))
 if password1=="password123":
        print("access granted")
        break
 else:
        counter=counter+1
        print("access denied")
if counter==4:
    print("you have lost all your attemps")