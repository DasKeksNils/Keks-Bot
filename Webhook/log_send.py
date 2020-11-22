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
        await webhook.send(embed=Embeds.edit(before=before, after=after))


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
