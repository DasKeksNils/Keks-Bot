
from discord.ext import commands

from config import log


def admin_cmds(bot):
    @bot.command()
    @commands.has_any_role("Admin")
    async def shutdown(ctx):
        await ctx.message.add_reaction("<:PepeOkay:779775701528215553>")
        await bot.close()
        log.shutdown(ctx)
