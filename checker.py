import requests
import random
import json
from threading import Thread
import urllib.request
import ctypes
from bs4 import BeautifulSoup
from dhooks import Webhook, Embed

webhook = Webhook('')
send_webhook = True
checkednumber = 0
workingnumber = 0

def threadlol(id):
    global checkednumber
    global workingnumber
    for x in range(199999):
        #length = 6
        #id = ''.join(random.choice(str("qwertyuopiasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890")) for i in range(length))
        urllol = f"https://discord.gg/{id}"
        r = requests.get(f"{urllol}")
        soup = BeautifulSoup(r.text, "html.parser")
        owotext = soup.find("meta",  property="og:url")
        owodesc = soup.find("meta",  property="og:description")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Amy Discord Invite Checker - Checked:{checkednumber} - Hit:{workingnumber}")
        if owotext:
            print(owotext["content"])
            invitee = owotext["content"]
            descriptionn = owodesc["content"]
            loljsondump = json.dumps(owodesc["content"])
            loljsonload = json.loads(loljsondump).split()
            if "members" in loljsonload:
                index = loljsonload.index("members")
                print(loljsonload[index-2])
                if send_webhook is True:
                    embed = Embed(
                    title=f"Amy Discord Invite Checker!",
                    description=f"Working Invite Found!",
                    color = 0x51c240,
                    timestamp='now'
                    )

                    embed.set_author(name='Click here to join server.', url=f"{invitee}")
                    embed.add_field(name=f"Invite:", value=f"**{invitee}**", inline=False)
                    embed.add_field(name=f"Members:", value=f"**{loljsonload[index-2]}**")
                    embed.set_footer("Made By Amy#1000", icon_url="https://cdn.discordapp.com/attachments/537166305342652437/649648400433807361/Alther_logo_smallx2.jpg")
                    webhook.send(embed=embed)
                    workingnumber += 1
                    return False, loljsonload[index-2]
            elif "other" in loljsonload:
                    index = loljsonload.index("other")
                    print(loljsonload)
                    if send_webhook is True:
                        embed = Embed(
                        title=f"Amy Discord Invite Checker!",
                        description=f"Working Invite Found!",
                        color = 0x51c240,
                        timestamp='now'
                        )

                        embed.set_author(name='Click here to join server.', url=f"{invitee}")
                        embed.add_field(name=f"Invite:", value=f"**{invitee}**", inline=False)
                        embed.add_field(name=f"Members:", value=f"**{loljsonload[index-1]}**")
                        embed.set_footer("Made By Amy#1000", icon_url="https://cdn.discordapp.com/attachments/537166305342652437/649648400433807361/Alther_logo_smallx2.jpg")
                        webhook.send(embed=embed)
                        workingnumber += 1
                        return False, loljsonload[index-1]
        else:
            print(f"Not Working - {id}")
            checkednumber += 1
            return True, None

for i in range(1):
    Thread(target=threadlol).start()

with open("user.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        username = line.strip()
        status, jsonlolok = threadlol(username)
        if not status:
            print("%s" % username)
            file = open("output.txt","a")
            file.write("https://discord.gg/" + username + " - [" + jsonlolok + "]" "\n")
            file.close()
