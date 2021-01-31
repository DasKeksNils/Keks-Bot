
from config.config import mutes
from config import log
import Webhook.log_send as ch_log
from Database.history import tempmute


def get_mute_ids():
    mute_ids = mutes().find({"_id": 0})
    for re in mute_ids:
        return re["mute_id"]


async def insert(user, mute_end, duration, reason, mod, ctx):
    mute_id = get_mute_ids() + 1
    mutes().insert({
        "mute_id": mute_id,
        "type": "Tempmute",
        "name": user.name,
        "user_id": user.id,
        "duration": duration,
        "mute_end": mute_end,
        "reason": reason,
        "guild_id": ctx.guild.id
    })
    mutes().update_one({"_id": 0}, {"$set": {"mute_id": mute_id}})
    tempmute(member=user, reason=reason, mute_id=mute_id, guild_id=ctx.guild.id, duration=duration)
    await ch_log.tempmute(member=user, mod=mod, reason=reason, mute_id=f"#{mute_id}", duration=duration)
    log.tempmute(member=user, mod=mod, reason=reason, duration=duration, mute_id=mute_id)


def is_in_db(user):
    return mutes().find_one({"user_id": user.id})
