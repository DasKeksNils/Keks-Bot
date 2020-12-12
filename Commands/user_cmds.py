import discord
from discord.ext import commands
from Commands.utils import download
from Webhook import Embeds


def user_commands(bot):
    @bot.command()
    @commands.cooldown(5, 30, commands.BucketType.guild)
    async def ping(ctx):
        await ctx.send(f"ping <:FeelsDonkMan:780075218433212426>\n{round(bot.latency * 1000 , 0)} ms")

    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cat(ctx):
        download.download("https://thiscatdoesnotexist.com/")
        await ctx.send(file=discord.File("picture.jpg"))

    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def horse(ctx):
        download.download("https://thishorsedoesnotexist.com/")
        await ctx.send(file=discord.File("picture.jpg"))

    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def boom(ctx):  # use inspect at tenor.com
        await ctx.send("https://media1.tenor.com/images/8909c612b5bb6264cad4b13366d24693/tenor.gif?itemid=19249577")

    @bot.command()
    @commands.cooldown(1, 30, commands.BucketType.guild)
    async def serverinfo(ctx):
        await ctx.send(embed=Embeds.server_info(ctx))
