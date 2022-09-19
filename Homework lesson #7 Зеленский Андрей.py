## TASK №1 ######################################################

number = 5008
str_number = str(number)
zero_count = str_number.count("0")

## TASK №2 ######################################################

number = 500800

        # Вариант решения 1 ##
str_number = str(number)
len(str_number) - len(str(int(str_number[::-1])))

        ## Вариант решения 2 ##
count_zero = 0
while number % 10 == 0:
    count_zero += 1
    number //= 10

## TASK №3 ######################################################

my_list_1 = [45, "FF", "68", 4, 41]
my_list_2 = [5, "tt", 98, 38]

        ## Вариант решения №1 ##
my_result = my_list_1[::2] + my_list_2[1::2]

        ## Вариант решения №2 ##

my_result = my_list_1[::2]
my_result.extend(my_list_2[1::2])


## TASK №4 ######################################################

my_list = [45, "FF", "68", 4, 41]
new_list = my_list[1:]
new_list.append(my_list[0])

## TASK №5 ######################################################

my_list = [45, "FF", "68", 4, 41]
my_list.append(my_list.pop(0))

## TASK №6 ######################################################

my_str = "43 больше чем 34 но меньше чем 56"
sum = 0
for element in my_str.split(" "):
    if element.isdigit():
        sum += int(element)

# TASK №7 ######################################################

my_str = "My long stringMy long stringMy long stringMy long string"
l_limit = "o"
r_limit = "g"

start = my_str.find(l_limit) + 1
finish = my_str.rfind(r_limit)
sub_str = "".join(my_str[start:finish])

# TASK №8 ######################################################

my_str = "gaerrhdhagg"

if len(my_str) % 2 != 0:
    my_str = my_str + "_"

        ## Вариант записи №1 ##

my_list_1 = [my_str[index:index + 2] for index in range(0, len(my_str), 2)]

        ## Вариант записи №2 ##

my_list_2 = []
for index in range(0, len(my_str), 2):
    my_list_2.append(my_str[index:index + 2])

# TASK №9 ######################################################

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
index = 1
count = 0
for elem in my_list[1:-1]:
    if elem > my_list[index-1] + my_list[index+1]:
        count += 1
    index += 1
print(count)
# TASK №10 ######################################################

my_list = [1, 2, 3, "11", "22", 33]
my_new_list = [i for i in my_list if i is str(i)]

# TASK №11 ######################################################

my_str = "ERggggggggJrtyujhgfwerT$%^#$%&Y"

        ## Вариант решения №1 ##(без учета больших букв)

my_new_list_1 = [element for element in my_str if my_str.count(element) == 1]

        ## Вариант решения №2 ##(с учетом больших букв)

my_new_list_2 = [element for element in my_str if my_str.lower().count(element) == 1]

# TASK №12 ######################################################

my_str_1 = "Qabcvti@#$%^UFD^Y&dfgt"
my_str_2 = "qabcfvVti*Igveefgjk#"

        ## Вариант решения №1 ##(без учета больших букв)

my_new_list_1 = list(set(my_str_2).intersection(set(my_str_1)))

        ## Вариант решения №2 ##(с учетом больших букв)

my_new_list_2 = list(set(my_str_2.lower()).intersection(set(my_str_1.lower())))

# TASK №13 ######################################################

my_str_1 = "abcvnnnj"
my_str_2 = "abcvvvv"

        ## Вариант записи №1 ## (без учета больших букв)

my_list_1 = []
for element in my_str_1 and my_str_2:
    if my_str_1.count(element) and my_str_2.count(element) == 1:
        my_list_1.append(element)

        ## Вариант записи №2 ## (без учета больших букв)

my_list_2 = [element for element in my_str_1 and my_str_2 if my_str_1.count(element) and my_str_2.count(element) == 1]

        ## Вариант решения №3 ## (с учетом больших букв)

my_list_3 = []
for element in my_str_1 and my_str_2:
    if my_str_1.lower().count(element) and my_str_2.lower().count(element) == 1:
        my_list_3.append(element)

        ## Вариант записи №4 ## (с учетом больших букв)

my_list_4 = [element for element in my_str_1 and my_str_2 if my_str_1.lower().count(element) and my_str_2.lower().count(element) == 1]

