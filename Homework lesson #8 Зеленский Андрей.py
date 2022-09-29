### TASK №1 ######################################################

my_list = ["dsfsgh", "tyqwet", 1, "2qwer", 45, 78, "wfeh", "qwe"]

        ### Вариант записи №1 ###

my_new_list = []
for index, element in enumerate(my_list, 1):
    if element is str(element) and index % 2 != 0:
        my_new_list.append(element)
     elif index % 2 == 0:
        my_new_list.append(element)


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
    names_ages.append([persons["age"], persons["name"]])
names_ages.sort()
for key, val in names_ages:
    if key == names_ages[0][0]:
        my_list_2.append(val)

        ## Задание б), вариант решения №1 ###


name_list = [persons["name"] for persons in persons]
name_list = [elem for elem in name_list if len(elem) == len(max(name_list, key=len))]

        ## Задание б), вариант решения №2 ###

name_list = []
name_list_long = []
for persons in persons:
    name_list.append(persons["name"])
for elem in name_list:
    if len(elem) == len(max(name_list, key=len)):
        name_list_long.append(elem)

        ## Задание в) ###

age_list = [persons["age"] for persons in persons]
age_list_avg = round(sum(age_list)/len(age_list), 1)


### TASK №5 ######################################################

cat_1 = {'name': 'Kitty_1',
         'colour': 'Red',
         'age': 4,
         'city': 'London',
         }
cat_2 = {'name': 'Kitty_2',
         'colour': 'Brown',
         'age': 7,
         'country': 'China'
         }

    ## Задание a) ###
my_list_1 = list(set(cat_1.keys()).intersection(set(cat_2.keys())))

    ## Задание б) ###

my_list_2 = list(set(cat_1.keys()).difference(set(cat_2.keys())))

    ## Задание в) ###

my_dict = {}
for key, val in cat_1.items():
    if key not in cat_2:
        my_dict[key] = val


my_dict_1 = {key: val for key, val in cat_1.items() if key not in cat_2}

    ## Задание г) Пример записи №1 ###

my_dict_3 = {}
for elem in cat_1:
    if elem in cat_2:
        my_dict_3.update([(elem, [cat_1[elem], cat_2[elem]])])
    else:
        my_dict_3.update([(elem, cat_1[elem])])
for elem_1 in cat_2:
    if elem_1 not in cat_1:
        my_dict_3.update([(elem_1, cat_2[elem_1])])

    ## Задание г) Пример записи №2 ###

my_dict_4 = {}
for elem in cat_1.items():
    if elem[0] not in cat_2:
        my_dict_4[elem[0]] = elem[1]
    else:
        my_dict_4[elem[0]] = [elem[1], cat_2[elem[0]]]
for elem_2 in cat_2.items():
    if elem_2[0] not in cat_1:
        my_dict_4[elem_2[0]] = elem_2[1]


## Задание г) Пример записи №3 (Более короткий вариант) ###

my_dict_3 = cat_1

for key, val in cat_2.items():
    if key in cat_1:
        my_dict_3[key] = [my_dict_3[key], val]
    else:
        my_dict_3.update({key: val})



