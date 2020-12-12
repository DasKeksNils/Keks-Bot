from discord.ext import commands
from config import log
import Webhook.log_send as ch_log
from Moderating.Perms import errors


def ban_commands(bot):

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def kick(ctx, user_or, *, reason=None):
        try:
            user = await bot.fetch_user(int(user_or))
        except:
            user = await bot.fetch_user(int(user_or[3:len(user_or) - 1]))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
        else:
            await ctx.guild.kick(user, reason=reason)
            await ch_log.member_kick(user, reason, ctx.author)
            log.kick(user, reason, ctx.author)

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def ban(ctx, user_or, *, reason=None):
        try:
            user = await bot.fetch_user(int(user_or))
        except:
            user = await bot.fetch_user(int(user_or[3:len(user_or) - 1]))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
        else:
            bans = await ctx.guild.bans()
            if bans:
                for BanEntry in bans:
                    if BanEntry.user == user:
                        ctx.send("User is already banned")
                        return
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
                    break
                else:
                    await ctx.send("Not Banned")
                    return
        await ctx.guild.unban(user)
        log.unban(user)
        await ch_log.member_unban(user)
