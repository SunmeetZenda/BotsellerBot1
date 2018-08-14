import discord
import csv


client = discord.Client()

filename= ("wtsKickmoji.csv")
f= open(filename,"a")

#f.write(userInput+'\n')

@client.event
async def on_message(message):
    if message.content.startswith("!id"):
         await Bot.send_message(message.channel, 'yes')


userInput= (message.content[3:])









client.run('NDc4NjQzMTQ0ODI1NzY1OTE1.DlO6iw.VxsHj4E3k-gE6zseijGMb8sMq_c')

