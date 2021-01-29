from Commands import admin_c, ban_c, clear_c, mute_c, roles_c, serverstats, tempmute, user_cmds, whois, database_setup


def self_commands(bot):
    ban_c.ban_commands(bot)
    roles_c.roles(bot)
    mute_c.mute_user(bot)
    clear_c.muting(bot)
    user_cmds.user_commands(bot)
    admin_c.admin_cmds(bot)
    whois.command(bot)
    serverstats.stats_cmd(bot)
    tempmute.temp_cmds(bot)
    database_setup.setup(bot)
