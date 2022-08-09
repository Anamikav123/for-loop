var = "hello world"
print(var[-11:-6])
a = "hello world"
print(a.replace("hello","hiiii"))
print(a.upper())
print(a.lower())
print(a.capitalize())
b = "         hey how are you           "
print(b)
print(b.strip())
print(b.lstrip())
print(b.rstrip())
print("------------------------------------------------")
s="hello Anamika"
s1="hello,Anamika"
s2="hello*Anamika*aNAMIKA"
s3="hello/Anamika"
s4="hello.Anamika"
print(s.split(" "))
print(s1.split(","))
print(s2.split("*"))
print(s3.split("/"))
print(s4.split("."))
c1="hello world"
print(c1.center(20,"_"))
count_string1="anu is a good  anu anu"
print(count_string1.count("anu"))
endswith_string1="hello world."
print(endswith_string1.endswith("."))
print(endswith_string1.endswith("d"))
print("------------------------------------------------")

find_string="i am a good good student"
print(find_string.find("good"))
print(find_string.find("good",5))
print(find_string.find("good",1,3))
print(find_string.find("good",5,10))
print(find_string.find("good",10))
print("------------------------------------------------")

find_string1="i am a good student"
print(find_string1.find("good"))
print(find_string1.find("good",5))
print(find_string1.find("good",1,3))
print(find_string1.find("good",5,10))
print(find_string1.find("good",10))
print("------------------------------------------------")

find_string4= "please arrest dileep"
print(find_string4.find("dileep"))
print(find_string4.find("dileep",2,6))
print(find_string4.index("dileep",2,6))




