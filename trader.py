from argparse import ArgumentParser
from utils import *
from utils_2 import *

args = ArgumentParser()

args.add_argument("ARG", default=None, nargs="+")
args.add_argument("BUY", nargs="?", default=None)
args.add_argument("SELL", nargs="?", default=None)
args.add_argument("BUY ALL", type=list, nargs="?", default=None)
args.add_argument("SELL ALL", type=list, nargs="?", default=None)
args.add_argument("RATE", type=str, nargs="?", default=None)
args.add_argument("AVAILABLE", type=str, nargs="?", default=None)
args.add_argument("NEXT", type=str, nargs="?", default=None)
args.add_argument("RESTART", type=str, nargs="?", default=None)

args = vars(args.parse_args())


if args["ARG"][0] == "AVAILABLE":
    print(available(data))
elif args["ARG"][0] == "RATE":
    print(rate(data))
elif args["ARG"][0] == "BUY" and "".join(args["ARG"][1]).isdigit():
    args["BUY"] = args["ARG"][1]
    buy_usd = float(args["BUY"])
elif args["ARG"][0] == "SELL" and "".join(args["ARG"][1]).isdigit():
    args["SELL"] = args["ARG"][1]
    sell_usd = float(args["SELL"])
elif args["ARG"][0] == "BUY" and args["ARG"][1] == "ALL":
    args["BUY ALL"] = True
elif args["ARG"][0] == "SELL" and args["ARG"][1] == "ALL":
    args["SELL ALL"] = True
elif args["ARG"][0] == "NEXT":
    args["NEXT"] = True
elif args["ARG"][0] == "RESTART":
    args["RESTART"] = True
