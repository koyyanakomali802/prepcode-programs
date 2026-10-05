blocked_username = input('enter the usernames:')
username = input("enter the username:")
if username  not in blocked_username:
    print("username is allowed")
else:
    print("not allowed")