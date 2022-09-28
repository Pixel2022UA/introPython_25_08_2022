

my_list = ["asfsgh", "tyqwet", 1 , "2qAwer", 45, 78, "afeh", "qwe"]

        ### Вариант записи №1 ###

# my_new_list = []
# for element in my_list:
#     if element is str(element) and "a" in element.lower():
#         my_new_list.append(element)

        ## Вариант записи №2 ###

my_new_list_1 = [element for element in my_list if element is str(element) and "a" in element.lower()]

print(my_new_list_1)