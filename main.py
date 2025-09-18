import os
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


#there are diff types of commands, ones that autocomplete (dynamic) and the other ones this is autocomplete
@bot.tree.command(name="touch", description="Touches YOU!")
async def hello_command(interaction: discord.Interaction):

    await interaction.response.send_message(f"HAHA {interaction.user.mention}, u got the cheese touch!")

#same with this
@bot.tree.command(name='67', description='what did u say???')
async def sixseven(interaction: discord.Interaction):
    await interaction.response.send_message(f"6 7!!🤷")


#this is static lets say (idk the name)
@commands.command(name='rps')
async def rps(ctx, user_choice: str): #r(rock)p(paper)s(scissors) do /rps rock or /rps scissors or /rps paper to do good
    user_choice = user_choice.lower()
    
    # Define the possible choices
    choices = ['rock', 'paper', 'scissors']
    
    #TODO: Fix the fact that nothing is returned when i just press /rps  (no space after just the 4character string)
    if user_choice not in choices:
        await ctx.send("That's not a valid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return 
        
    bot_choice = random.choice(choices)
    
    result = ""
    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        result = "You win!"
    else:
        result = "I win!"
        
    # Send the result to the Discord channel
    await ctx.send(f"You chose **{user_choice}**.\n\nI chose **{bot_choice}**.\n\n**{result}**")

#adds commands (still new to this idfk)
bot.add_command(rps)

@bot.command()
async def sixseven(ctx):#slef explanatory
    await ctx.send(f"6 7!!🤷")

@bot.command()
async def say(ctx, *, message: str):#this basically just echos what u say /say blach blach ->blach blach
    await ctx.send(message)

TOKEN = os.getenv('DISCORD_TOKEN')#fellas you gotta use env variables dont put ur token on github tsk tsk tsk
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN environment variable not found.")
    print("Please set the environment variable with your bot token.")

