from utils import available, rate, global_data,buy_xxx, sell_xxx, buy_all, sell_all, course_change, restart
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("ARG", default=None, nargs="+")
args = vars(args.parse_args())


if args["ARG"][0] == "AVAILABLE":
    print(available(global_data))
elif args["ARG"][0] == "RATE":
    print(rate(global_data))
elif args["ARG"][0] == "BUY" and "".join(args["ARG"][1]).isdigit():
    buy_usd = float(args["ARG"][1])
    buy_xxx(buy_usd)
elif args["ARG"][0] == "SELL" and "".join(args["ARG"][1]).isdigit():
    sell_usd = float(args["ARG"][1])
    sell_xxx(sell_usd)
elif args["ARG"][0] == "BUY" and args["ARG"][1] == "ALL":
    buy_all()
elif args["ARG"][0] == "SELL" and args["ARG"][1] == "ALL":
    sell_all()
elif args["ARG"][0] == "NEXT":
    course_change()
elif args["ARG"][0] == "RESTART":
    restart()

