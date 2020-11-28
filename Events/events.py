import discord
from discord.ext import commands
from config import log
from config import config
import Webhook.log_send as ch_log
from Moderating.Perms import errors
from Moderating.Perms import role as perms


def message_events(bot):

    @bot.event
    async def on_ready():
        log.ready(bot)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/DerKeksTV/Keks-Bot"))

    @bot.event
    async def on_resumed():
        log.resume()

    @bot.event
    async def on_disconnect():
        log.disconnect()

    @bot.event
    async def on_message(message):
        if message.author == bot.user or message.channel.id == int(config.channels()["log_channel_id"]):
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
            await ctx.send(errors.missing_permission())
        else:
            await ctx.send(error)
        log.command_error(ctx, error)
        print(error)

    @bot.event
    async def on_member_join(member):
        log.member_join(member)
        await ch_log.join(member)
        user = perms.get_role(role="User", ctx=member)
        await member.add_roles(user)

    @bot.event
    async def on_member_remove(member):
        log.member_leave(member)
        await ch_log.leave(member)

    @bot.event
    async def on_member_unban(guild, member):
        log.unban(member)
        await ch_log.member_unban(member)

    @bot.event
    async def on_guild_channel_create(channel):
        log.channel_create(channel)
        await ch_log.channel_create(channel)

    @bot.event
    async def on_guild_channel_delete(channel):
        log.channel_delete(channel)
        await ch_log.channel_delete(channel)

    @bot.event
    async def on_guild_channel_update(before, after):
        log.channel_update(before=before, after=after)
        await ch_log.channel_update(before=before, after=after)

    @bot.event
    async def on_relationship_add(self, relationship):
        await discord.Relationship.accept(self)
