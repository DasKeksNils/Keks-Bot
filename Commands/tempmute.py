from discord.ext import commands
import time

from Moderating.Perms import errors
from Moderating.Perms import role as perms
from Database import insert_tempmute as data


def temp_cmds(bot):
    print("temps load")

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
        elif not data.is_in_db(user):
            muted_role = ctx.guild.get_role(perms.roles()["Muted"])
            await user.add_roles(muted_role)
            utc_time_sec = int(time.strftime("%Y", time.gmtime())) * 31540000 + int(time.strftime("%m", time.gmtime())) * 2628000 + int(time.strftime("%d", time.gmtime())) * 86400 + int(time.strftime("%H", time.gmtime())) * 3600 + int(time.strftime("%M", time.gmtime())) * 60 + int(time.strftime("%S", time.gmtime()))
            mute_end = int(utc_time_sec + dur_sec)
            await data.insert(user=user, mute_end=mute_end, duration=duration_or, reason=reason, mod=ctx.author, ctx=ctx)
            await ctx.send(f"{user} is now muted!")
        else:
            await ctx.send(f"{user} is already in Database!")
