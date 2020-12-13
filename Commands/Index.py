from Commands import ban_c
from Commands import roles_c
from Commands import mute_c
from Commands import clear_c
from Commands import user_cmds
from Commands import admin_c
from Commands import whois


def self_commands(bot):

    ban_c.ban_commands(bot)
    roles_c.roles(bot)
    mute_c.mute_user(bot)
    clear_c.muting(bot)
    user_cmds.user_commands(bot)
    admin_c.admin_cmds(bot)
    whois.command(bot)
