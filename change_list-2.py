change_list = [1, 2, 3, 4, 5, "hello", "job", True, False, None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(change_list)
change_list[0] = "change1"
print(change_list)
change_list[-1] = "Change-Last"
print(change_list)
#change_list[-1][-1] = "Change-Last"
#print(change_list)
#change_list[-1][8] = "Change-Last"
#print(change_list)
change_list[0:3] = ["hellow"]
print(change_list)
change_list.insert(4,"Bobby")
print(change_list)
change_list.append("Appended")
print(change_list)

