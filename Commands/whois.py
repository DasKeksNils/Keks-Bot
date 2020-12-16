import discord
from discord.ext import commands
import time
from Moderating.Perms import role


def command(bot):

    @bot.command()
    @commands.has_any_role("Admin", "Dev", "Moderator")
    async def whois(ctx, user_or=None):
        if user_or is None:
            user = ctx.author
        else:
            try:
                user = ctx.guild.get_member(int(user_or))
            except ValueError:
                user = ctx.guild.get_member(int(user_or[3:len(user_or) - 1]))

        embed = discord.Embed(
            title=f"Who is {user}",
            color=discord.Colour.dark_purple()
        )
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_footer(text=f"{user.id} \n" + time.strftime("%m/%d/%Y at %H:%M", time.localtime()), icon_url=embed.Empty)
        embed.add_field(name="Created at", value=str(user.created_at))
        embed.add_field(name="Joined at", value=str(user.joined_at))
        embed.add_field(name="Roles", value=role.list_roles(user), inline=False)
        await ctx.send(embed=embed)
