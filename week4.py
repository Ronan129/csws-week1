names = ['a', 'b', 'c', 'd', 'Admin']
username = 'q'
if username == "Admin":
    print(f"Hello {username}, would you like a status report")
elif username in names:
    print(f"hello{username}, thanks for logging in")
else:
    print("username not recognised")
    