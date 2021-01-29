import time
import json
from pymongo import MongoClient
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import logging as log


import discord
from discord.ext import commands

log.basicConfig(filename="log.log", level=log.INFO)


def startup():
    with open("./config/startup.json") as file:
        return json.load(file)


def mongo():
    with open("./config/mongodb.json") as file:
        return json.load(file)


def db():
    cluster = MongoClient(mongo()["connection_id"])
    data = cluster["Discord"]
    collection = data["Mutes"]
    return collection


def utc_sec():
    return int(time.strftime("%Y", time.gmtime())) * 31540000 + int(time.strftime("%m", time.gmtime())) * 2628000 + int(time.strftime("%d", time.gmtime())) * 86400 + int(time.strftime("%H", time.gmtime())) * 3600 + int(time.strftime("%M", time.gmtime())) * 60 + int(time.strftime("%S", time.gmtime()))


def timestamp():
    return str(time.strftime(" [%m/%d/%Y | %H:%M:%S] ", time.localtime()))


async def unmute(member, mod, mute_id, reason, totype):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=unmute_emb(member=member, mod=mod, mute_id=mute_id, reason=reason, totype=totype))


def log_unmute(member, mod):
    log.info(timestamp() + f"[UNMUTE] {member} ({member.id}) was unmuted by {mod} ({mod.id})")


def unmute_emb(member, mod, mute_id, reason, totype):
    unmute_embed = discord.Embed(
        title="Member unmuted",
        color=discord.Colour.green()
    )
    unmute_embed.add_field(name="Moderator", value=mod)
    unmute_embed.add_field(name="Mute_id", value=mute_id)
    unmute_embed.add_field(name="Type", value=totype)
    unmute_embed.add_field(name="reason", value=reason)
    unmute_embed.set_author(name=member.name, icon_url=member.avatar_url)
    unmute_embed.set_footer(text=f"{member.id} \n " + timestamp(), icon_url=unmute_embed.Empty)
    return unmute_embed


async def unmute_loop(bot):
    print("Thread start")

    while True:
        print("new loop")
        time.sleep(10)
        db_users = db().find({"type": "Tempmute"})
        for i in db_users:
            mute_end = i["mute_end"]
            if int(mute_end) - utc_sec() < 0:
                totype = "Tempmute"
                mute_id = i["mute_id"]
                reason = i["reason"]
                user_id = i["user_id"]
                guild_id = i["guild_id"]

                guild = await bot.fetch_guild(int(guild_id))
                user = await guild.fetch_member(int(user_id))
                await user.remove_roles(discord.utils.get(guild.roles, name="Muted"))
                db().find_one_and_delete({"user_id": user.id})
                await unmute(member=user, mod=bot.user, mute_id=f"#{mute_id}", reason=reason, totype=totype)
                log_unmute(member=user, mod=bot.user)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print("start")
    await unmute_loop(bot)


@bot.event
async def on_command_error():
    return


bot.run(startup()["token"])  # this will run with the same token and will start ca. 15 secs after the main bot
