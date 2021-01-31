from discord.ext import commands
import time

from Moderating.Perms import errors
from Moderating.Perms import role as perms
from config.config import mutes
from config import log
import Webhook.log_send as ch_log
from Database import history


def temp_cmds(bot):

    def get_mute_ids():
        mute_ids = mutes().find({"_id": 0})
        for re in mute_ids:
            return re["mute_id"]

    def is_in_db(user):
        return mutes().find_one({"user_id": user.id})

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def tempmute(ctx, user_or, duration_or, reason=None):
        try:
            user = await ctx.guild.fetch_member(int(user_or))
        except ValueError:
            user = await ctx.guild.fetch_member(int(user_or[3:len(user_or) - 1]))
        if user is None or user == ctx.author:
            await ctx.send(errors.user_not_exist())
            return
        if reason is None:
            reason = "None"
        dur1 = duration_or[len(duration_or)-1:len(duration_or)]  # format: s;m;h;d;y
        dur = duration_or[0:len(duration_or)-1]
        if dur1 == "s":
            dur_sec = int(dur)
        elif dur1 == "m":
            dur_sec = int(dur) * 60
        elif dur1 == "h":
            dur_sec = int(dur) * 3600
        elif dur1 == "d":
            dur_sec = int(dur) * 86400
        elif dur1 == "y":
            dur_sec = int(dur) * 31540000
        else:
            await ctx.send("Format Error")
            return
        if await perms.is_muted(user):
            await ctx.send(f"{user} is already muted!")
        elif not is_in_db(user):
            muted_role = ctx.guild.get_role(perms.roles()["Muted"])
            await user.add_roles(muted_role)
            utc_time_sec = int(time.strftime("%Y", time.gmtime())) * 31540000 + int(time.strftime("%m", time.gmtime())) * 2628000 + int(time.strftime("%d", time.gmtime())) * 86400 + int(time.strftime("%H", time.gmtime())) * 3600 + int(time.strftime("%M", time.gmtime())) * 60 + int(time.strftime("%S", time.gmtime()))
            mute_end = int(utc_time_sec + dur_sec)
            duration = duration_or
            mute_id = get_mute_ids() + 1
            mutes().insert({
                "mute_id": mute_id,
                "type": "Tempmute",
                "name": user.name,
                "user_id": user.id,
                "duration": duration,
                "mute_end": mute_end,
                "reason": reason,
                "guild_id": ctx.guild.id
            })
            mutes().update_one({"_id": 0}, {"$set": {"mute_id": mute_id}})
            await ch_log.tempmute(member=user, mod=ctx.author, reason=reason, mute_id=f"#{mute_id}", duration=duration)
            log.tempmute(member=user, mod=ctx.author, reason=reason, duration=duration, mute_id=mute_id)
            history.tempmute(member=user, reason=reason, mute_id=mute_id, guild_id=ctx.guild.id, duration=duration)
            await ctx.send(f"{user} is now muted!")
        else:
            await ctx.send(f"{user} is already in Database!")
