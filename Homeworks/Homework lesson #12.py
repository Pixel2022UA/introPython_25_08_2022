import json
import re

dirname = "data.json"


###### TASK 1 #############################################

def authors_data(dirname):
    with open(dirname, "r") as json_file:
        data = json.load(json_file)
    return data


data_1 = authors_data(dirname)


###### TASK 2 #############################################

def sort_by_surname(elem):
    surname = elem["name"]
    sort_sur = surname.split()[-1]
    return sort_sur


sorted_values = sorted(data_1, key=sort_by_surname)


###### TASK 3 #############################################


def sort_by_lenth(elem):
    my_string = elem["text"]
    sort_by_len = len(my_string.split())
    return sort_by_len


sorted_values = sorted(data_1, key=sort_by_lenth)

###### TASK 4 #############################################

def sort_by_death(elem):
    my_string = elem["years"]
    pattern_1 = r"[0-9BC]+"
    zip_values = re.findall(pattern_1, my_string)
    result = " ".join(zip_values)
    death = []
    if "BC" in result:
        death = int(zip_values[-2])*-1
    else:
        death = int(zip_values[-1])
    return death


sorted_values = sorted(data_1, key=sort_by_death)

###########################################################