from unicodedata import name
import telethon
import asyncio
import os, sys
import re
from random import *
import requests
from telethon import TelegramClient, events
from telegraph_api import Telegraph
from datetime import datetime
import random
from telethon.tl.custom import Button
import json


from defs import getUrl, getcards, phone
ID =  27531588
HASH = '349a20a388db2e8f1cdad15fada4b4b0'
SEND_CHAT = '@ArmaniBinner'

client = TelegramClient('session', ID, HASH)
ccs = []

chats  = ['https://t.me/JennaScrap']
            

with open('cards.txt', 'r') as r:
    temp_cards = r.read().splitlines()


for x in temp_cards:
    car = getcards(x)
    if car:
        ccs.append(car[0])
    else:
        continue
    
@client.on(events.NewMessage(chats=chats, func = lambda x: getattr(x, 'text')))
async def my_event_handler(m):
    if m.reply_markup:
        text = m.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = m.text
    cards = getcards(text)
    if not cards:
        return
    cc,mes,ano,cvv = cards
    if cc in ccs:
        return
    ccs.append(cc)
    apibinlist = json.loads(requests.get("https://lookup.binlist.net/"+cc).text)
    binEmoji = apibinlist["country"]["emoji"]
    binName = apibinlist["country"]["name"]
    binType = apibinlist["type"]
    binBank = apibinlist["bank"]["name"]
    #if not bin:
        #return
    
    #bin_json =  bin.json()
    extra = cc[0:0 + 12]
    fullinfo = f"{cc}|{mes}|{ano}|{cvv}"
    images = ["https://telegra.ph/file/ded3024390a2ef2589316.jpg", "https://telegra.ph/file/1feccaa71b944a09a2a0c.jpg", "https://telegra.ph/file/ba6f75f6fe36feeeff6cb.jpg"]
    image = random.choice(images)
    telegraph = Telegraph()
    await telegraph.create_account("Scrapper Free Db", author_name="The Dumxh")

    new_page = await telegraph.create_page(
        "Nigth Scrapper",
        content_html = f"<p>[+] 🎀𝗖𝗖 𝗦𝗖𝗔𝗥𝗔𝗣𝗣𝗘𝗥 𝗦𝗣𝗔𝗠🎀 \n——————————————————\n[+] Credit Card: {cc}|{mes}|{ano}|{cvv}\n——————————————————\n Extra: {extra}xxxx|{mes}|{ano}|xxx\n——————————————————\n[+] Scrapper By: @l_lI_X</p>"
    )
    text = f"""

** 💗✨𝙎𝙋𝘼𝙈𝙄𝙉𝙂 𝘾𝘾✨💗**

∆∆-∆∆-∆∆-∆∆-∆∆-∆∆-∆

**🎀𝗖𝗥𝗘𝗗𝗜𝗧 𝗖𝗔𝗥𝗗✘ 

✘ {fullinfo} ✘**

✘✘✘✘✘✘✘✘✘✘✘✘✘✘

🎀𝗕𝗔𝗡𝗞 ✘ {binBank} 

🎀𝗖𝗢𝗨𝗡𝗧𝗥𝗬 ✘ {binName}-{binEmoji}

🎀𝗖𝗖 𝗧𝗬𝗣𝗘 ✘ {binType}

✘✘✘✘✘✘✘✘✘✘✘✘✘✘

**🎀𝗘𝘅𝘁𝗿𝗮 ✘ 
⤷[```{extra}xxxx|{mes}|{ano}|xxx```]

🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀
**[🔥𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗥𝗘🔥| @l_lI_X ✘ @F_C_1_6 ]**
**[✨💗 𝗰𝗵𝗮𝗻 💗✨| @CRKSOO_CC ✘
"""   
    print(f'{cc}|{mes}|{ano}|{cvv}')
    with open('cards.txt', 'a') as w:
        w.write(fullinfo + '\n')

    await client.send_message(SEND_CHAT, text)

client.start()
client.run_until_disconnected()