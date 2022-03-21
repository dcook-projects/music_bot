import discord
from discord.ext import commands
import music
import config

cogs = [music]
client = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)

client.loop.create_task(music.setup(client))

client.run(config.BOT_TOKEN)