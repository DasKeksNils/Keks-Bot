import discord
from discord.ext import commands


def roles(bot):
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
