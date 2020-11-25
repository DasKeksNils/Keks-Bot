import logging as log
import time


log.basicConfig(filename="log.log", level=log.INFO)


def timestamp():
    ts = time.strftime(" [%m/%d/%Y | %H:%M:%S] ", time.localtime())
    return str(ts)


def ready(client):
    log.info(timestamp() + "Logged in as {0.user}".format(client))
    log.info(timestamp() + "Time as " + time.strftime("UTC %z", time.localtime()))
    print("Logged in as {0.user}".format(client))


def message_send(message):
    log.info(timestamp() + "[SEND] Message from {0.author} send in {0.channel} content: {0.content}".format(message))


def message_delete(message):
    log.info(timestamp() + "[DELETE] Message from {0.author} deleted in {0.channel} content: {0.content}".format(message))


def bulk_delete(messages):
    log.info(timestamp() + f"[BULK_DELETE] Messages: {messages}")


def message_edit(before, after):
    log.info(timestamp() + "[EDIT] Message from " + str(before.author) + " edited in " + str(before.channel) + " before: " + str(before.content) + " | to: " + str(after.content))


def member_join(member):
    log.info(timestamp() + "[JOIN] Member {} joined.".format(member))


def member_leave(member):
    log.info(timestamp() + "[LEFT] Member {} left.".format(member))


def member_update(before, after):
    log.info(timestamp() + "[UPDATE] Member " + before.name + " changed " + before + " into " + after)


def command_error(ctx, error):
    log.info(timestamp() + "[INFO] {0.author} has an command error in {0.channel} : ".format(ctx) + str(error))


def ban(member, reason, mod):
    log.info(timestamp() + f"[INFO] {member} got banned from {mod} because of: {reason}")


def unban(member):
    log.info(timestamp() + f"[INFO] {member} got unbanned.")


def kick(member, reason, mod):
    log.info(timestamp() + f"[INFO] {member} got kicked by {mod} because of: {reason}")


def mute(member, mod, reason):
    log.info(timestamp() + f"[INFO] {member} was muted by {mod} because of: {reason}")


def unmute(member, mod):
    log.info(timestamp() + f"[INFO] {member} was unmuted by {mod}")
