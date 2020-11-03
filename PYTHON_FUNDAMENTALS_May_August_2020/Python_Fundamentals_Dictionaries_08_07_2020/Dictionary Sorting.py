my_dict = {"Peter": 20, "George": 10, "Ivan": 15}
    # asending
# sorted_dict = dict(sorted(my_dict.items(), key=lambda el: el[1]))
    # desending
# sorted_dict = dict(sorted(my_dict.items(), key=lambda el: el[1], reverse=True))
# sorted_dict = dict(sorted(my_dict.items(), key=lambda el: -el[1]))
    # sorting by key and value
sorted_dict = dict(sorted(my_dict.items(), key=lambda el: (el[1], el[0]), reverse=True))


print(my_dict)
print(sorted_dict)