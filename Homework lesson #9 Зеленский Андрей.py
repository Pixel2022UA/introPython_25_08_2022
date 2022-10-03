import random as rnd
import string as str


my_list = ["dsfsgh", "atyqwet", "1", "2qwer", "34yahg", "fdhhh", "wfeh", "qwe"]
my_list_2 = ["asfsgh", "tyqwet", 1 , "2qAwer", 45, 78, "afeh", "qwe"]
my_str = "WE*RHz2356ugsgh34567seRh"
my_str_2 = "zqabcfvVti*IgveefgjkR#"

### TASK №1 ######################################################

def sort_list(my_list):
    my_new_list = []
    for index, element in enumerate(my_list, 1):
        if index % 2:
            my_new_list.append(element[::-1])
        else:
            my_new_list.append(element)
    return my_new_list


### TASK №2 ######################################################

def list_with_a_first(my_list):
    my_new_list_1 = []
    for element in my_list:
        if "a" == element[0]:
            my_new_list_1.append(element)
    return my_new_list_1

### TASK №3 ######################################################

def list_with_a(my_list):
    my_new_list_2 = []
    for element in my_list:
        if "a" in element:
            my_new_list_2.append(element)
    return my_new_list_2

### TASK №4 ######################################################

def list_str(my_list_2):
    my_new_list_3 = []
    for element in my_list_2:
        if element is str(element):
            my_new_list_3.append(element)
    return my_new_list_3
print(list_str(my_list_2))
### TASK №5 ######################################################

def onetime_elem_in_str(my_str):
    my_new_list_4 = []
    for elem in set(my_str):
        if my_str.count(elem) == 1:
            my_new_list_4.append(elem)
    return my_new_list_4

### TASK №6 ######################################################

def inter_elem(my_str, my_str_2):
    my_new_list_5 = list((set(my_str).intersection(set(my_str_2))))
    return my_new_list_5

### TASK №7 ######################################################

def onetime_inter_elem(my_str, my_str_2):
    my_new_list_6 = []
    for element in set(my_str) and set(my_str_2):
        if my_str.count(element) == 1 and my_str_2.count(element) == 1:
            my_new_list_6.append(element)
    return my_new_list_6

### TASK №8 ######################################################

names = ["Jack", "Piter", "Liza", "Elvis"]
domains = ["com", "ua", "com.ua", "biz"]

def email_generator(names, domains):
    rnd_name = rnd.choice(names)
    rnd_domain = rnd.choice(domains)
    rnd_int_to_str = rnd.randint(100, 999)
    rnd_str = "".join(rnd.choice(str.ascii_lowercase) for i in range(rnd.randint(5, 7)))
    rnd_email = "".join(f"{rnd_name}.{rnd_int_to_str}@{rnd_str}.{rnd_domain}")
    return rnd_email
    # или сразу return f"{rnd_name}.{rnd_int_to_str}@{rnd_str}.{rnd_domain}")

