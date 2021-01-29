import discord
from discord.ext import commands

from Moderating.Perms import errors


def stats_cmd(bot):

    @bot.command()
    async def stats(ctx):
        user_count = 0
        cool_count = 0
        muted_count = 0
        freund_count = 0
        bot_count = 0
        mod_count = 0
        dev_count = 0
        admin_count = 0
        members = ctx.guild.members
        for member in members:
            for role in member.roles:
                if role.name == "User":
                    user_count = user_count + 1
                if role.name == "Coole Dudes":
                    cool_count = cool_count + 1
                if role.name == "Muted":
                    muted_count = muted_count + 1
                if role.name == "Freund":
                    freund_count = freund_count + 1
                if role.name == "Bot":
                    bot_count = bot_count + 1
                if role.name == "Moderator":
                    mod_count = mod_count + 1
                if role.name == "Dev":
                    dev_count = dev_count + 1
                if role.name == "Admin":
                    admin_count = admin_count + 1
        stats_embed = discord.Embed(
            title="Server Stats",
            description=ctx.guild.name,
            color=discord.Colour.purple()
        )
        stats_embed.add_field(name="Account's", value=f"{ctx.guild.member_count}", inline=False)
        stats_embed.add_field(name="Admin's", value=f"{admin_count}")
        stats_embed.add_field(name="Dev's", value=f"{dev_count}")
        stats_embed.add_field(name="Moderator's", value=f"{mod_count}")
        stats_embed.add_field(name="Bot's", value=f"{bot_count}")
        stats_embed.add_field(name="Freund", value=f"{freund_count}")
        stats_embed.add_field(name="Coole Dudes", value=f"{cool_count}")
        stats_embed.add_field(name="User", value=f"{user_count}")
        stats_embed.add_field(name="Muted", value=f"{muted_count}")
        stats_embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=stats_embed)
