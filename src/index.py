import discord 
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix = '>', description = "This is a description")

@bot.command()
async def ping(context):
    await context.send('pong')

@bot.command()
async def sum(context, num1: int, num2: int):
    await context.send(num1 + num2)

@bot.command()
async def info(context):
    embed = discord.Embed(title = f"{context.guild.name}", description = "Lorem impsum asdfasdf", timestamp = datetime.datetime.utcnow(), color = discord.Color.green())
    embed.add_field(name = "Server created at", value = f"{context.guild.created_at}")
    embed.add_field(name = "Server owner", value = f"{context.guild.owner}")
    embed.add_field(name = "Server region", value = f"{context.guild.region}")
    embed.add_field(name = "Server ID", value = f"{context.guild.id}")
    await context.send(embed = embed)

#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/accountname"))
    print("Loading bot...")

bot.run('NzAwNDU5MjYxMDU4MjIwMDYy.Xpjrkg.GBqx0NDfAUGxFsQ9DmqjTg0Mvy0')