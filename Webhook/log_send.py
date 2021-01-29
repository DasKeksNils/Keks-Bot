from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from config.config import startup
from Webhook import Embeds


async def delete(message):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.delete(message))


async def bulk_delete(messages):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.bulk_delete(messages))


async def edit(before, after):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.msg_edit(before=before, after=after))


async def join(member):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.join(member))


async def leave(member):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.leave(member))


async def member_update(before, after):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.member_update(before=before, after=after))


async def member_ban(member, reason, mod):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.ban(member, reason, mod))


async def member_unban(member):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.unban(member))


async def member_kick(member, reason, mod):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.kick(member, reason, mod))


async def mute(member, mod, reason, ban_id):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.mute(member=member, mod=mod, reason=reason, ban_id=ban_id))


async def tempmute(member, mod, reason, ban_id, duration):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.tempmute(member=member, mod=mod, reason=reason, ban_id=ban_id, duration=duration))


async def unmute(member, mod, ban_id, reason, totype):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.unmute(member=member, mod=mod, ban_id=ban_id, reason=reason, totype=totype))


async def channel_create(channel):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.channel_create(channel))


async def channel_delete(channel):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.channel_delete(channel))


async def channel_update(before, after):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(startup()["log_wh"], adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=Embeds.channel_update(before=before, after=after))
