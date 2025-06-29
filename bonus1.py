# password = input("Enter Password to check: ")
# check_password = {}
# if(len(password) <= 8):
#     check_password['length'] = False
# else:
#     check_password['length'] = True
    
# is_digit = False
# for c in password:
#     if c.isdigit():
#         is_digit = True
# check_password['contains_digit'] = is_digit

# is_upper = False
# for c in password:
#     if c.isupper():
#         is_upper = True
# check_password['contains_upper'] = is_upper

# if(all(check_password.values())):
#     print("Strong Password")
# else:
#     print("Weak Password")
  
width = float(input("Enter Width: "))
height = float(input("Enter height: "))
if width == height:
    exit("This is a square not rectangle")
else:
    print(f"the area is : {width * height}")