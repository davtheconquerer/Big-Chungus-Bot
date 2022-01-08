import discord
import os


from dotenv import load_dotenv
load_dotenv()





bot = discord.Bot(
    intents = discord.Intents(
        guilds = True,
        messages = True
    ),
    debug_guilds = [867087433202663444],

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




# ~~~~~~~~~~ #
# MODERATION #
# ~~~~~~~~~~ #

# `purge command` deletes number of messages >>>

@bot.application_command(name = "purge", description = "delete messages in bulk", default_permission = False)
@discord.permissions.has_any_role(867087495391608843, 835190138363052119)

async def purge(ctx, messages: discord.commands.Option(int, "number of messages to delete", max_value=100, min_value=1)):
    await ctx.defer(ephemeral=True)

    await ctx.channel.purge(limit=messages)

    await ctx.interaction.edit_original_message(content = f"You purged `{messages}` messages")




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
