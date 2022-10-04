import calendar

### TASK №1 ######################################################

filename_1 = "domains.txt"


def domains_list(filename_1):
    with open(filename_1, "r") as file:
        data = [domains.strip().replace(".", "") for domains in file.readlines()]
    return data


domains_list(filename_1)

### TASK №2 ######################################################

filename_2 = "names.txt"


def second_names_list(filename_2):
    names_list = []
    with open(filename_2, "r") as file:
        for elem in file.readlines():
            names_list.append(elem.rsplit("\t")[1])
    return names_list


second_names_list(filename_2)

### TASK №3 ######################################################

filename_3 = "authors.txt"


def sort_def(filename_3):
    dict_dates = []
    with open(filename_3, "r") as file_txt:
        dates_list = [line.strip().split(" - ")[0] for line in file_txt.readlines() if "-" in line]
        for elem in dates_list:
            if len(elem.split()) == 3:
                dict_dates.append([{"date": elem}])
    return dict_dates


sort_def(filename_3)

### TASK №4 ######################################################

filename_3 = "authors.txt"

def sort_def(filename_3):
    dates_2 = []
    month_dict = {name: num for num, name in enumerate(calendar.month_name) if num}
    my_dict_keys = ["date_original", "date_modified"]
    with open(filename_3, "r") as file_txt:
        date_1 = [line.strip().split(" - ")[0] for line in file_txt.readlines() if "-" in line]
        for elem in date_1:
            if len(elem.split()) == 3:
                dd, mm, yyyy = elem.split()
                dd = int(dd[:-2])
                for key in month_dict.keys():
                    if key == mm:
                        mm = month_dict[key]
            dates_2.append(".".join(['{:02}'.format(dd), '{:02}'.format(mm), yyyy]))
    my_dict_values = zip(date_1, dates_2)
    my_dict = [dict(zip(my_dict_keys, values)) for values in my_dict_values]
    return my_dict


sort_def(filename_3)

####################################################################