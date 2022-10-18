import os
import json


config_dir = os.path.abspath("config.json")
cond_system_dir = os.path.abspath("cond_system.json")

def load_data(config_dir, cond_system_dir):
    with open(config_dir, "r") as json_file:
        data_1 = json.load(json_file)
    if os.path.getsize(cond_system_dir) == 0:
        data = data_1
        with open(cond_system_dir, "w") as json_file:
            json_file.write(json.dumps(data))
    else:
        with open(cond_system_dir, "r") as json_file:
            data_2 = json.load(json_file)
        data = {**data_1, **data_2}
    return data
data = load_data(config_dir, cond_system_dir)
# print(data)


def rate(data):
    price = data["course"]
    return price
rate(data)



def available(data):
    uahusd = " ".join([(str(k)+" "+ str(v)) for k, v in data.items()][1:3])
    return uahusd
available(data)




