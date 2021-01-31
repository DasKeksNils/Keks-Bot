from config import config
from Events.events import message_events
from Commands import Index

import discord
from discord.ext import commands

import subprocess
import os
import signal
import time

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


message_events(bot)
Index.self_commands(bot)


# subprocess.call("start Database/unmute_temps.py", shell=True)  # change shell=False for no console
proc = subprocess.Popen("start Database/unmute_temps.py", stdout=subprocess.PIPE, shell=True)


bot.run(config.startup()["token"])


# TODO: Word Blacklist
# TODO: Mongodb tempmute change
