class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def cat(self):
        print("meow")
        print("name",self.name)
    def dog(self):
        print("wofff")

mypet= Animal(name="aditya",age="25")
mypet.cat()