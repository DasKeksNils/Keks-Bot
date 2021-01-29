import logging as log
import time


log.basicConfig(filename="log.log", level=log.INFO)


def timestamp():
    return str(time.strftime(" [%m/%d/%Y | %H:%M:%S] ", time.localtime()))


def ready(client):
    log.info(timestamp() + "Logged in as {0.user}".format(client))
    log.info(timestamp() + "Time as " + time.strftime("UTC %z", time.localtime()))
    print(timestamp() + "[CLIENT] Logged in as {0.user}".format(client))


def disconnect():
    log.info(timestamp() + "[CLIENT] has disconnnected")
    print(timestamp() + "Client has disconnected")


def resume():
    log.info(timestamp() + "[CLIENT] has reconnected")
    print(timestamp() + "Client has reconnected")


def message_send(msg):
    log.info(timestamp() + f"[SEND] Message ({msg.id}) from {msg.author} ({msg.author.id}) sent in {msg.channel} ({msg.channel.id}) content: {msg.content}")


def message_delete(msg):
    log.info(timestamp() + f"[DELETE] Message ({msg.id}) from {msg.author} ({msg.author.id}) deleted in {msg.channel} ({msg.channel.id}) content: {msg.content}")


def bulk_delete(messages):
    log.info(timestamp() + f"[BULK_DELETE] Deletet messages: {[message.content for message in messages]}")


def message_edit(before, after):
    log.info(timestamp() + f"[EDIT] Message ({after.id}) from {before.author} ({before.author.id}) edited in {before.channel} ({before.channel.id}) before: {before.content} | to: {after.content}")


def member_join(member):
    log.info(timestamp() + f"[JOIN] Member {member} ({member.id}) joined.")


def member_leave(member):
    log.info(timestamp() + f"[LEFT] Member {member} ({member.id}) left.")


def member_update(before, after):
    log.info(timestamp() + f"[UPDATE] Member {before.name} ({before.id}) changed {before} into {after}")


def command_error(ctx, error):
    log.info(timestamp() + f"[ERROR] {ctx.author} ({ctx.author.id}) has an command error in {ctx.channel} : {error}")


def ban(member, reason, mod):
    log.info(timestamp() + f"[BAN] {member} ({member.id}) got banned from {mod} ({mod.id}) because of: {reason}")


def unban(member):
    log.info(timestamp() + f"[UNBAN] {member} ({member.id}) got unbanned.")


def kick(member, reason, mod):
    log.info(timestamp() + f"[KICK] {member} ({member.id}) got kicked by {mod} ({mod.id}) because of: {reason}")


def mute(member, mod, reason, ban_id):
    log.info(timestamp() + f"[MUTE] {member} ({member.id}) was muted (ban_id: {ban_id}) by {mod} ({mod.id}) because of: {reason}")


def tempmute(member, mod, reason, duration, ban_id):
    log.info(timestamp() + f"[TEMPMUTE] {member} ({member.id}) was tempmuted (ban_id: {ban_id}) {duration} by {mod} ({mod.id}) because of {reason}")


def unmute(member, mod):
    log.info(timestamp() + f"[UNMUTE] {member} ({member.id}) was unmuted by {mod} ({mod.id})")


def channel_create(channel):
    log.info(timestamp() + f"[CHANNEL] {channel} ({channel.id}) was created.")


def channel_delete(channel):
    log.info(timestamp() + f"[CHANNEL] {channel} ({channel.id}) was deleted.")


def channel_update(before, after):
    log.info(timestamp() + f"[CHANNEL] {before.name} ({before.id}) was edited. Before: {before} | After: {after}")
    print(before)
    print(after)


def shutdown(ctx):
    log.info(timestamp() + f"[SHUTDOWN] {ctx.author} ({ctx.author.id}) has shutdown the bot.")
    print(timestamp() + f"{ctx.author} ({ctx.author.id}) has shutdown the bot.")


def voice_update(member, before, after):
    if before.channel != after.channel:
        if before.channel is None:
            log.info(timestamp() + f"[MEMBER] {member} ({member.id}) joint channel: {after.channel} ({after.channel.id})")
        elif after.channel is None:
            log.info(timestamp() + f"[MEMBER] {member} ({member.id}) left channel: {before.channel} ({before.channel.id})")
        else:
            log.info(timestamp() + f"[MEMBER] {member} ({member.id}) switch channel from {before.channel} ({before.channel.id}) to {after.channel} ({after.channel.id})")
