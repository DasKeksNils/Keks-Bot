
from config.config import tempmutes
from config import log
import Webhook.log_send as ch_log


def get_ban_ids():
    ban_ids = tempmutes().find({"_id": 0})
    for re in ban_ids:
        return re["ban_id"]


async def insert(user, mute_end, duration, reason, mod, ctx):
    ban_ids = get_ban_ids()
    tempmutes().insert({
        "ban_id": ban_ids + 1,
        "type": "Tempmute",
        "name": user.name,
        "user_id": user.id,
        "duration": duration,
        "mute_end": mute_end,
        "reason": reason,
        "guild_id": ctx.guild.id
    })
    tempmutes().update_one({"_id": 0}, {"$set": {"ban_id": ban_ids + 1}})
    await ch_log.tempmute(member=user, mod=mod, reason=reason, ban_id="#" + str(ban_ids + 1), duration=duration)
    log.tempmute(member=user, mod=mod, reason=reason, duration=duration, ban_id=ban_ids + 1)


def is_in_db(user):
    return tempmutes().find_one({"user_id": user.id})
