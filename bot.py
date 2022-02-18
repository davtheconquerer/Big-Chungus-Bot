import discord
import os


from dotenv import load_dotenv
load_dotenv()





bot = discord.Bot(
    intents = discord.Intents(
        guilds = True,
        messages = True
    ),

    status = discord.Status.idle,
    activity = discord.Activity(
        name = "to big noises",
        type = discord.ActivityType.listening
    )
)



# Start up event >>>

@bot.event
async def on_ready():
    print("big chungus is up and running")


# replies if someone types big or chungus, vice versa >>>

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return


    if message.content == "big":
        await message.reply(content = "chungus", allowed_mentions = discord.AllowedMentions.none())


    elif message.content == "chungus":
        await message.reply(content = "big", allowed_mentions = discord.AllowedMentions.none())


    elif message.content == "aleks sucks":
        await message.reply(content = "agreed", allowed_mentions = discord.AllowedMentions.none())


    elif message.content == "alex sucks":
        await message.reply(content = "agreed", allowed_mentions = discord.AllowedMentions.none())



# ~~~~ #
# HELP #
# ~~~~ #

# `help command` provides help

@bot.application_command(name = "help", description = "provides list of available commands", guild_ids = [867087433202663444, 835190138363052113])

async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.from_rgb(255, 136, 0), title = f"This is the Help Menu for {bot.user}!", description = "*nothing here...*")
    embed.set_author(name="ShadowDev#0001", url="https://github.com/ItsShadowDev/Big-Chungus-Bot", icon_url="https://cdn.discordapp.com/avatars/695230133229060127/b21ac30b4c841d1e2b8bb19a37b6cb5b.png")
    embed.set_image(url="https://c.tenor.com/7Ypq9_9najcAAAAC/thumbs-up-double-thumbs-up.gif")
    await ctx.defer(ephemeral=False)

    await ctx.respond(embeds=[embed])



# ~~~~~~~~~~ #
# MODERATION #
# ~~~~~~~~~~ #

# `purge command` deletes number of messages >>>

@bot.application_command(name = "purge", description = "delete messages in bulk", guild_ids = [867087433202663444, 835190138363052113], default_permission = False)
@discord.commands.permissions.has_any_role(867087495391608843, 835190138363052119)

async def purge(ctx, messages: discord.commands.Option(int, "number of messages to delete", max_value=100, min_value=1)):
    await ctx.defer(ephemeral=True)

    await ctx.channel.purge(limit=messages)

    await ctx.interaction.edit_original_message(content = f"You purged `{messages}` messages")


# `kick command` kicks a user >>>

@bot.application_command(name = "kick", description = "kicks a user", guild_ids = [867087433202663444], default_permission = False)
@discord.commands.permissions.has_any_role(867087495391608843, 835190138363052119) # <<< role ids

async def kick(ctx, member: discord.commands.Option(discord.Member, "the member you want to kick"), reason: discord.commands.Option(str, "reason for kick", required=False, default="You have been kicked!")):
    await member.send(f"`Punishment:` Kick\n`Moderator:` {ctx.member.username}#{ctx.member.discriminator}\n`Reason:` {reason}")
    await member.kick(reason=reason)


# `ban command` bans a user >>>

@bot.application_command(name = "ban", description = "bans a user", guild_ids = [867087433202663444], default_permission = False)
@discord.commands.permissions.has_any_role(867087495391608843, 835190138363052119) # <<< role ids

async def ban(ctx, member: discord.commands.Option(discord.Member, "the member you want to ban"), reason: discord.commands.Option(str, "reason for ban", required=False, default="You have been banned!")):
    await member.send(f"`Punishment:` Ban\n`Moderator:` {ctx.member.username}#{ctx.member.discriminator}\n`Reason:` {reason}")
    await member.ban(reason=reason)



# ~~~ #
# FUN #
# ~~~ #

# `ping command` fun >>>

@bot.application_command(name = "ping", description = "ping")
async def ping(ctx):
    await ctx.respond(content = "pong")


# `uwo command` which replies with owo >>>

@bot.application_command(name = "uwu", description = "UwUwUwUwUwUwU")
async def uwu(ctx):
    await ctx.respond(content = "owo")



# not important >>>

token = os.getenv("TOKEN")
bot.run(token)
