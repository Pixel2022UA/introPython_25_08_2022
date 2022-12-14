import os
import json
import random as rnd

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

global_data = load_data(config_dir, cond_system_dir)
data_for_func = list(global_data.values())


def upload_files(filename):
    data_2 = {**global_data, **filename}
    with open(cond_system_dir, "w") as json_file:
        json_file.write(json.dumps(data_2))
    return


def round_all(number):
    number = int(number * 100)/100
    return number


def rate(global_data):
    price = "".join("{:.02f}".format(global_data["course"]))
    return price


def available(global_data):
    balance = "".join("UAH {:.02f}".format(global_data["UAH"]) + " " + "USD {:.02f}".format(global_data["USD"]))
    return balance

def buy_xxx(buy_usd, data_for_func):
    buy_usd_exch = buy_usd * data_for_func[0]
    if data_for_func[1] - buy_usd_exch >= 0:
        uah_quant = round_all(data_for_func[1] - buy_usd_exch)
        usd_quant = round_all(data_for_func[2] + buy_usd)
        buy_xxx_dict = {"UAH": uah_quant, "USD": usd_quant}
        upload_files(buy_xxx_dict)
    else:
        req_bal = round_all(buy_usd_exch)
        avail_bal = round_all(data_for_func[1])
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {req_bal}, AVAILABLE {avail_bal}")

    return


def sell_xxx(sell_usd, data_for_func):
    if data_for_func[2] - sell_usd >= 0:
        usd_quant = round_all((data_for_func[2] - sell_usd))
        uah_quant = round_all(data_for_func[1] + (sell_usd*data_for_func[0]))
        sell_xxx_dict = {"UAH": uah_quant, "USD": usd_quant}
        upload_files(sell_xxx_dict)
    else:
        req_bal = sell_usd
        avail_bal = round_all(data_for_func[2])
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {req_bal}, AVAILABLE {avail_bal}")
    return


def buy_all(data_for_func):
    if data_for_func[1] > data_for_func[0] / 100:                                                                                                       # ???????????? 1 ?????????? ???????????? ????????????
        usd_quant = round_all(data_for_func[2] + (int((data_for_func[1]/(data_for_func[0]))*100)/100))                                                   # ?????????????????????? ???????????????? ??.??. ?????? ?????????? ???????????? ?? uah_quant ?? ???????? ?????????????? ???????????? ???? ??????????
        uah_quant = round_all(((data_for_func[1]/data_for_func[0]) - (int((data_for_func[1]/(data_for_func[0]))*100)/100))*data_for_func[0])             # ?????????????????? ???????????????? ?? ?????????????? ???? ???????? ??????????????, ???????????????? ??????????????
        buy_all_dict = {"UAH": uah_quant, "USD": usd_quant}
        upload_files(buy_all_dict)
    return


def sell_all(data_for_func):
    if data_for_func[2] >= 0.01:
        uah_quant = round_all(data_for_func[1] + (data_for_func[2] * data_for_func[0]))
        usd_quant = 0.00
        sell_all_dict = {"UAH": uah_quant, "USD": usd_quant}
        upload_files(sell_all_dict)
    return


def course_change(data_for_func):
    start = data_for_func[0] - data_for_func[3]
    stop = data_for_func[0] + data_for_func[3]
    course = '{:.2f}'.format(rnd.uniform(start, stop))
    course_dict = {"course": course}
    upload_files(course_dict)
    return


def restart(config_dir):
    with open(config_dir, "r") as json_file:
        data = json.load(json_file)
    upload_files(data)
    return
