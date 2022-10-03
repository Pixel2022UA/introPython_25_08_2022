# import calendar
#
# filename_3 = "authors.txt"
#
# def sort_def(filename_3):
#     dates_1 = []
#     dates_2 = []
#     month_dict = {name: num for num, name in enumerate(calendar.month_name) if num}
#     with open(filename_3, "r") as file_txt:
#         str_ = [line.strip().split(" - ") for line in file_txt.readlines() if len(line) > 10]
#         for elem in str_:
#             dates_1.append(elem[0])
#         for elem in dates_1:
#             dd, mm, yyyy = elem.split()
#             dd = int(dd[:-2])
#             for key in month_dict.keys():
#                 if key == mm:
#                     mm = month_dict[key]
#             dates_2.append(".".join(['{:02}'.format(dd), '{:02}'.format(mm), yyyy]))
#         my_dict_values = zip(dates_1, dates_2)
#         my_dict_keys = ["date_original", "date_modified"]
#         my_dict = [dict(zip(my_dict_keys, values)) for values in my_dict_values]
#     return my_dict
#
# print(sort_def(filename_3))

#
# import calendar
#
# filename_3 = "authors.txt"
#
# def sort_def(filename_3):
#     dates_1 = []
#     dates_2 = []
#     month_dict = {name: num for num, name in enumerate(calendar.month_name) if num}
#     with open(filename_3, "r") as file_txt:
#         str_ = [line.strip().split(" - ") for line in file_txt.readlines() if len(line) > 10]
#         for elem in str_:
#             dates_1.append(elem[0])
#         for elem in dates_1:
#             dd, mm, yyyy = elem.split()
#             dd = int(dd[:-2])
#             for key in month_dict.keys():
#                 if key == mm:
#                     mm = month_dict[key]
#             dates_2.append(".".join(['{:02}'.format(dd), '{:02}'.format(mm), yyyy]))
#         my_dict_values = zip(dates_1, dates_2)
#         my_dict_keys = ["date_original", "date_modified"]
#         my_dict = [dict(zip(my_dict_keys, values)) for values in my_dict_values]  # еще можно добавить проверку if len(dates_1) == len(dates_2)
#     return my_dict
#
# print(sort_def(filename_3))


