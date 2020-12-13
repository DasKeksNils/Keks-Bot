import discord
import time


def timestamp():
    return str(time.strftime("%m/%d/%Y at %H:%M", time.localtime()))


def join(member):
    member_join = discord.Embed(
        title="Member joined",
        description="Created at " + str(member.created_at),
        colour=discord.Colour.green()
    )
    member_join.set_footer(text=f"{member.id} \n" + timestamp(), icon_url=member_join.Empty)
    member_join.set_author(icon_url=member.avatar_url, name=member)
    return member_join


def leave(member):
    member_leave = discord.Embed(
        title="Member left",
        description="Joined at " + str(member.created_at),
        colour=discord.Colour.red()
    )
    member_leave.set_footer(text=f"{member.id} \n" + timestamp(), icon_url=member_leave.Empty)
    member_leave.set_author(icon_url=member.avatar_url, name=member)
    member_leave.add_field(name="Roles", value=str([role.name for role in member.roles]))
    return member_leave


def delete(message):
    delete_embed = discord.Embed(
        title="Message deleted in " + str(message.channel),
        description=message.content,
        colour=discord.Colour.orange()
    )
    delete_embed.set_author(icon_url=message.author.avatar_url, name=message.author)
    delete_embed.set_footer(text=f"{message.id} \n" + timestamp(), icon_url=delete_embed.Empty)
    return delete_embed


def bulk_delete(messages):
    bulk_embed = discord.Embed(
        title="Bulk message delete",
        color=discord.Colour.orange(),
        description=str([message.content for message in messages])
    )
    bulk_embed.set_footer(text=timestamp(), icon_url=bulk_embed.Empty)
    return bulk_embed


def msg_edit(before, after):
    edit_embed = discord.Embed(
        title="Message edited in " + str(before.channel),
        colour=discord.Colour.dark_green()
    )
    edit_embed.add_field(name="Before", value=str(before.content), inline=True)
    edit_embed.add_field(name="After", value=str(after.content), inline=True)
    edit_embed.set_author(icon_url=before.author.avatar_url, name=before.author)
    edit_embed.set_footer(text=f"{after.id} \n" + timestamp(), icon_url=edit_embed.Empty)
    return edit_embed


def member_update(before, after):
    user_update = discord.Embed(
        title="Member updated",
        color=discord.Colour.blue()
    )
    user_update.add_field(name="Before", value=str(before), inline=True)
    user_update.add_field(name="After", value=str(after), inline=True)
    user_update.set_author(icon_url=before.member.avatar_url, name=before.member)
    user_update.set_footer(text=f"{after.id} \n" + timestamp(), icon_url=user_update.Empty)
    return user_update


def ban(member, reason, mod):
    ban_embet = discord.Embed(
        title="Member got banned!",
        color=discord.Colour.red()
    )
    ban_embet.add_field(name="Reason", value=str(reason))
    ban_embet.add_field(name="Moderator", value=str(mod))
    ban_embet.set_author(name=member, icon_url=member.avatar_url)
    ban_embet.set_footer(text=f"{member.id} \n" + timestamp(), icon_url=ban_embet.Empty)
    return ban_embet


def unban(member):
    unban_embet = discord.Embed(
        title="Member got unbanned!",
        color=discord.Colour.dark_green()
    )
    unban_embet.set_author(name=member, icon_url=member.avatar_url)
    unban_embet.set_footer(text=f"{member.id} \n" + timestamp(), icon_url=unban_embet.Empty)
    return unban_embet


def kick(member, reason, mod):
    kick_embed = discord.Embed(
        title="Member got kicked!",
        color=discord.Colour.red()
    )
    kick_embed.add_field(name="Reason", value=str(reason))
    kick_embed.add_field(name="Moderator", value=str(mod))
    kick_embed.set_author(name=member, icon_url=member.avatar_url)
    kick_embed.set_footer(text=f"{member.id} \n" + timestamp(), icon_url=kick_embed.Empty)
    return kick_embed


def mute(member, mod, reason):
    mute_embed = discord.Embed(
        title="Member muted",
        color=discord.Colour.dark_orange()
    )
    mute_embed.add_field(name="Reason", value=reason)
    mute_embed.add_field(name="Moderator", value=mod)
    mute_embed.set_author(name=member, icon_url=member.avatar_url)
    mute_embed.set_footer(text=f"{member.id} \n" + timestamp(), icon_url=mute_embed.Empty)
    return mute_embed


def unmute(member, mod):
    unmute_embed = discord.Embed(
        title="Member unmuted",
        color=discord.Colour.green()
    )
    unmute_embed.add_field(name="Moderator", value=mod)
    unmute_embed.set_author(name=member, icon_url=member.avatar_url)
    unmute_embed.set_footer(text=f"{member.id} \n " + timestamp(), icon_url=unmute_embed.Empty)
    return unmute_embed


def channel_create(channel):
    create_embed = discord.Embed(
        title="Channel created",
        color=discord.Colour.blue()
    )
    create_embed.add_field(name="Name", value=channel.name)
    create_embed.set_footer(text=f"{channel.id} \n" + timestamp(), icon_url=create_embed.Empty)
    return create_embed


def channel_delete(channel):
    delete_embed = discord.Embed(
        title="Channel deleted",
        color=discord.Colour.dark_orange()
    )
    delete_embed.add_field(name="Name", value=channel.name)
    delete_embed.add_field(name="Created at", value=str(channel.created_at))
    delete_embed.set_footer(text=f"{channel.id} \n" + timestamp(), icon_url=delete_embed.Empty)
    return delete_embed


def channel_update(before, after):
    update_embed = discord.Embed(
        title="Channel edited",
        color=discord.Colour.blue()
    )
    update_embed.add_field(name="Before:", value=before)
    update_embed.add_field(name="After:", value=after)
    update_embed.set_footer(text=f"{after.id} \n" + timestamp(), icon_url=update_embed.Empty)
    return update_embed



