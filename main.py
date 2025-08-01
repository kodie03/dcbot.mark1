import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

basic_role = 'level-1'

@bot.event
async def on_ready():
    print(f'We are ready to go in, {bot.user.name}')

#

@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to the server {member.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
     # Replace 'YOUR_BYPASS_USER_ID_HERE' with the actual ID of the user you want to bypass
    #bypass_user_id = 435803034681999370  # Example ID

    #if message.author.id == bypass_user_id:
    #    return # This will make the bot ignore all rules for this specific user


    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention} dont swear')
    #(insert TEMP2 Here)
    await bot.process_commands(message)
#TEMP2 
'''
    if "nigga" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention}, mannn dont say that stuff')

    if "nigger" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention}, mannn dont say that stuff')

''' 
# end of TEMP2
    
@bot.command()
async def hello(ctx):
    '''
    Basic Greeting!
    '''
    await ctx.send(f'Hello {ctx.author.mention}')

'''
#woopf
@bot.command()
async def clearancelevel1(ctx):
    
    
    role = discord.utils.get(ctx.guild.roles, name=basic_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f'{ctx.author.mention} is now assigned to {basic_role}')
    else:
        await ctx.send(f'Role does not exist')
'''

@bot.command()
async def clearancelevel1(ctx):
    '''
    Assigns the user to the basic "level-1" role.
    '''
    # Delete the message that triggered the command
    await ctx.message.delete()

    role = discord.utils.get(ctx.guild.roles, name=basic_role)
    if role:
        await ctx.author.add_roles(role)
        # Send a confirmation message and store it in a variable
        confirmation_message = await ctx.send(f'Congrats you now have the role!')
        # Wait for 5 seconds before deleting the confirmation message
        await asyncio.sleep(5)
        await confirmation_message.delete()
    else:
        # If the role doesn't exist, send a message that will also be deleted
        error_message = await ctx.send(f'Role does not exist')
        # Wait for 5 seconds before deleting the error message
        await asyncio.sleep(5)
        await error_message.delete()

####

@bot.command()
async def buss(ctx):
    """
    Gonna jork it for you
    """
    gif_url = "https://tenor.com/vi4D.gif"
    await ctx.send(gif_url)
    # Send the initial message
    await ctx.send("I'm boutta cummmmmm")
    # Perform a countdown from 5 to 1 with a 1-second delay
    for i in range(5, 0, -1):
        await ctx.send(str(i))
        await asyncio.sleep(1)

    # Send the new GIF after the countdown is complete
    await ctx.send('BUUSSSSSSS')
    await ctx.send("https://tenor.com/bXnp7.gif")
    await asyncio.sleep(1)
    await ctx.send('https://tenor.com/bnkny.gif')
    await asyncio.sleep(1)               
    await ctx.send('https://tenor.com/Swgy.gif')
    
    # Send the final message with the user's mention
    await ctx.send(f"oh fuck yeah baby {ctx.author.mention}")


# You can add more commands that send different GIFs if you like.
# For example, here's a second one:
@bot.command()
async def party(ctx):
    """
    Sends a party GIF.
    """
    party_gif_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2pndG9tM3NqZzJ0Z25yNTRtbzJvMXE1a293Z2d6NHk2Z3lqcmVvMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IwSGgA17jDq28/giphy.gif"
    await ctx.send(party_gif_url)



#bot.run(token, log_handler=handler, log_level=logging.DEBUG)