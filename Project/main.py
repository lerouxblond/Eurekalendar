import os
import discord
import datetime
import logging
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
LOG_PATH = os.getenv("LOG_PATH")
handler = logging.FileHandler(filename=LOG_PATH, encoding="utf-8", mode="w")

class EurekaBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['task']:
            await self.load_extension(f"cogs.{extension}")



intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = EurekaBot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Eurekalendar bot is connected as {bot.user}")


bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)