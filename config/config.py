import json
import discord
from discord.ext import commands


def bot():
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix=".", intents=intents)
    return bot


def startup():
    with open("config/startup.json") as file:
        startup = json.load(file)
    return startup


def channels():
    with open("config/Channels.json") as file:
        channels = json.load(file)
    return channels


def log_channel(client):
    log_ch = client.get_channel(int(channels()["log_channel_id"]))
    return log_ch

