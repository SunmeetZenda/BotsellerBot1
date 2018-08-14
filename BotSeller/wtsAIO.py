import csv
import discord


kickmoji = ''
eve = ''
cyber = ''
ghost = ''
trip = ''
dashe = ''
misc = ''


#Discord Bot Made by @SunmeetZenda

#Kickmoji
with open('wtsKickmoji.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            (f'Column names are {", ".join(row)}')
            line_count += 1
        kickmoji  += (f'{row["Username"]} Wants to sell  {row["BotName"]} For the price of ${row["Price"]}.\n' )
        line_count += 1


#Eve
with open('wtsEve.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            (f'Column names are {", ".join(row)}')
            line_count += 1
        eve  += (f'{row["Username"]} Wants to sell  {row["BotName"]} For the price of {row["Price"]}.\n' )
        line_count += 1


#Cyber
with open('wtsCyber.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            (f'Column names are {", ".join(row)}')
            line_count += 1
        cyber  += (f'{row["Username"]} Wants to sell  {row["BotName"]} For the price of {row["Price"]}.\n' )
        line_count += 1


#Ghost
with open('wtsGhost.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            (f'Column names are {", ".join(row)}')
            line_count += 1
        ghost  += (f'{row["Username"]} Wants to sell  {row["BotName"]} For the price of {row["Price"]}.\n' )
        line_count += 1


#Trip
with open('wtsTrip.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            (f'Column names are {", ".join(row)}')
            line_count += 1
        trip  += (f'{row["Username"]} Wants to sell  {row["BotName"]} For the price of {row["Price"]}.\n' )
        line_count += 1


#Dashe
with open('wtsDashe.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            (f'Column names are {", ".join(row)}')
            line_count += 1
        dashe  += (f'{row["Username"]} Wants to sell  {row["BotName"]} For the price of {row["Price"]}.\n' )
        line_count += 1


#Misc
with open('wtsMisc.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            (f'Column names are {", ".join(row)}')
            line_count += 1
        misc  += (f'{row["Username"]} Wants to sell  {row["BotName"]} For the price of {row["Price"]}.\n' )
        line_count += 1




client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!wtb kickmoji'):
        msg = (kickmoji).format(message)
        await client.send_message(message.channel, msg)
   
    if message.content.startswith('!wtb eve'):
        msg = (eve).format(message)
        await client.send_message(message.channel, msg)
  
    if message.content.startswith('!wtb cyber'):
        msg = (cyber).format(message)
        await client.send_message(message.channel, msg)   

    if message.content.startswith('!wtb ghost'):
        msg = (ghost).format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('!wtb trip'):
        msg = (trip).format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('!wtb dashe'):
        msg = (dashe).format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('!wtb misc'):
        msg = (misc).format(message)
        await client.send_message(message.channel, msg)






@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('DISCORD TOKEN HERE')



