likes = {}
comments = {}

while True:
    cmd_input= input()

    if cmd_input == "Log out":
        break

    args = cmd_input.split(": ")
    cmd = args[0]
    username = args[1]

    if cmd == "New follower":
        if username in likes:
            continue

        likes[username] = 0
        comments[username] = 0
    elif cmd == "Like":
        count = int(args[2])

        if username in likes:
            likes[username] = 0
            comments[username] = 0

        likes[username] += count
    elif cmd == "Comment":
        if username in comments:
            likes[username] = 0
            comments[username] = 0

        comments[username] += 1
    elif cmd == "Blocked":
        if username not in likes:
            print(f"{username} doesn't exist.")
            continue

        likes.pop(username)

print(f"{len(likes)} followers")
sorted_likes = dict(sorted(likes.items(), key=lambda u: (-u[1], u[0])))

for username, count_likes in sorted_likes.items():
    count_comments = comments[username]
    print(f"{username}: {count_likes + count_comments}")