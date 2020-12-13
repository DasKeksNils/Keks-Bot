import discord
from discord.ext import commands
from Commands.utils import download
import time


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
        def server_info(ctx):
            info_embed = discord.Embed(
                title="Server Info",
                color=discord.Colour.purple()
            )
            info_embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
            info_embed.add_field(name="Created at:", value=str(ctx.guild.created_at))
            info_embed.add_field(name="Owner:", value=str(ctx.guild.owner))
            info_embed.add_field(name="Members:", value=str(ctx.guild.member_count))
            info_embed.set_footer(text=f"Server_id: {ctx.guild.id} \n" + time.strftime("%m/%d/%Y at %H:%M", time.localtime()), icon_url=info_embed.Empty)
            return info_embed
        await ctx.send(embed=server_info(ctx))
