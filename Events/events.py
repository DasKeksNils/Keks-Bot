from discord.ext import commands
from config import log
import Webhook.log_send as ch_log


def message_events(bot):

    @bot.event
    async def on_ready():
        log.ready(bot)

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        log.message_send(message)
        await bot.process_commands(message)

    @bot.event
    async def on_message_delete(message):
        if message.author == bot.user:
            return
        log.message_delete(message)
        await ch_log.delete(message)

    @bot.event
    async def on_bulk_message_delete(messages):
        log.bulk_delete(messages)
        await ch_log.bulk_delete(messages)

    @bot.event
    async def on_message_edit(before, after):
        if before.author == bot.user:
            return
        log.message_edit(before=before, after=after)
        await ch_log.edit(before=before, after=after)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You don't have the permission to do that <:SmileW:779776042096918528>")
        else:
            await ctx.send(error)
        log.command_error(ctx, error)
        print(error)

    @bot.event
    async def on_member_join(member):
        log.member_join(member)
        await ch_log.join(member)

    @bot.event
    async def on_member_leave(member):
        log.member_leave(member)
        await ch_log.leave(member)

    @bot.event
    async def on_member_unban(guild, member):
        log.unban(member)
        await ch_log.member_unban(member)
