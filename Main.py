from config import config
from Events.events import message_events
from Commands import Index

# TODO: Webhook log fix

bot = config.bot()
message_events(bot)

Index.self_commands(bot)


bot.run(config.startup()["token"])
