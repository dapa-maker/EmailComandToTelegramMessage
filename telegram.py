from dotenv import load_dotenv, dotenv_values
import os
import requests



def sendMessage(msg):
    load_dotenv()
    tele_auth = os.getenv("TELE_AUTH")
    chat_id = os.getenv("CHAT_ID")
    msg_api = "https://api.telegram.org/bot"+tele_auth+"/sendMessage?chat_id="+chat_id+"&text="+msg
    requests.get(msg_api)

