import random as rnd
import string as str_
import json
import os


### TASK №1 ######################################################

def generate_txt_data():
    symbols = str_.printable[0:62] + " "
    rnd_str = "".join(rnd.choice(symbols) for i in range(rnd.randint(100, 1000)))
    return rnd_str


generate_txt_data()


### TASK №2 ######################################################

def generate_json_data():
    def rnd_keys():
        key = "".join(rnd.choice(str_.ascii_lowercase) for i in range(5))
        return key

    def rnd_vals():
        val_1 = rnd.uniform(0, 1)
        val_2 = rnd.randint(-100, 100)
        val_3 = rnd.choice([True, False])
        list_vols = rnd.choice([val_1, val_2, val_3])
        return list_vols

    rnd_dict = {rnd_keys(): rnd_vals() for elem in range(rnd.randint(5, 20))}
    return rnd_dict


generate_json_data()

### TASK №3 ######################################################

dirname = "C:/Users/Пиксель/PycharmProjects/introPython_25_08_2022/random.txt"

def generate_and_write_file(dirname: str):
    if os.path.splitext(dirname)[1][1:] == "json":
        with open(dirname, 'w') as json_file:
            json_file.write(json.dumps(generate_json_data()))
    elif os.path.splitext(dirname)[1][1:] == "txt":
        with open(dirname, "w") as file:
            file.write(generate_txt_data())
    else:
        print("Unsupported file format")
    return


generate_and_write_file(dirname)
