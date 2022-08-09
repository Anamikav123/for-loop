#space give false,number and alphabets are only give true value

isalnum="Anamika12"
print(isalnum.isalnum())
print("---------------------------------------")
isal="Anamika thhh"
print(isal.isalpha())
print("---------------------------------------")
isal="Anamika"
print(isal.isalpha())
print("---------------------------------------")
isalnum="Anamika12"
print(isalnum.isalnum())
print("---------------------------------------")
isalnum="Anamika"
print(isalnum.isalnum())
print("---------------------------------------")
isalnum="55452"
print(isalnum.isalnum())
print("---------------------------------------")
isalnum="Anamika##"
print(isalnum.isalnum())
print("---------------------------------------iden")

#is identifier
var="Anamika"
print(var.isidentifier())
var="Ana_mika"
print(var.isidentifier())
var="Anamika7"
print(var.isidentifier())
var="Anamika67@3"
print(var.isidentifier())
var="777Anamika"
print(var.isidentifier())
print("---------------------------------------space")

#isspace,cheching all charecters have space
var="Anu Anu"
print(var)
print(var.isspace())
var="      "
print(var.isspace())
print("---------------------------------------title")

# istitle--
is_title= "He is a good Man"
print(is_title)
print(is_title.istitle())
is_title= "He Is A Good Man"
print(is_title.istitle())
# isupper and lower

is_upper= "HE Is A GOOD"
print(is_upper)
print(is_upper.isupper())
is_lower= "hello kitty"
print(is_lower.islower())
print("---------------------------------------")
# join list
X=['a','b','c']
print(''.join(X))
X=['a','b','c']
print('#'.join(X))

string_partition="ahcsfteue"
print(string_partition.partition('c'))

string_replace="joseph is a good guy"
print(string_replace.replace('joseph','marry'))

string_replace3="joseph is a good guy,joseph is fair,joseph is handsome ,joseph"
print(string_replace3.replace('joseph','marry',2))

starts_with="how are you"
print(starts_with.startswith('you'))

swapcase_str="How are You"
print(swapcase_str.swapcase())













