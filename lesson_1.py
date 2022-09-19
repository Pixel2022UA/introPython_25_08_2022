my_str = "gaerrhdhagg"

if len(my_str) % 2 != 0:
    my_str = my_str + "_"

my_list_1 = [my_str[index:index + 2] for index in range(0, len(my_str), 2)]

        ## Вариант записи №1 ##
my_list_2 = []
for index in range(0, len(my_str), 2):
    my_list_2.append(my_str[index:index + 2])

print(my_list_1, my_list_2)