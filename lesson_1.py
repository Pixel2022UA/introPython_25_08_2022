my_str = "Les"

if len(my_str) < 5:
    my_str = my_str + my_str[::-1]
else:
    my_str = my_str

print(my_str)