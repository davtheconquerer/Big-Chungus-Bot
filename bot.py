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




@bot.event
async def on_ready():
    print("big chungus is up and running")




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




@bot.application_command(name = "uwu", description = "UwUwUwUwUwUwU")
async def uwu(ctx):
    await ctx.respond(content = "owo")

@bot.application_command(name = "purge", description = "delete messages in bulk")
async def purge(ctx, messages: discord.commands.Option(int, "number of messages to delete", max_value=100, min_value=2)):
    await ctx.defer(ephemeral=True)

    await ctx.channel.purge(limit=messages)

    await ctx.interaction.edit_original_message(content = f"You purged `{messages}` messages")


@bot.application_command(name = "ping", description = "ping")
async def ping(ctx):
    await ctx.respond(content = "pong")







token = os.getenv("TOKEN")
bot.run(token)
