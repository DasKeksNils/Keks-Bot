from config.config import history
import time


def timestamp():
    return str(time.strftime("[%m/%d/%Y | %H:%M:%S]", time.localtime()))


def tempmute(member, reason, mute_id, guild_id, duration):
    history().insert({
        "type": "Tempmute",
        "mute_id": mute_id,
        "name": member.name,
        "user_id": member.id,
        "duration": duration,
        "reason": reason,
        "guild_id": guild_id,
        "timestamp": timestamp()
    })


def mute(member, reason, mute_id, guild_id):
    history().insert({
        "type": "Mute",
        "mute_id": mute_id,
        "name": member.name,
        "user_id": member.id,
        "reason": reason,
        "guild_id": guild_id,
        "timestamp": timestamp()
    })


def ban(member, reason, ban_id, guild_id):
    history().insert({
        "type": "Ban",
        "ban_id": ban_id,
        "name": member.name,
        "user_id": member.id,
        "reason": reason,
        "guild_id": guild_id,
        "timestamp": timestamp()
    })


def kick(member, reason, ban_id, guild_id):
    history().insert({
        "type": "Kick",
        "ban_id": ban_id,
        "name": member.name,
        "user_id": member.id,
        "reason": reason,
        "guild_id": guild_id,
        "timestamp": timestamp()
    })
