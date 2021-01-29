from discord.ext import commands
from Moderating.Perms import role as perms
from config import log
import Webhook.log_send as ch_log
from Moderating.Perms import errors
from config.config import tempmutes
from Database import insert_tempmute as data


def get_ban_ids():
    ban_ids = tempmutes().find({"_id": 0})
    for re in ban_ids:
        return re["ban_id"]


def mute_user(bot):
    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def mute(ctx, user_or, *, reason=None):
        try:
            user = await ctx.guild.fetch_member(int(user_or))
        except ValueError:
            user = await ctx.guild.fetch_member(int(user_or[3:len(user_or) - 1]))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
            return
        if await perms.is_muted(user):
            await ctx.send(f"{user} is already muted!")
        elif not data.is_in_db(user):
            muted_role = ctx.guild.get_role(perms.roles()["Muted"])
            await user.add_roles(muted_role)
            ban_ids = get_ban_ids()
            tempmutes().insert({
                "ban_id": ban_ids + 1,
                "type": "Mute",
                "name": user.name,
                "user_id": user.id,
                "reason": reason,
                "guild_id": ctx.guild.id
            })
            tempmutes().update_one({"_id": 0}, {"$set": {"ban_id": ban_ids + 1}})

            log.mute(member=user, mod=ctx.author, reason=reason, ban_id=ban_ids + 1)
            await ch_log.mute(member=user, mod=ctx.author, reason=reason, ban_id=ban_ids + 1)
            await ctx.send(f"{user} is now muted!")
        else:
            await ctx.send(f"{user} already in Database")

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def unmute(ctx, user_or):
        try:
            user = await ctx.guild.fetch_member(int(user_or))
        except ValueError:
            user = await ctx.guild.fetch_member(int(user_or[3:len(user_or) - 1]))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
            return
        if await perms.is_muted(user):
            muted_role = ctx.guild.get_role(perms.roles()["Muted"])
            await user.remove_roles(muted_role)
            log.unmute(member=user, mod=ctx.author)

            dbuser = tempmutes().find({"user_id": user.id})
            for i in dbuser:
                totype = i["type"]
                ban_id = i["ban_id"]
                reason = i["reason"]
            tempmutes().find_one_and_delete({"user_id": user.id})
            await ch_log.unmute(member=user, mod=ctx.author, ban_id="#" + str(ban_id), reason=reason, totype=totype)
            await ctx.send(f"{user} is now unmuted!")
        else:
            await ctx.send(f"{user} is not muted!")
