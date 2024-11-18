fantasy_heroes={
    "Elinor" : "Level 12",
    "Gareth" : "Level 8",
    "Lyra" : "Level 15"
}
print(fantasy_heroes)
Gareth= fantasy_heroes["Gareth"]
print("Gareth:",Gareth)
x=fantasy_heroes.keys()
print(x)
x=fantasy_heroes.values()
print(x)
fantasy_heroes["Lyra"]="Level 18"
print(fantasy_heroes)
fantasy_heroes["Peter"]="level 7"
print(fantasy_heroes)
del fantasy_heroes ["Elinor"]
print(fantasy_heroes)
x=fantasy_heroes.items()
print(fantasy_heroes)

sample_dict={
    "0":"10",
    "1":"20"
}
sample_dict["3"]="30"
print(sample_dict)

dic1={
    1:10,
    2:20
}
dic2={
    3:30,
    4:40
}
dic3={
    5:50,
    6:60
}
mydict=dic1.copy()
print(mydict)
mydict.update(dic2)
print(mydict)
mydict.update(dic3)
print(mydict)

sample_dict={
    "a":"100",
    "b":"200",
    "c":"300"
}
x=sample_dict.values()
if "200" in x:
    print("200 is present in this dict")

