from config import config
from Events.events import message_events
from Commands import Index

import discord
from discord.ext import commands
import subprocess

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


print("ms1")
message_events(bot)
print("ms2")
Index.self_commands(bot)
print("ms3")


subprocess.call("start Database/unmute_temps.py", shell=True)  # change shell=False for no console


bot.run(config.startup()["token"])


# TODO: Word Blacklist
# TODO: Mongodb tempmute change
