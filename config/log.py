import logging as log
import time


log.basicConfig(filename="log.log", level=log.INFO)


def timestamp():
    ts = time.strftime(" [%m/%d/%Y | %H:%M:%S] ", time.localtime())
    return str(ts)


def ready(client):
    log.info(timestamp() + "Logged in as {0.user}".format(client))
    log.info(timestamp() + "Time as " + time.strftime("UTC %z", time.localtime()))
    print(timestamp() + "[CLIENT] Logged in as {0.user}".format(client))


def disconnect():
    log.info(timestamp() + "[CLIENT] has disconnnected")
    print(timestamp() + "Client has disconnected")


def resume():
    log.info(timestamp() + "[CLIENT] has reconnected")
    print(timestamp() + " Client has reconnected")


def message_send(message):
    log.info(timestamp() + "[SEND] Message from {0.author} sent in {0.channel} content: {0.content}".format(message))


def message_delete(message):
    log.info(timestamp() + "[DELETE] Message from {0.author} deleted in {0.channel} content: {0.content}".format(message))


def bulk_delete(messages):
    log.info(timestamp() + f"[BULK_DELETE] Deletet messages: {[message.content for message in messages]}")


def message_edit(before, after):
    log.info(timestamp() + "[EDIT] Message from " + str(before.author) + " edited in " + str(before.channel) + " before: " + str(before.content) + " | to: " + str(after.content))


def member_join(member):
    log.info(timestamp() + "[JOIN] Member {} joined.".format(member))


def member_leave(member):
    log.info(timestamp() + "[LEFT] Member {} left.".format(member))


def member_update(before, after):
    log.info(timestamp() + "[UPDATE] Member " + before.name + " changed " + before + " into " + after)


def command_error(ctx, error):
    log.info(timestamp() + "[ERROR] {0.author} has an command error in {0.channel} : ".format(ctx) + str(error))


def ban(member, reason, mod):
    log.info(timestamp() + f"[BAN] {member} got banned from {mod} because of: {reason}")


def unban(member):
    log.info(timestamp() + f"[UNBAN] {member} got unbanned.")


def kick(member, reason, mod):
    log.info(timestamp() + f"[KICK] {member} got kicked by {mod} because of: {reason}")


def mute(member, mod, reason):
    log.info(timestamp() + f"[MUTE] {member} was muted by {mod} because of: {reason}")


def unmute(member, mod):
    log.info(timestamp() + f"[UNMUTE] {member} was unmuted by {mod}")


def channel_create(channel):
    log.info(timestamp() + f"[CHANNEL] {channel} was created.")


def channel_delete(channel):
    log.info(timestamp() + f"[CHANNEL] {channel} was deleted.")


def channel_update(before, after):
    log.info(timestamp() + f"[CHANNEL] {before.name} was edited. Before: {before} | After: {after}")
    print(before)
    print(after)


def shutdown(ctx):
    log.info(timestamp() + f"[SHUTDOWN] {ctx.author} had shutdown the bot.")
    print(timestamp() + f"{ctx.author} had shutdown the bot.")


def voice_update(member, before, after):
    if before.channel != after.channel:
        if before.channel is None:
            log.info(timestamp() + f"[MEMBER] {member} ({member.id}) joint channel: {after.channel} ({after.channel.id})")
        elif after.channel is None:
            log.info(timestamp() + f"[MEMBER] {member} ({member.id}) left channel: {before.channel} ({before.channel.id})")
        else:
            log.info(timestamp() + f"[MEMBER] {member} ({member.id}) switch channel from {before.channel} ({before.channel.id}) to {after.channel} ({after.channel.id})")
