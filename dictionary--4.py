dict={1:"she",2:"you",3:"he"}#1,2,3 are keys
print(dict[1])
print(dict[2])
print(dict[3])
#print(dict[4])
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get(1))
print(dict.get(2))
print("----------------------------------")
dict.update({4:"me"})
print(dict)
dict[5]="I"
print(dict)
dict.pop(1)
print(dict)
dict.popitem()
print(dict)
del dict[2]
print(dict)
dict.clear()
print(dict)

