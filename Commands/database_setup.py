from discord.ext import commands
from config.config import mutes, bans


def setup(bot):

    @bot.command()
    @commands.has_any_role("Admin", "Dev")
    async def botsetup(ctx):
        mutes().insert({
            "_id": 0,
            "name": "mute_id",
            "mute_id": 0,
        })
        bans().insert({
            "_id": 0,
            "name": "ban_id",
            "ban_id": 0,
        })
        await ctx.send("Setup completed!")
