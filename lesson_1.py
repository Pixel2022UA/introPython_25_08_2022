# import calendar
import random as rnd
# filename_3 = "authors.txt"
#
# def sort_def(filename_3):
#     dates_2 = []
#     month_dict = {name: num for num, name in enumerate(calendar.month_name) if num}
#     my_dict_keys = ["date_original", "date_modified"]
#     with open(filename_3, "r") as file_txt:
#         date_1 = [line.strip().split(" - ")[0] for line in file_txt.readlines() if "-" in line]
#         for elem in date_1:
#             if len(elem.split()) == 3:
#                 dd, mm, yyyy = elem.split()
#                 dd = int(dd[:-2])
#                 for key in month_dict.keys():
#                     if key == mm:
#                         mm = month_dict[key]
#             dates_2.append(".".join(['{:02}'.format(dd), '{:02}'.format(mm), yyyy]))
#     my_dict_values = zip(date_1, dates_2)
#     my_dict = [dict(zip(my_dict_keys, values)) for values in my_dict_values]
#     return my_dict
#
# print(sort_def(filename_3))
#
#
#
#
#
# key = "".join(rnd.choice(str_.ascii_lowercase) for i in range(5))
# val_1 = rnd.uniform(0, 1)
# val_2 = rnd.randint(-100, 100)
# val_3 = rnd.choice([True, False])
# list_option = rnd.choice([val_1, val_1, val_3])
#
#
# print(val_1, val_1, val_3)

# C:\Users\Пиксель\PycharmProjects\introPython_25_08_2022

# "".join(re.search('(\d{4})', film))

import re
import os
import shutil
#
# folder = "K:/Фильмы ч2/"
# list_films = os.listdir("K:/Фильмы ч2")
# for film in list_films:
#     if film.endswith(".txt"):
#         print(type(film))
#         _ = re.search('(\d{4})', film)
#         year = " - " + _.group() + " - КП"
#         path_film_name = film[:-4]+year
#         path_film_name_dir = folder+path_film_name
#         print(path_film_name, path_film_name_dir)
#         if not os.path.exists(path_film_name):
#             try:
#                 os.mkdir(path_film_name_dir)
#             except FileExistsError:
#                 pass
#             shutil.move(folder+film, path_film_name_dir)


