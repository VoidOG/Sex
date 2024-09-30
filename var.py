import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "29872536"))
    API_HASH = os.getenv("API_HASH", "65e1f714a47c0879734553dc460e98d6")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7230519531:AAF8unU6I14L_gcR4AHYxmHsVMASJj7Tbww")
    sudo = os.getenv("SUDO","6698364560 6730517246 7163357187")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
