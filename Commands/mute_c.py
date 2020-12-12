import discord
from discord.ext import commands
from Moderating.Perms import role as perms
from config import log
import Webhook.log_send as ch_log
from Moderating.Perms import errors


def mute_user(bot):
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