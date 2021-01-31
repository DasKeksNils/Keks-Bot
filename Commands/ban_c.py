from discord.ext import commands
from config import log
import Webhook.log_send as ch_log
from Moderating.Perms import errors
from config.config import bans
from Database import history


def ban_commands(bot):

    def get_ban_ids():
        mute_ids = bans().find({"_id": 0})
        for re in mute_ids:
            return re["ban_id"]

    def is_in_db(user):
        return bans().find_one({"user_id": user.id})

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def kick(ctx, user_or, *, reason=None):
        try:
            user = await bot.fetch_user(int(user_or))
        except ValueError:
            user = await bot.fetch_user(int(user_or[3:len(user_or) - 1]))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
        else:
            ban_id = get_ban_ids() + 1
            await ctx.guild.kick(user, reason=reason)
            await ch_log.member_kick(user, reason, ctx.author)
            log.kick(user, reason, ctx.author)
            history.kick(member=user, ban_id=ban_id, reason=reason, guild_id=ctx.guild.id)

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def ban(ctx, user_or, *, reason=None):
        user = await bot.fetch_user(int(user_or[3:len(user_or) - 1]))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
        else:
            guild_bans = await ctx.guild.bans()
            if bans:
                for BanEntry in guild_bans:
                    if BanEntry.user == user:
                        ctx.send("User is already banned")
                        return
            if not is_in_db(user):
                ban_id = get_ban_ids() + 1
                bans().insert({
                    "mute_id": ban_id,
                    "type": "Ban",
                    "name": user.name,
                    "user_id": user.id,
                    "reason": reason,
                    "guild_id": ctx.guild.id
                })
                bans().update_one({"_id": 0}, {"$set": {"ban_id": ban_id}})
                history.ban(member=user, reason=reason, ban_id=ban_id, guild_id=ctx.guild.id)
                await ctx.guild.ban(user, reason=reason)
                log.ban(user, reason, ctx.author)
                await ch_log.member_ban(user, reason, ctx.author)
            else:
                ctx.send("User is not in Database")

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def unban(ctx, user_id):
        user = await bot.fetch_user(int(user_id))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
        else:
            guild_bans = await ctx.guild.bans()
            for BanEntry in guild_bans:
                if BanEntry.user == user:
                    break
                else:
                    await ctx.send("Not Banned")
                    return
        if is_in_db(user):
            bans().find_one_and_delete({"user_id": user.id})
            await ctx.guild.unban(user)
            log.unban(user)
        else:
            ctx.send("User is not in Database")
