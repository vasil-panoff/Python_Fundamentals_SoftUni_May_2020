my_dict = {'Peter': 21, 'George': 45, 'John': 45}

# reversed
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0]), reverse=True))
# ascending
# sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print(sorted_dict)