first = [1, 2, 3, 4, 5]
second = [6, 7, 8, 9, 10]
third = first + second
print(third)
# second method

first.extend(second)
print(first)
print(second)
print("--------------------------------------------------------")

Remove_list = [1, 2, 3, 4, 5, "hello"]
print(Remove_list)
Remove_list.remove(1)
print(Remove_list)
Remove_list.remove(2)
print(Remove_list)
# updated list value change--pop means taken out
Remove_list.pop(0)
print(Remove_list)
#  if no valu given last value removed
Remove_list.pop()
print(Remove_list)
#
del Remove_list[0]
print(Remove_list)
# del Remove_list
# print(Remove_list)

print("--------------------------------------------------------")
for_list = [1, 2, 3, 4, 5]
for x in for_list:
    print(x)
    print(x * x)
    print(x * x * x)
    print(x * x * x * x)
# here the space in print called indendation
print("--------------------------------------------------------")

new = ["thanha", 23, "place", "luminar"]
print(len(new))
for i in range(0, len(new)):
    print(new[i])

print("--------------------------------------------------------")
sum = range(0, len(new))
print(sum)
print(list(sum))

