tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(len(tuple1))
print(tuple1[3])
print(tuple1[0:2])
len1 = len(tuple1)
print(len1)
print(tuple1[:len1])
print(tuple1[3:len1])
print("--------------------------------------------------------")
print(tuple1.count(5))  # no of occurence
print(tuple1.index(5))
print("--------------------------------------------------------")
# tuple unpacking
fruits = ("apple", "bananna", "cherry")
a, b, c = fruits
print(a)
print(b)
print(c)
print("--------------------------------------------------------")

fruits1 = ("apple", "bananna", "cherry", "guava", "mango", "pinaple")
a, b, *c = fruits1    #baki elements list ayi c le kerum
print(a)
print(b)
print(c)
print("--------------------------------------------------------")
fruits1 = ("apple", "bananna", "cherry", "guava", "mango", "pinaple")
a, *b, c = fruits1    #baki elements list ayi c le kerum
print(a)
print(b)
print(c)

print("--------------------------------------------------------")
fruits1 = ("apple", "bananna", "cherry", "guava", "mango", "pinaple")
*a, b, c = fruits1    #baki elements list ayi c le kerum
print(a)
print(b)
print(c)
#tuple le ne list akki tuple akki insert append ellam cheyyam,tuple is unchnagable
tuuple=(1,2,3)
tuuple=list(tuuple)
tuuple.append(5)
tuuple=tuple(tuuple)
print(tuuple)

ttuuple1=(1,2,3)
ttuuple1=list(ttuuple1)
ttuuple1.append()
ttuuple1=tuple(ttuuple1)
print(ttuuple1)















