# a
t = ("foo",)
# c
x = ("red","green","blue")
y = list(x)
y.append("yellow")
x =tuple(y)
print(x)


t=("pen","book","banana","pencil")
l=list(t)
l.remove("banana")
t=tuple(l)
print(t)
t=(5,10,15)
l=list(t)
l[1]=20
t=tuple(l)
print(l)

t=("Python","Java","C++")
if "Java" in t:
    print("Java is present in this tuple")
T1 = (1,2,3,4,5,6,7,8)
print(T1[1::2])
print(T1[-1:-5:-2])
print(T1[::-1])
print(T1[:7:2])
T1=(45,67,98)
T2=((45,67,98))
print( 45 in T2)
print(45 in T1)
