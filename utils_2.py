from utils import *
from trader import *
import random as rnd


try:
    def buy_xxx(buy_usd):
        ex_data = list(data.values())[:-1]
        buy_usd_exch = round(buy_usd*ex_data[0], 2)
        if ex_data[1] - buy_usd_exch >= 0:
            uah_quant = round(ex_data[1] - round(buy_usd_exch, 2), 2)
            usd_quant = round(ex_data[2] + buy_usd, 2)
        else:
            req_bal = buy_usd_exch
            avail_bal = round(ex_data[1], 2)
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {req_bal}, AVAILABLE {avail_bal}")
        return {"UAH": uah_quant, "USD": usd_quant}
    buy_xxx_usd = buy_xxx(buy_usd)



    def dump_data_buy_xxx(buy_xxx_usd):
        data_2 = {**data, **buy_xxx_usd}
        with open(cond_system_dir, "w") as json_file:
            json_file.write(json.dumps(data_2))
        return
    dump_data_buy_xxx(buy_xxx_usd)

except:
    pass


try:
    def sell_xxx(sell_usd):
        ex_data = list(data.values())[:-1]
        if ex_data[2] - sell_usd >= 0:
            usd_quant = round((ex_data[2] - sell_usd), 2)
            uah_quant = round(ex_data[1] + (sell_usd*ex_data[0]),2)
        else:
            req_bal = sell_usd
            avail_bal = ex_data[2]
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {req_bal}, AVAILABLE {avail_bal}")
        return {"UAH":uah_quant, "USD": usd_quant}
    sell_xxx_usd = sell_xxx(sell_usd)

    def dump_data_sell_xxx(sell_xxx_usd):
        data_2 = {**data, **sell_xxx_usd}
        with open(cond_system_dir, "w") as json_file:
            json_file.write(json.dumps(data_2))
        return
    dump_data_sell_xxx(sell_xxx_usd)

except:
    pass




if args["BUY ALL"] == True:
    def buy_all():
        ex_data = list(data.values())[:-1]
        if ex_data[1] > 0:
            usd_quant = ex_data[2] + (int((ex_data[1] / (ex_data[0]))*100)/100)
            uah_quant = round(((ex_data[1]/ex_data[0])-(int((ex_data[1] / (ex_data[0]))*100)/100))*ex_data[0], 2)
        return {"UAH": uah_quant, "USD": usd_quant}
    buy_all_usd = buy_all()

    def dump_data_buy_all(buy_all_usd):
        data_2 = {**data, **buy_all_usd}
        with open(cond_system_dir, "w") as json_file:
            json_file.write(json.dumps(data_2))
        return
    dump_data_buy_all(buy_all_usd)


if args["SELL ALL"] == True:
    def sell_all():
        ex_data = list(data.values())[:-1]
        if ex_data[2] >= 0:
            uah_quant = ex_data[1] + (ex_data[2] * ex_data[0])
            usd_quant = round(0,2)
        return {"UAH": uah_quant, "USD": usd_quant}
    sell_all_usd = sell_all()

    def dump_data_sell_all(sell_all_usd):
        data_2 = {**data, **sell_all_usd}
        with open(cond_system_dir, "w") as json_file:
            json_file.write(json.dumps(data_2))
        return
    dump_data_sell_all(sell_all_usd)


if args["NEXT"] == True:
    def course_change():
        ex_data = list(data.values())
        start = ex_data[0] - ex_data[3]
        stop = ex_data[0] + ex_data[3]
        course = float('{:.2f}'.format(round(rnd.uniform(start, stop), 2)))
        pre_course = {"course": course}
        data_2 = {**data, **pre_course}
        with open(cond_system_dir, "w") as json_file:
            json_file.write(json.dumps(data_2))
        return pre_course
    course_change()

if args["RESTART"] == True:
    def restart():
        with open(config_dir, "r") as json_file:
            data = json.load(json_file)
        with open(cond_system_dir, "w") as json_file:
            json_file.write(json.dumps(data))
        return data
    restart()