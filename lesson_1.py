import os
import re
import calendar
filename_3 = "authors.txt"

def sort_def(filename_3):
    dict_dates_modify = []
    dates_list = []
    date_modified = []
    month_dict = {name: num for num, name in enumerate(calendar.month_name) if num}
    pattern_of_date = r'\d{1,2}\w{2}\s\w{3,10}\s\d{4}'
    with open(filename_3, "r") as file_txt:
        str_ = [line.strip() for line in file_txt.readlines()]
        # for elem in str_:
        #     if len(elem) > 20:
        #         date, info = line.split('-')
        for elem in str_:
            dates_str = "".join(re.findall(pattern_of_date, elem))
            dict_dates_modify.append({"date_original": dates_str})
            dates_list.append(dates_str)
            # print(dates_list)

            for elem in dates_list:
                if len(elem):
                    dd, mm, yyyy = elem.split()
                    dd = int(dd[:-2])
                    for key in month_dict.keys():
                        if key == mm:
                            mm = month_dict[key]
                    date_modified.append(".".join(['{:02}'.format(dd),'{:02}'.format(mm),yyyy]))
        print(date_modified)

    # result = dict_dates_modify.copy()
    # for elem in result:
    #     for key,val in elem.items():
    #         elem[key, ]
    #
    # for key, val in cat_2.items():
    #     if key in cat_1:
    #         my_dict_3[key] = [my_dict_3[key], val]
    #     else:
    #         my_dict_3.update({key: val})




    return dict_dates_modify
#
#
#
#
# # # dates = "".join(re.findall(pattern, elem))
print(sort_def(filename_3))




# filename_3 = "authors.txt"
# #
# def sort_def(filename_3):
#     dict_dates_modify = []
# month_dict = {name: num for num, name in enumerate(calendar.month_name) if num}
#     pattern = r'\d{1,2}\w{2}\s\w{3,10}\s\d{4}'
#     with open(filename_3, "r") as file_txt:
#         str_ = [line.strip() for line in file_txt.readlines()]

# line = ["1rf January 1919", "1rf January 1919"]
#
# my_dict = []
# for elem in line:
#     dd, mm, yyyy = elem.split()
#     dd = int(dd[:-2])
#     for key in month_dict.keys():
#         if key == mm:
#             mm = month_dict[key]
#     modi = ".".join(['{:02}'.format(dd),'{:02}'.format(mm),yyyy])
#     my_dict.append({"date": modi})
# print(my_dict)


# if len(elem) > 15:
#     dates_2 = elem.split("-")
#     # print(dates_2[0])