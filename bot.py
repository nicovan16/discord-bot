import discord
from discord.ext import commands
import random
import typing

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "$", intents = intents, description="Bot programmer par le pire dev du monde, aka Nico, mais tkt")

@client.event
async def on_ready():
    game = discord.Game("FORTNITE")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Prêt !")

@client.event
async def on_member_join(member):
    print("{} est un bg de la street".format(member))
    await member.send("Tu es un bg de la street.")

@client.event
async def on_member_remove(member):
    print("{} est un gros pd.".format(member))
    await member.send("Tu es un gros pd.")

@client.command()
async def wesh(ctx):
    await ctx.send("T'es trop une Sandboxracaille, wesh")

@client.command()
async def serverInfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrits et {numberOfVoiceChannels} salons vocaux."
    await ctx.send(message)

@client.command()
async def bite(ctx, nom: typing.Optional[str]):
    if not nom:
        await ctx.send("Ta bite:\n8{}>".format(random.randint(0, 20) * "="))
    else:
        await ctx.send('La bite de {}:\n8{}>'.format(nom, random.randint(0, 20) * "="))

@client.command()
async def con(ctx, nom: typing.Optional[str]):
    a = random.randint(0, 100)
    if not nom:
        if a >= 90:
            await ctx.send("Tu es con à: {}% \nAutiste spotted -_-".format(a))
        elif 50<=a<90:
            await ctx.send("Tu es con à: {}% \nT'es gentil quoi".format(a))
        elif 10<=a<49:
            await ctx.send("Tu es con à {}% \nTrkl t'es en dessous de la moyenne".format(a))
        else:
          await ctx.send("Tu es con à: {}% \nT'es un génie en fait".format(a))
    else:
        if a >= 90:
            await ctx.send("{} est con à: {}% \nAutiste spotted -_-".format(nom, a))
        elif 50<=a<90:
            await ctx.send("{} est con à: {}% \nIl/Elle est gentil(le) quoi".format(nom , a))
        elif 10<=a<49:
            await ctx.send("{} est con à: {}% \nTrkl il/elle est en dessous de la moyenne".format(nom, a))
        else:
            await ctx.send("{} est con à: {}% \nC'est un(e) génie en fait".format(nom, a))

@client.command(aliases=["ms","latence"])
async def ping(ctx):
    await ctx.send("La latence est {} ms".format(round(client.latency*1000)))

#@client.command(aliases=["purge"])
#async def clear(ctx, amount=0):
    #await ctx.channel.purge(limit=amount+1)

client.run("ODA4Njk5NzE2NzIwMDAxMDg1.YCKWTQ.yfoA-vBRa9rUkS2BiBWTdA4ZyEk")
