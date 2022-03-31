import discord
import os
import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("ONLINE"))

keep_alive.keep_alive()
client.run(os.getenv("OTU1MDkxNzk3ODc1NTAzMTQ0.YjcojQ.v2NkWmcxE_T5La1qmg9eMwymGlI"), bot=False)
