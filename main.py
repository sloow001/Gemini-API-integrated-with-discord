import discord
import google.generativeai as genai
from discord.ext import commands

permissions = discord.Intents.default()
permissions.message_content = True
permissions.members = True
bot = commands.Bot(command_prefix=".", intents=permissions)

# you generate this in (https://aistudio.google.com/app/apikey)
genai.configure(api_key="your_google_api")

def generate_content(query):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    return response.text

@bot.command()
async def generate(ctx: commands.Context, *, query):
    content = generate_content(query)
    # As discord has a character limit, here we will be splitting the message if it is more than 2000 characters
    if len(content) <= 2000:
        await ctx.reply(content)
    else:
        parts = [content[i:i+2000] for i in range(0, len(content), 2000)]
        for part in parts:
            await ctx.reply(part)

@bot.event
async def on_ready():
    print("Done Bot")

# you generate this in (https://discord.com/developers/applications)
bot.run("your bot token")
