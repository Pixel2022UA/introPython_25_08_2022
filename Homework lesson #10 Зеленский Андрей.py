import os
import re


### TASK №1 ######################################################

filename_1 = "domains.txt"
def domains_list(filename_1):
    with open(filename_1, "r") as file:
        data = [domains.strip().replace(".", "") for domains in file.readlines()]
    return data

### TASK №2 ######################################################

filename_2 = "names.txt"

def second_names_list(filename_2):
    names_list = []
    with open(filename_2, "r") as file:
        for elem in file.readlines():
            names_list.append(elem.rsplit("\t")[1])
    return names_list

### TASK №3 ######################################################

filename_3 = "authors.txt"

def sort_def(filename_3):
    dict_dates = []
    pattern = r'\d{1,2}\w{2}\s\w{3,10}\s\d{4}'
    with open(filename_3, "r") as file_txt:
        str_ = [line.strip() for line in file_txt.readlines()]
        for elem in str_:
            dates = "".join(re.findall(pattern, elem))
            if len(dates):
                dict_dates.append({"date": dates})
    return dict_dates


### TASK №4 ######################################################