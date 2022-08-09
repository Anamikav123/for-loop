newlist = [1, 2, 3, 4, 5]
print(newlist)
newlist.clear()
print(newlist)
print("--------------------------------------------------------")

thislist = ["Apple", "banana", "AA", "cherry", "aurain"]
print(thislist)
print("--------------------------------------------------------")
thislist.sort()

print(thislist)
thislist.sort(reverse=True)
print(thislist)


print("--------------------------------------------------------")
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = ['g', 'h', 'i']
list4 = list1  # address copied
list4.append('100')
print(list1)
print(list4)
#here list 1 also cahnged to solve the issue create list5
print("--------------------------------------------------------")
list5 = list1.copy()
list5.append('500')
print(list5)
print(list1)
