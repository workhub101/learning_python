numbers=[16,3,45,87,43,1]
total=0
for num in numbers:
    
    total=total+num
print(total)


if total<100:
    print("you are within 100")
else:
    print("you are out of 100")

for i in range(1,51):
    if i % 2 == 0:
        print(i)

start = int(input("enter the start value"))
end = int(input("please enter the end value"))
for i in range(start, end+1):
    if i % 3 == 0:
        print("the number is divisible by 3")
        print(i)
    if i % 5 ==0:
        print("the number is divisible by 5")
        print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("the number is divisible by 3 and 5")
        print(i)