#logical oparator
a = 50
b = 100
print(a > 10 and b > 2000)
print(a > 10 or b > 2000)
print(not (a > 10 and b > 2000))
# identity  oparators#is is not
x = [30, 40]
y = [30, 40]
z = x
print("------------------------------")
print(x is y)
print(x is not y)
print(x is  z)
print(x is not z)
print("------------")
print("Address of a",id(x))
print("Address of a",id(y))
print("Address of a",id(z))

