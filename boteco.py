import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l-accesso come {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('geopop#1'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=Q-cutQgHc00&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C'
        await message.channel.send(video_url)

    elif message.content.startswith('geopop#2'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=WALo6GLp_to&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=2'
        await message.channel.send(video_url)

    elif message.content.startswith('geopop#3'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=nIWDMpSU6iI&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=3'
        await message.channel.send(video_url)
    
    elif message.content.startswith('geopop#4'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=QTAlsSdNvV8&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=4'
        await message.channel.send(video_url)
    elif message.content.startswith('geopop#5'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=QJNBtzPshVU&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=5'
        await message.channel.send(video_url)

    elif message.content.startswith('geopop#6'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=AFEMHZioqJU&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=6'
        await message.channel.send(video_url)
    
    elif message.content.startswith('geopop#7'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=BRjXSv3FU0w&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=7'
        await message.channel.send(video_url)

    elif message.content.startswith('geopop#8'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=XAaXVF-9QeM&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=8'
        await message.channel.send(video_url)
    
    elif message.content.startswith('geopop#9'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=QSQa1bZ_hGQ&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=9'
        await message.channel.send(video_url)
    elif message.content.startswith('geopop#10'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=45OlPkURlus&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=10'
        await message.channel.send(video_url)

    elif message.content.startswith('geopop#11'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://www.youtube.com/watch?v=WJAIhXdagvE&list=PL8AiOx5ykoROctdEiGTGG-eCJGMRcro0C&index=11'
        await message.channel.send(video_url)
    elif message.content.startswith('raccolta differenziata'):
        await message.channel.send("stai per vedere una lezione di Geopop sul riciclo")
        video_url = 'https://youtu.be/mDpK_MNOg94'
        await message.channel.send(video_url)


# Inserisci il tuo token del bot Discord qui x your token goes there
client.run('')
