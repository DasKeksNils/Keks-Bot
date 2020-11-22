import discord
from discord.ext import commands
from lib import download as lib
from Moderating.Perms import role as perms
from config import log
import Webhook.log_send as ch_log


def self_commands(bot):

    @bot.command()
    async def ping(ctx):
        await ctx.send(f"{round(bot.latency * 1000 , 0)} ms")

    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cat(ctx):
        lib.download("https://thiscatdoesnotexist.com/")
        await ctx.send(file=discord.File("picture.jpg"))

    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def horse(ctx):
        lib.download("https://thishorsedoesnotexist.com/")
        await ctx.send(file=discord.File("picture.jpg"))

    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def boom(ctx):  # use inspect at tenor.com
        await ctx.send("https://media1.tenor.com/images/8909c612b5bb6264cad4b13366d24693/tenor.gif?itemid=19249577")

    @bot.command()
    @perms.is_mod()
    async def ban(ctx, user: discord.User, *, reason=None):
        if user is None or user == ctx.author:
            await ctx.send("This User don't exist or is yourself!")
        else:
            await user.send(f"You got banned from {ctx.guild} because of {reason}.")
            await ctx.guild.ban(user, reason=reason)
            log.ban(user, reason, ctx.author)
            await ch_log.member_ban(user, reason, ctx.author)

    @bot.command()
    @perms.is_mod()
    async def ban_id(ctx, user, *, reason=None):
        user = await bot.fetch_user(int(user))
        if user is None or user == ctx.author:
            await ctx.send("This User don't exist or is yourself!")
        else:
            await user.send(f"You got banned from {ctx.guild} because of {reason}.")
            await ctx.guild.ban(user, reason=reason)
            log.ban(user, reason, ctx.author)
            await ch_log.member_ban(user, reason, ctx.author)

    @bot.command()
    @perms.is_mod()
    async def unban(ctx, user_id):
        user = await bot.fetch_user(int(user_id))
        if user is None or user == ctx.author:
            await ctx.send("This user don't exist or is yourself!")
        else:
            await ctx.guild.unban(user)
            log.unban(user)
            await ch_log.member_unban(user)

    @bot.command()
    @perms.is_mod()
    async def kick(ctx, user: discord.User, *, reason=None):
        if user is None or user == ctx.author:
            await ctx.send("This user don't exist or is yourself!")
        else:
            await ctx.guild.kick(user, reason=reason)
            await ch_log.member_kick(user, reason, ctx.author)
            log.kick(user, reason, ctx.author)

    @bot.command()
    @perms.is_mod()
    async def clear(ctx, number: int):
        msgs = []
        async for x in ctx.channel.history(limit=number + 1):
            msgs.append(x)
        await ctx.channel.delete_messages(msgs)
        await ctx.send(str(len(msgs)) + " messages sucessfully deleted :thumbsup:")
