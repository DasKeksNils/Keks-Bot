import discord
from discord.ext import commands
from Moderating.Perms import errors


def muting(bot):
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