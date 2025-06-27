member = input("Enter a new member: ")
file = open("members.txt", "a")
file.write(member + "\n")
file.close()