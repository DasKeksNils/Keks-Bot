from config import config
from Events.events import message_events
from Commands import Index

# TODO: mute log and message (embed)
# TODO: autorole on join


bot = config.bot()

message_events(bot)

Index.self_commands(bot)


bot.run(config.startup()["token"])
