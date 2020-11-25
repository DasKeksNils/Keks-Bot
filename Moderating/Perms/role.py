import discord
import json
from config import config

bot = config.bot()


def get_role(role, ctx):
    r = discord.utils.get(ctx.guild.roles, name=role)
    return r


def roles():
    with open("Moderating/Perms/roles.json") as file:
        roles_json = json.load(file)
        return roles_json


async def is_muted(user):
    if get_role(role="Muted", ctx=user) in user.roles:
        return True
    else:
        return False
