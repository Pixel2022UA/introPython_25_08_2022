my_str_1 = "abcvnnnRj"
my_str_2 = "abcvvvvrr"

        ## Вариант записи №1 ##

my_list_1 = []
for element in my_str_1 and my_str_2:
    if my_str_1.count(element) and my_str_2.count(element) == 1:
        my_list_1.append(element)

        ## Вариант записи №2 ##

my_list_2 = [element for element in my_str_1 and my_str_2 if my_str_1.count(element) and my_str_2.count(element) == 1]

my_list_3 = []
for element in my_str_1 and my_str_2:
    if my_str_1.lower().count(element) and my_str_2.lower().count(element) == 1:
        my_list_3.append(element)

        ## Вариант записи №2 ##

my_list_4 = [element for element in my_str_1 and my_str_2 if my_str_1.lower().count(element) and my_str_2.lower().count(element) == 1]



print(my_list_1)
print(my_list_2)
print(my_list_3)
print(my_list_4)