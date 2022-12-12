# practice for loop 
# ask user name and count each character
# "Pranjal Singh"
# P : 1
# r : 1
# a : 2
# n : 1
# j : 1
# a : 2
# l : 1
#   : 1
# S : 1
# i : 1
# g : 1
# h : 1
name = input("enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]