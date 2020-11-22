from discord.ext import commands
import json
from config import config
with open("Moderating/Perms/roles.json") as file:
    roles = json.load(file)

bot = config.bot()


def is_mod():
    async def mod(ctx):
        admin_role = ctx.guild.get_role(roles["Admin"])
        dev_role = ctx.guild.get_role(roles["Dev"])
        mod_role = ctx.guild.get_role(roles["Mod"])
        if admin_role in ctx.author.roles or dev_role in ctx.author.roles or mod_role in ctx.author.roles:
            return True
        else:
            return False
    return commands.check(mod)


def is_dev():
    async def dev(ctx):
        admin_role = ctx.guild.get_role(roles["Admin"])
        dev_role = ctx.guild.get_role(roles["Dev"])
        if admin_role in ctx.author.roles or dev_role in ctx.author.roles:
            return True
        else:
            return False
    return commands.check(dev)


def is_adim():
    async def admin(ctx):
        admin_role = ctx.guild.get_role(roles["Admin"])
        if admin_role in ctx.author.roles:
            return True
        else:
            return False
    commands.check(admin)
