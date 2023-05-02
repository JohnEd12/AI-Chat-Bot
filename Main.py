import discord
import os
from dotenv import load_dotenv
from nueralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Clent()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.autho == client.user:
        return
    if message.content.startswith("$aibot"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)


client.run(TOKEN)
