bread_options=["white","wheat","multigrain"]
filling_options=["cheese","lettuce","tomato"]
for bread in bread_options:
    for filling in filling_options:
        sandwich = bread+  " bread with "  +  filling
        print(sandwich)
adj=["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
for i in range(1,21):
    for j in range(1,11):
        print(i*j, end=" ")
    print('')
t = 0
for i in range(0,3):# i=0,1,2
    for j in range(3,5):# j=3,4
        t += i + j #t=0+0+3 t=3+4+0=7 t=7+1+3=11 t=11+1+4=16 t=16+2+3=21 t=21+2+4=27
print(t)