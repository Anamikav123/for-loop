# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#   print(i)

num =10
if num % 5 == 0:
    print("num is divisible by 5")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = []
even_list = []
for i in list1:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(odd_list)
print(even_list)

print("-------------------------------------------------")
vowels_and_constants = ['a', 'e', 'i', 'o', 'u', 'r',  'P', 'x', 'E']
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_list = []
constant_list = []
for i in vowels_and_constants:
    i = i.lower()
    if i in vowels:
        vowel_list.append(i)
    else:
        constant_list.append(i)

print(vowel_list)
print(constant_list)

print("-------------------------------------------------")

new = 0
for i in range(0, 5):
    new +=i
print(new)
print("-------------------------------------------------")
string = "Luminar is the BEst Institute"
lower_count = 0
upper_count = 0
space_count = 0
for i in string:
    if i.isspace():
        space_count += 1
    elif i.islower():
        lower_count += 1
    else:
        upper_count += 1
print("lower_count", lower_count)
print("upper_count", upper_count)
print("space_count", space_count)

print("-------------------------------------------------")
# find sum of 1-10
sum = 0
for i in range(0, 11):
    sum +=i
print(sum)
