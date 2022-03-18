import discord
from discord.ext import commands
import music
import config

cogs = [music]
client = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)

"""
@client.event
async def on_voice_state_update(member, before, after):
    voice_state = member.guild.voice_client
    if voice_state is None:
        return

    if len(voice_state.channel.members) == 1:
        await voice_state.disconnect()
"""

"""
async for i in range(len(cogs)):
    await cogs[i].setup(client)
"""

client.loop.create_task(music.setup(client))

client.run(config.BOT_TOKEN)