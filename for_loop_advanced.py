testing-----------------------------------------------updated
# 1-10 numbers multiplication
mul=1
for i in range(1,11):
    mul*=i
print((mul))
print("-----------------------------------------------------")
#to get sum of given numbers
num=12345
sum=0
# we can't find length in integer form so we convert in into sting
for i in range (len(str(num))):
    # To get the last number from given numbers we use modulus of 10
    temp=num%10
    # To take out that number divide it using 10
    num=num//10
    print(num)
    # To add it with previous number this step is used
    sum+=temp
print(sum)
