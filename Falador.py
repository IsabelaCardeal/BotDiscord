import discord.role
import discord
from discord import ClientException
from discord.ext import commands
import discord.guild
from discord.opus import OpusNotLoaded
from gtts import gTTS
from discord import FFmpegPCMAudio
import random


client = commands.Bot(command_prefix="!")


@client.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cheguei.mp3')
        player = voice.play(source)
    else:
        await ctx.send('Você nem tá no canal certo o doida(o)!!')


filas = {}


@client.command()
async def fila(ctx, arg):
    voice = ctx.guild.voice_client
    song = arg + '.mp3'
    source = FFmpegPCMAudio(song)

    guild_id = ctx.message.guild.id

    if guild_id in filas:
        filas[guild_id].append(source)
    else:
        filas[guild_id] = [source]

    await ctx.send('Adicionado a fila!')


def check_queue(ctx, id):
    if filas[id]:
        voice = ctx.guild.voice_client
        source = filas[id].pop(0)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))


@client.command()
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    song = arg + '.mp3'
    source = FFmpegPCMAudio(song)
    player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('Não tem nada tocando no momento!')


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('Não tem nada pausado!')


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def fala(ctx, *, text=None):
    if not text:
        await ctx.send(f"Hey {ctx.author.mention}, Eu preciso que vc escreva o q eu tenho q dizer, INFERNO!")
        return
    vc = ctx.voice_client
    if not vc:
        # Primeiro tem q dar join para o bot funcionar
        await ctx.send("Me puxa pro canal antes queridinha(o).")
        return
    # Abaixo prepara o texto, a linguagem a ser usada e salva
    tts = gTTS(text=text, lang="pt")
    tts.save("frase.mp3")
    try:
        vc.play(discord.FFmpegPCMAudio('frase.mp3'), after=lambda e: print(f"Terminei de falar: {e}"))
        # Coloca o volume em 1
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
        # Aqui é pra responder caso uma exceção ocorra
    except ClientException as e:
        await ctx.send(f"A client exception occured:\n`{e}`")
    except TypeError as e:
        await ctx.send(f"TypeError exception:\n`{e}`")
    except OpusNotLoaded as e:
        await ctx.send(f"OpusNotLoaded exception: \n`{e}`")


@client.command()
async def speak(ctx, *, text=None):
    if not text:
        #Aqui segue a mesma coisa, porém deixei a língua em inglês
        await ctx.send(f"Hey {ctx.author.mention}, I need to know what to say please.")
        return
    vc = ctx.voice_client
    tts = gTTS(text=text, lang="en")
    tts.save("entext.mp3")
    vc.play(discord.FFmpegPCMAudio('entext.mp3'), after=lambda e: print(f"Finished playing: {e}"))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 1


@client.command()
async def frase(ctx):
    frases = \
        ['frase1.mp3', 'frase2.mp3', 'frase3.mp3', 'frase4.mp3', 'frase5.mp3', 'frase6.mp3', 'frase7.mp3', 'frase8.mp3',
         'frase9.mp3', 'frase10.mp3']

    voice = ctx.guild.voice_client
    ria = random.choice(frases)
    player = voice.play(discord.FFmpegPCMAudio(ria))


@client.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.send('Tô vazando, vlw, flws!!')
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('Ainda bem que eu nem estou aí!!')




@client.event
async def on_ready():
    print("Bot tá pronto!")


client.run("SEU TOKEN AQUI")
