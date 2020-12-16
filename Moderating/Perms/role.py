import discord
import json
from config import config

bot = config.bot()


def get_role(role, ctx):
    return discord.utils.get(ctx.guild.roles, name=role)


def roles():
    with open("Moderating/Perms/roles.json") as file:
        return json.load(file)


async def is_muted(user):
    return get_role(role="Muted", ctx=user) in user.roles


def list_roles(user):
    roles_str = ""
    for role in user.roles:
        if not role == get_role(role="@everyone", ctx=user):
            roles_str = roles_str + f"{role}, "
    return roles_str[0:len(roles_str) - 2]
