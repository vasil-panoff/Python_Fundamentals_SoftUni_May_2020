age = int(input())

if age <= 14:
    print("drink toddy")
elif age <= 18:
    print("drink coke")
elif age <= 21:
    print("drink beer")
elif age > 21:
    print("drink whisky")


#alt solution

#age = int(input())
#message = "drink "
#if age <= 14:
#   message += "toddy"
#elif age <= 18:
#   message += "coke"
#elif age <= 21:
#   message += "beer"
#else:
#   message += "whisky"
#print (message)