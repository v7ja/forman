from telethon import TelegramClient, sync, errors
from telethon.sessions import StringSession
from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
from datetime import datetime
from telethon import functions, types
import random, time, requests, telebot , os
R = '\033[1;31m'
y = '\033[1;33m'
G= "\033[1;92m"
chat_id = input('- Enter Id : ')
token = input('- Enter Token : ')
try:
	bot = telebot.TeleBot(token)
except:
	exit('- Trun On Vpn / Error Token Bot')
def check(client, username):
    global bot
    global chat_id
    requ = requests.get("https://fragment.com/username/" + username)
    if '<span class="tm-section-header-status tm-status-avail">Available</span>' in requ.text:
        print("UserName Available In Fragment : " + username)
        return "sale"
    time.sleep(0)
    try:
            print(G+"UserName Available : " + username)
            result = client(functions.channels.UpdateUsernameRequest(channel="يوزر قناة",username="يوزر"))
            if result:
            
        else:
            print(R+"UserName Not Available : " + username)
    except errors.FloodWaitError as timb:
        print(f'You Have Been Blocked Wait {timb.seconds}')
        time.sleep(timb.seconds)
    except errors.UsernameInvalidError:
        print(R+"Username Invalid : " + username)
    except errors.rpcbaseerrors.BadRequestError:
        print(R+"Username Banned : " + username)

def username(client):
    AB = 'qwertYuiopasdfghjklzxcvbnm'
    num = '1234567890'
    while True:
        mm = str("".join(random.choice(AB) for i in range(1)))
        nn = str("".join(random.choice(AB) for i in range(1)))
        ww = str("".join(random.choice(num) for i in range(1)))
        hh = str("".join(random.choice(AB) for i in range(1)))
        c = (mm + ww + nn + "_" + nn )
        c1 = (mm + mm + nn + "_" + nn)
        c2 = (mm + hh + mm + nn + ww)
        c3 = (mm + mm + mm + "_" + hh)
        c4 = (hh + "_" + mm + mm + mm)
        c5 = (nn  + mm + mm + "_" + mm)
        c6 = (mm + "_" + ww + hh + nn)
        c7 = (hh  + mm + ww + hh + ww)
        c8 = (mm + hh + ww + ww + ww)
        c9 = (mm + hh + ww + nn + nn)
        user = (c,c1,c2,c3,c4,c5,c6,c7,c8,c9)
        username = str("".join(random.choice(user)))
        check(client, username)
api_id = input('- Enter Api_Id : ')
api_hash = input('- Enter Api_Hash : ')
def session1():
    client = TelegramClient(StringSession(), api_id, api_hash)
    client.start()
    session = client.session.save()
    client.disconnect()
    return session
def main():
    session = session1()
    client = TelegramClient(StringSession(session), api_id, api_hash)
    try:
    	client.start()
    except:
    	exit('- Error Api_Id , Api_Hash')
    client(JoinChannelRequest('@yabhiraq'))
    os.system('clear')
    username(client)
    client.disconnect()
main()