import json
import discord
from discord.ext import commands
from pymongo import MongoClient


def bot():
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix=".", intents=intents)
    return bot


def startup():
    with open("config/startup.json") as file:
        return json.load(file)


def channels():
    with open("config/Channels.json") as file:
        return json.load(file)


def log_channel(client):
    return client.get_channel(int(channels()["log_channel_id"]))


def mongo():
    with open("config/mongodb.json") as file:
        return json.load(file)


def tempmutes():
    cluster = MongoClient(mongo()["connection_id"])
    db = cluster["Discord"]
    collection = db["tempmutes"]
    return collection
