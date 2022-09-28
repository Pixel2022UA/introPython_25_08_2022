### TASK №1 ######################################################

my_list = ["dsfsgh", "tyqwet", 1 , "2qwer", 45, 78, "wfeh", "qwe"]

        ### Вариант записи №1 ###

my_new_list = []
for index, element in enumerate(my_list, 1):
    if element is str(element) and index % 2 != 0:
        my_new_list.append(element[::-1])

        ### Вариант записи №2 ###

my_new_list_1 = [element[::-1] for index, element in enumerate(my_list, 1) if element is str(element) and index % 2 != 0]


### TASK №2 ######################################################

my_list = ["asfsgh", "tyqwet", 1 , "2qwer", 45, 78, "afeh", "qwe"]

        ### Вариант записи №1 ###

my_new_list_1 = []
for element in my_list:
    if element is str(element) and element[0].lower() == "a":
        my_new_list_1.append(element)

        ### Вариант записи №2 ###

my_new_list_2 = [element for element in my_list if element is str(element) and element[0].lower() == "a"]

### TASK №3 ######################################################

my_list = ["asfsgh", "tyqwet", 1 , "2qAwer", 45, 78, "afeh", "qwe"]

        ### Вариант записи №1 ###

my_new_list = []
for element in my_list:
    if element is str(element) and "a" in element.lower():
        my_new_list.append(element)

        ## Вариант записи №2 ###

my_new_list_1 = [element for element in my_list if element is str(element) and "a" in element.lower()]

### TASK №4 ######################################################

persons = [{"name": "Piter", "age": 14}, {"name": "Jack", "age": 4}, {"name": "Ostin", "age": 4}]

        ## Задание а), вариант решения №1 ###

my_list_1 = []
names_ages = [(persons["name"], persons["age"]) for persons in persons]
names_ages.sort(key= lambda elem: elem[1])
my_list_1 = [key for key, val in names_ages if val == names_ages[0][1]]

        ## Задание а), вариант решения №2 (без lambda) ###

names_ages = []
my_list_2 =[]
for persons in persons:
    names_ages.append([persons["name"], persons["age"]])
for elem in names_ages:
    elem = elem.reverse()
names_ages.sort()
for key, val in names_ages:
    if key == names_ages[0][0]:
        my_list_2.append(val)

        ## Задание б), вариант решения №1 ###


name_list = [persons["name"] for persons in persons]
name_list = [elem for elem in name_list if len(elem) == len(max(name_list, key=len))]

        ## Задание б), вариант решения №2 ###

name_list = []
for persons in persons:
    name_list.append(persons["name"])
    for elem in name_list:
        if len(elem) != len(max(name_list, key=len)):
            name_list.remove(elem)

        ## Задание в) ###

age_list = [persons["age"] for persons in persons]
age_list_avg = round(sum(age_list)/len(age_list), 1)


### TASK №5 ######################################################

Cat_1 = {'name': 'Kitty_1',
         'colour': 'Red',
         'age': 4,
         'city': 'London',
         }
Cat_2 = {'name': 'Kitty_2',
         'colour': 'Brown',
         'age': 7,
         'country': 'China'
         }

    ## Задание a) ###
my_list_1 = list(set(Cat_1.keys()).intersection(set(Cat_2.keys())))

    ## Задание б) ###

my_list_2 = list(set(Cat_1.keys()).difference(set(Cat_2.keys())))

    ## Задание в) ###

my_dict = {}
for key, val in Cat_1.items():
    if key not in Cat_2:
        my_dict[key] = val


my_dict_1 = {key: val for key, val in Cat_1.items() if key not in Cat_2}

    ## Задание г) Пример записи №1 ###

my_dict_3 = {}
for elem in Cat_1:
    if elem in Cat_2:
        my_dict_3.update([(elem, [Cat_1[elem], Cat_2[elem]])])
    else:
        my_dict_3.update([(elem, Cat_1[elem])])
for elem_1 in Cat_2:
    if elem_1 not in Cat_1:
        my_dict_3.update([(elem_1, Cat_2[elem_1])])

    ## Задание г) Пример записи №2 ###

my_dict_4 = {}
for elem in Cat_1.items():
    if elem[0] not in Cat_2:
        my_dict_4[elem[0]] = elem[1]
    else:
        my_dict_4[elem[0]] = [elem[1], Cat_2[elem[0]]]
for elem_2 in Cat_2.items():
    if elem_2[0] not in Cat_1:
        my_dict_4[elem_2[0]] = elem_2[1]



