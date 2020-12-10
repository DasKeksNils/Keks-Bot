import discord
from discord.ext import commands
from Commands.utils import download
from Moderating.Perms import role as perms
from config import log
import Webhook.log_send as ch_log
from Moderating.Perms import errors
from Webhook import Embeds


def self_commands(bot):

    @bot.command()
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
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def ban(ctx, user: discord.User, *, reason=None):
        if user is None or user == ctx.author:
            await ctx.send("This User don't exist or is yourself!")
        else:
            bans = await ctx.guild.bans()
            for BanEntry in bans:
                if BanEntry.user == user:
                    await ctx.send("User is already banned!")
                else:
                    await ctx.guild.ban(user, reason=reason)
                    log.ban(user, reason, ctx.author)
                    await ch_log.member_ban(user, reason, ctx.author)

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def ban_id(ctx, user, *, reason=None):
        user = await bot.fetch_user(int(user))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
        else:
            bans = await ctx.guild.bans()
            for BanEntry in bans:
                if BanEntry.user == user:
                    ctx.send("User is already banned")
                else:
                    await ctx.guild.ban(user, reason=reason)
                    log.ban(user, reason, ctx.author)
                    await ch_log.member_ban(user, reason, ctx.author)

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def unban(ctx, user_id):
        user = await bot.fetch_user(int(user_id))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
        else:
            bans = await ctx.guild.bans()
            for BanEntry in bans:
                if BanEntry.user == user:
                    await ctx.guild.unban(user)
                    log.unban(user)
                    await ch_log.member_unban(user)
                else:
                    await ctx.send("Not Banned")

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def kick(ctx, user: discord.User, *, reason=None):
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
        else:
            await ctx.guild.kick(user, reason=reason)
            await ch_log.member_kick(user, reason, ctx.author)
            log.kick(user, reason, ctx.author)

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def clear(ctx, number: int):
        msgs = []
        async for x in ctx.channel.history(limit=number + 1):
            msgs.append(x)
        await ctx.channel.delete_messages(msgs)
        await ctx.send(str(number) + " messages sucessfully deleted :thumbsup:")

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def clear_user(ctx, user: discord.User, *, limit: int):
        if user is None:
            await ctx.send(errors.user_not_exist())
        else:
            msgs = []
            async for x in ctx.channel.history():
                if x.author == user:
                    msgs.append(x)
                    if len(msgs) == limit:
                        break
            await ctx.channel.delete_messages(msgs)
            await ctx.send(str(limit) + f" messages from {user} sucessfully deleted :thumsup:")

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def mute(ctx, user: discord.Member, *, reason=None):
        if user is None:
            await ctx.send(errors.user_not_exist())
            return
        if await perms.is_muted(user):
            await ctx.send(f"{user} is already muted!")
        else:
            muted_role = ctx.guild.get_role(perms.roles()["Muted"])
            await user.add_roles(muted_role)
            log.mute(member=user, mod=ctx.author, reason=reason)
            await ch_log.mute(member=user, mod=ctx.author, reason=reason)
            await ctx.send(f"{user} is now muted!")

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def unmute(ctx, user: discord.Member):
        if user is None:
            await ctx.send(errors.user_not_exist())
        if await perms.is_muted(user):
            muted_role = ctx.guild.get_role(perms.roles()["Muted"])
            await user.remove_roles(muted_role)
            log.unmute(member=user, mod=ctx.author)
            await ch_log.unmute(member=user, mod=ctx.author)
            await ctx.send(f"{user} is now unmuted!")
        else:
            await ctx.send(f"{user} is not muted!")

    @bot.command()
    @commands.has_any_role("Admin")
    async def shutdown(ctx):
        await ctx.message.add_reaction("<:PepeOkay:779775701528215553>")
        await bot.close()
        log.shutdown(ctx)

    @bot.command()
    @commands.cooldown(1, 30, commands.BucketType.guild)
    async def serverinfo(ctx):
        await ctx.send(embed=Embeds.server_info(ctx))

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def addrole(ctx, user: discord.Member, role: discord.Role):
        if role in user.roles:
            ctx.send("This user has this role already.")
        else:
            await user.add_roles(role)
            await ctx.message.add_reaction("<:PepeOkay:779775701528215553>")

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def removerole(ctx, user: discord.Member, role: discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.message.add_reaction("<:PepeOkay:779775701528215553>")
        else:
            ctx.send("This user don't has this role.")
