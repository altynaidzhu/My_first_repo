
username = input("Enter your nickname: ")


if len(username) > 12:
    print("Your username is tooo long!!!")
elif not username.find(" ") == -1:
    print("Can't contain spaces")
elif not username.isalpha():
    print("Can't contain numbers")
else:
    print(f"Welcome {username} ")
username = username.replace(" ", "")
username = username.replace("digit", "")
