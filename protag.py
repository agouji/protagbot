import discord
import asyncio
import random

client = discord.Client()

def poem():
    with open("sayori.txt", "r") as words:
        sayori = []
        for ele in words.read().split():
            sayori.append(ele)

    with open("yuri.txt", "r") as words:
        yuri = []
        for ele in words.read().split():
            yuri.append(ele)

    with open("natuki.txt", "r") as words:
        natuki = []
        for ele in words.read().split():
            natuki.append(ele)

    poem = []

    x = 0
    sayoscore = 0
    yuriscore = 0
    natukiscore = 0
    corrupt = 0

    while x < 20:
        picker = random.randint(0, 64)
        if picker >= 43:
            poem.append(sayori[random.randint(0, len(sayori) - 1)])
            sayoscore += 1
        elif picker >= 22:
            poem.append(yuri[random.randint(0, len(yuri) - 1)])
            yuriscore += 1
        elif picker >= 1:
            poem.append(natuki[random.randint(0, len(natuki) - 1)])
            natukiscore += 1
        else:
            monika = "moniE"
            for i in range(255):
                monika += chr(random.randint(160, 255))
            return monika
            corrupt += 1
            break
        x += 1

    if corrupt == 0:

        if natukiscore >= sayoscore and natukiscore >= yuriscore:
            win = "Natsuki"
        elif sayoscore >= yuriscore:
            win = "Sayori"
        else:
            win = "Yuri"

        print ("Natsuki: %s Sayori: %s Yuri: %s" % (natukiscore, sayoscore, yuriscore))
        stanz1 = ("%s " % poem[1].capitalize())
        for word in poem[2:5]:
            stanz1 += ("%s " % word)
        stanz1 += ("%s.\n" % poem[5])

        stanz2 = ("%s " % poem[6].capitalize())
        for word in poem[7:8]:
            stanz2 += ("%s " % word)
        stanz2 += ("%s.\n" % poem[8])

        stanz3 = ("%s " % poem[9].capitalize())
        for word in poem[10:11]:
            stanz3 += ("%s " % word)
        stanz3 += ("%s.\n" % poem[11])

        stanz4 = ("%s " % poem[12].capitalize())
        for word in poem[13:15]:
            stanz4 += ("%s " % word)
        stanz4 += ("%s.\n" % poem[15])

        stanz5 = ("%s " % poem[16].capitalize())
        for word in poem[17:19]:
            stanz5 += ("%s " % word)
        stanz5 += ("%s.\n" % poem[19])

        comp = "```\n%s\n```" % (poem[0].capitalize() + "\n\n" + stanz1 + stanz2 +stanz3 + stanz4 + stanz5) + '\n' + "%s will like this poem the most." % win

        return comp

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Pong!')
    elif message.content.startswith('!poem'):
       await client.send_message(message.channel, poem())

token = raw_input('Insert Token: )    
client.run('token')
