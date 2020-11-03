usernames = input().split(", ")

for username in usernames:
    if len(username) >= 3 and len(username) <= 16 and \
            (username.isalnum() or "_" in username or "-" in username):
        print(username)