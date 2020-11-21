# User registration
users = {}
new_user = {}
requested_data = ["first_name", "last_name", "nick_name","password", "comfirm_password"]

for data in requested_data:
    if data == "password":
        passwd = input(f"Enter {data}: ")
    elif data == "comfirm_password":
        passwd2 = input(f"Enter {data}: ")
    else:
        info = input(f"Enter {data}: ") 
        new_user.update({data:info})
else:
    if passwd == passwd2:
        new_user.update({"password":passwd})

print(new_user)

# Storing value in bigger Dictionary

key = len(users)
key += 1
users.update({key:new_user})
print(users)
