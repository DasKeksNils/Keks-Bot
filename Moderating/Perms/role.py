from discord.ext import commands
import json
from config import config

bot = config.bot()


def admin_role(ctx):
    admin = ctx.guild.get_role(roles()["Admin"])
    return admin


def mod_role(ctx):
    mod = ctx.guild.get_role(roles()["Mod"])
    return mod


def muted_role(ctx):
    mute = ctx.guild.get_role(roles()["Muted"])
    return mute


def dev_role(ctx):
    dev = ctx.guild.get_role(roles()["Dev"])
    return dev


def roles():
    with open("Moderating/Perms/roles.json") as file:
        roles_json = json.load(file)
        return roles_json


def is_mod():
    async def mod(ctx):
        admin_role(ctx)
        dev_role(ctx)
        mod_role(ctx)
        if admin_role in ctx.author.roles or dev_role in ctx.author.roles or mod_role in ctx.author.roles:
            return True
        else:
            return False
    return commands.check(mod)


def is_dev():
    async def dev(ctx):
        admin_role(ctx)
        dev_role(ctx)
        if admin_role in ctx.author.roles or dev_role in ctx.author.roles:
            return True
        else:
            return False
    return commands.check(dev)


def is_adim():
    async def admin(ctx):
        admin_role(ctx)
        if admin_role in ctx.author.roles:
            return True
        else:
            return False
    commands.check(admin)


async def is_muted(ctx, user):
    muted_role(ctx)
    if muted_role in user.roles:
        return True
    else:
        return False
