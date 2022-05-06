import random
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from io import BytesIO
from PIL import Image
#pro PIL funcionar tem q instalar o pillow

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.listen("on_message")
async def testa(message):
    if message.author == client.user:
        return

   # Nesse formato sempre q a mensagem começar com a palavra entre '' o bot irá responder a frase escrita no await.

    if message.content.startswith('Olá'):
        await message.channel.send('Que SATISFAÇÃO, ASPIRA!')

    if message.content.startswith('fuder'):
        await message.channel.send('Quer me fuder me beija, caralho!')

    if message.content.startswith('marreco'):
        await message.channel.send('Que PORRA é essa marreco??')

    if message.content.startswith('06'):
        await message.channel.send('Xerife, O SENHOR É UM FANFARRÃO!!')

    if message.content.startswith('F'):
        await message.channel.send('F')

    # Como o bot é uma referência ao Capitão Fábio do filme Tropa de Elite, fiz alguns códigos com referências policiais
    # Na sequência tem referência com a comunicação em código Q feita por rádios policais e as patentes policiais c o uso aleatório(random)

    codigin = \
        [('{0.user} QAP'.format(client)), 'QAR, Fox Uniform Índia!!!', 'QRA', 'QRL, tente mais tarde', 'QRQ QSL', 'QRS',
         'QRT',
         'QRU', (message.author.mention + ' QRV'), 'QRX', 'QRZ QSL', 'QSL QAP', 'QSM???', 'QSO', 'QTC QAP', 'QTH QAP',
         'QTR?',
         'QTU QSL', 'QSJ', 'TKS', (message.author.mention + ' QSN?'), 'QSR', 'QSL TKS!', 'QAP QSL', 'QSL QAR',
         'QSL QRX']

    if message.content.startswith('Q'):
        response = random.choice(codigin)
        await message.channel.send(response)

    if message.author == client.user:
        return
    ptt = \
        [' Vc é Cadete!'
         ' :poop: :poop: '
         ' https://tenor.com/view/shooting-gun-gif-10705262 ',
         ' Vc é Soldado! '
         ' :confounded: :poop: '
         'https://tenor.com/view/shot-shoot-gun-gif-8193952 ',
         ' Vc é Cabo! '
         ' :sick: :poop: '
         ' https://tenor.com/view/shooting-leg-shooting-foot-epic-fail-gif-15187504 ',
         ' Vc é 3º Sargento! '
         ' :robot: :poop: '
         ' https://tenor.com/view/magic-hugs-magic-hugs-gifs-blind-fire-shooting-everyone-gif-9990849 ',
         ' Vc é 2º Sargento! '
         ' :sneeze: :poop: '
         ' https://tenor.com/view/shooting-gif-8412137 ',
         ' Vc é 1º Sargento! '
         ' :face_vomiting: :poop: '
         ' https://tenor.com/view/guns-shooting-rapid-shooting-gif-15985662 ',
         ' Vc é Suboficial!  '
         ' :persevere: :clown: '
         ' https://tenor.com/view/gun-gun-fire-shooting-surprised-newbie-gif-3699790 ',
         ' Vc é Aspirante! '
         ' :tired_face: :clown: '
         ' https://tenor.com/view/strength-test-shooting-phones-gun-fire-smartphones-apple-gif-12594378 ',
         ' Vc é 2º Tenente! '
         ' :face_with_symbols_over_mounth: :face_with_symbols_over_mounth: '
         ' https://tenor.com/view/shooting-dance-shootingfan-gif-4836077 ',
         ' Vc é 1º Tenente! '
         ' :exploding_head: :face_with_symbols_over_mounth: '
         ' https://tenor.com/view/sheriff-cowboy-western-gun-gif-14191460 ',
         ' Vc é Capitão! '
         ' :star: :cowboy: '
         ' https://tenor.com/view/black-widow-avengers-endgame-marvel-shooting-gif-13804696 ',
         ' Vc é Major! '
         ' :nerd: :face_with_monocle: '
         ' https://tenor.com/view/gun-shooting-gif-7938698 ',
         ' Vc é Tenente-Coronel! '
         ' :satisfied: :face_with_monocle: '
         ' https://tenor.com/view/gordo-bom-de-tiro-tiro-gordao-picando-fogo-gun-gif-15477774 ',
         ' Vc é Coronel! '
         ' :nerd: :smirk: '
         ' https://tenor.com/view/girl-weapon-gun-firing-gif-15462753 ',
         ' Vc é Subcomandante! '
         ' :stuck_out_tongue_closed_eyes: :sunglasses: '
         ' https://tenor.com/view/jenn-jacques-shooting-shootingsports-shotgun-gun-gif-14326969 ',
         ' Vc é Comandante Geral! '
         ' :smiling_imp: :star_struck: '
         ' https://media1.tenor.com/images/3ee83e5fc11ecae9bf4c89007d3105dd/tenor.gif?itemid=17871040 ']

    if message.content == 'patente':
        response = random.choice(ptt)
        await message.channel.send(message.author.mention + response)


# Aqui o bot cria uma embed com estilo de ficha policial, usei o random para mudar os crimes e a cor da embed.
# Agora esses comandos pedem o prefixo escolhido lá em cima.

@client.command()
async def ficha(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    texto = \
        [' É a traficante mais procurada no Brasil, envolvida com a comercialização de grande quantidade de drogas.'
         ' Em uma de suas prisões, trocou tiros com policiais. '
         'Atende pelos apelidos de Professora e Tia. Condenada a mais de 50 anos de prisão.',

         ' É o líder de uma organização criminosa que, por meio da captação de investimentos em criptmoedas,'
         ' teria montado um dos maiores esquemas de pirâmide financeira no Brasil.'
         ' Atende pelo apelido de Faraó do Bitcoin, movimentou mais de $38 BILHÕES de reais!! Responde a 288 processos na área cível.',

         ' Golpista de primeiríssima já assumiu diversas identidades falsas, conseguiu VIPs se passando por CEO, '
         'tb conseguiu diárias em Resort, dirigir viaturas se passando por agente de operções especiais e até pilotou para o narcotráfico.'
         ' Atende pelos apelidos de Kim, Ariel, Noah, Andrea e etc.  Cumpriu 15 anos de prisão, porém já fugiu + de 9x.',

         ' É o político do povo, qdo iniciou se dizia contra o sistema corrupto, q ía trazer uma nova política para o país, melhorar'
         ' a educação, saúde e economia. Conseguiu ser eleito, criou uma aliança e montou maior esquema de desvio de orçamento já visto.'
         ' Atende pelo apelido de Cobra, por ser mto articulado e traiçoeiro. Desviou centenas de milhões de reais, nunca foi condenado '
         'e já está no seu 4º mandato.']

    cor = \
        [8388736, discord.Colour.dark_purple(), discord.Colour.green(), discord.Colour.blue(),
         discord.Colour.dark_gold(),
         discord.Colour.dark_grey(), discord.Colour.dark_green(), discord.Colour.blurple(),
         discord.Colour.dark_orange(),
         discord.Colour.magenta(), discord.Colour.light_grey(), discord.Colour.red(), discord.Colour.teal(),
         discord.Colour.gold()]

    megafone = ":warning:"
    pessoa = user
    alerta = ':gun: :money_with_wings: :coin: :ninja:'
    st = discord.Embed(
        title=f"{megafone}{megafone}{megafone} ATENÇÃO!! {megafone}{megafone}{megafone}",
        description=random.choice(texto),
        colour=random.choice(cor))
    st.set_author(name=f'Nome: {pessoa}',
                  icon_url=user.avatar_url_as()),
    st.set_footer(text='A DENÚNCIA QUE LEVE O PROCURADO/FORAGIDO A SER PRESO, PODERÁ GERAR PRÊMIO DE 10 MIL REAIS AO'
                       ' DENUNCIANTE, PRESERVADO O SIGILO DE SUA IDENTIDADE.'),
    st.set_thumbnail(url=user.avatar_url_as())
    await ctx.channel.send(embed=st)


# Aqui o bot vai utilizar os canais de voz e reproduzirá arquivos .mp3 q estejam na mesma pasta do arquivo python
# O QAP(no código Q = Na escuta) e o QAR = desligar farão com q o bot se junte a vc no canal e saia do canal
# O play, pause, resume e stop executam o padrão, toca o arquivo, pausa o arquivo,
# volta a tocar o arquivo do momento q pausou e para o arquivo e não volta mais da onde parou
# O fila monta uma playlist.

filas = {}


@client.command(pass_context=True)
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

#aqui o bot vai se juntar ao canal de voz e já reproduzir o arquivo 'seuarquivo.mp3'.

@client.command(pass_context=True)
async def QAP(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('seuarquivo.mp3')
        player = voice.play(source)

    else:
        await ctx.send('Você nem tá no canal certo o doida(o)!!')


@client.command(pass_context=True)
async def QAR(ctx):
    if ctx.voice_client:
        await ctx.send('Tô vazando, vlw, flws!!')
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('Ainda bem que eu nem estou aí!!')


@client.command(pass_context=True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    song = arg + '.mp3'
    source = FFmpegPCMAudio(song)
    player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))


@client.command(pass_context=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('Não tem nada tocando no momento!')


@client.command(pass_context=True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('Não tem nada pausado!')


@client.command(pass_context=True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

#esse comando pega um arquivo de imagem salvo, adiciona a imagem do avatar da pessoa marcada cria um novo arquivo
# e o envia editado, no caso a imagem escolhida foi a de procurado, daí fica o avatar da pessoa c o fundo de procurado
# o resize se refere ao tamanho da foto do usuario escolhido e os numeros do paste se referem a posição q a imagem vai ser colada

@client.command()
async def wanted(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    wanted = Image.open("Procurado1.jpg")
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((149, 148))
    wanted.paste(pfp, (102, 171))
    wanted.save("cara.jpg")
    await ctx.send(file=discord.File("cara.jpg"))


# por fim coloco o aviso q o bot está online somente no terminal, gosto de colocá-lo no final de
# td para checar se está tem algum erro e só depois ficar online.

@client.event
async def on_ready():
    print('{0.user} Tá on!!!!'.format(client))


client.run("BOT TOKEN AQUI")
