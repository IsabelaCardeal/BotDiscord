# Bot para o discord em Python

Esse é um projeto de Bot em python com comandos básicos, embeds e resposta em áudios.

Mas vamos do passo a passo para criar o bot no discord:
## Primeira Parte
* Clique na opção New Application no site https://discord.com/developers/applications
* Escolha o nome do Bot, vai aparece uma nova página(vc deverá estar em General Information) para editar o nome, a foto, a descrição do bot
* Na esquerda vc vai ler Settings, clique na opção Bot e add Bot.

Agora vai aparecer a mensagem "A wild bot has appeared!" - Vc vai ver a foto escolhida, o nome do bot e o Token, se não aparecer de primeira clique em Reset Token.

* SALVE ESSE TOKEN pois ele é essencial para conectar o bot c o discord(nunca divulgue ele)!!!

Nas opções abaixo aperecem opções de Autorização, eu deixei marcada a opção - Public Bot e todas do Privileged Gateway Intents. Abaixo vão ter várias opções de permissões, vc não precisa marcar agora, dps no seu server vc pode configurar isso.
E é só isso que vc precisa mexer no discord nesse momento(pode deixar como está as opções Rich Presence e App Tester).

## Segunda Parte 
Agora vamos entrar com a programação do bot, vc vai precisar ter instalado o programa da linguagem que vc vai utilizar e um editor.

No meu caso eu estou usando o Python 3.6 e a IDE PyCharm modo gratuito(q é o da comunidade), vc pode usar outro IDE, como o Visual Studio ou outros, o que vc melhor preferir.
* [Download Python](https://www.python.org/downloads/) 
* [Download Pycharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows)

**OBS.: Caso vc escolha utilizar o PyCharm, pode instalar o Python dentro da IDE msm, dps q baixar e abrir o Pycharm vai abrir a janela de configs, qdo chegar em New Project vc seleciona o interpretador pretendido(Base Interpreter) e por ali msm irá baixar o Python.**

* [Tutorial instalação e configuração Python e Pycharm](https://www.devmedia.com.br/instalacao-do-python/40643#:~:text=Na%20tela%20inicial%20do%20PyCharm,e%20depois%20em%20%E2%80%9CSettings%E2%80%9D.&text=Na%20nova%20tela%20da%20Figura,os%20nossos%20c%C3%B3digos%20em%20Python.)

## Terceira Parte
Agora nós vamos para o código em si, no meu caso, vou compartilhar o meu Bot 02, ele é inspirado no Capitão Fábio do filme Tropa de Elite, então alguns comandos tem referência com o personagem e com a profissão policial e o Bot Falador, ele só funciona em um canal de voz, tanto reproduz audios pré gravados como os do site myinstant(https://www.myinstants.com/pt/index/br/), como músicas baixadas no seu pc e também transforma a sua frase em áudio com a voz do Google.
Segue os links dos comandos dos bots:

### [Comandos Bot 02](https://github.com/IsabelaCardeal/BotDiscord/blob/master/Bot02.py) :policeman:
### [Comandos Bot Falador](https://github.com/IsabelaCardeal/BotDiscord/blob/master/Falador.py) :singer:

Eu já deixei alguns comentários e explicações nos arquivos. Mas logo abaixo vou colocar algumas explicações e variações possíveis.

<details>
<summary><b>BOT 02</b></summary> 
<br/>
Vou começar explicando a diferença em usar o comando com prefixo e sem, mtas pessoas preferem utilizar o prefixo para que não ocorra a interferência do bot em uma conversa ou pergunta ou frase no chat.

OBS.: Como o meu caso é um personagem eu botei alguns de propósito onde ele se "intromete" na conversa.

Vamos exemplificar algumas diferenças e como a falta do prefixo pode bagunçar tudo.

Nesse caso sempre que a mensagem começar com 06 ele irá responder, mesmo que vc escreva 0654848, 06belavista, só não vai funcionar se ecrever algum caractere antes.
```
@client.listen("on_message")
async def testa(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('06'):
        await message.channel.send('Xerife, O SENHOR É UM FANFARRÃO!!')
```
Nesse outro caso, sempre q vc utilizar o if + in message.content.lower(), não importa em qual parte da frase vc coloque o termo, o bot sempre vai responder. Exemplo:

```
@client.listen("on_message")
async def testa(message):
    if message.author == client.user:
        return
        
    if '06' in message.content.lower():
        await message.channel.send('Xerife, O SENHOR É UM FANFARRÃO!!')
```
Logo, se vc escrever 54654606 ou euqueria06 ele sempre vai retornar a msg - ' Xerife, .....' e é aí que pode ocorrer o conflito, as vezes a pessoa no chat só queria dizer a hr ou uma outra informação e o bot se "intrometeu" e respondeu.

Uma outra forma possível seria escrever somente o message.content daí o bot só irá responder se aparecer no chat exatamente o termo escolhido, não adianta escrever 065555 06 0800 ou 656 06, apenas 06 seria aceito. 

```
@client.listen("on_message")
async def testa(message):
    if message.author == client.user:
        return
        
    if message.content == '06':
        await message.channel.send('Xerife, O SENHOR É UM FANFARRÃO!!')
```
Agora vamos para o caso de fazer um bot q responda qdo utilizamos o prefixo, temos q começar com a definição do prefixo e em seguida ao async def sempre vai o comando desejado:

```
client = commands.Bot(command_prefix="!")

@client.command()
async def _06(ctx): #nesse caso em específico temos q botar o _ antes do número pq o Python não aceita somente número como identificador, nem caracteres especiais($,!,&) por isso até eles são boas escolhas para ser o prefixo.
    if ctx.message.guild:
        await ctx.send('Xerife, O SENHOR É UM FANFARRÃO!')

@client.command()
async def policia(ctx):
    if ctx.message.guild:
        await ctx.send('Puliça, P-U-L-I-Çeçidrilha-A!!')
```
**PS.: Vc pode usar os 2 métodos juntos, sem problemas, eu gosto de misturar com prefixo e sem, mas vai de cada um.**

Sobre o comando wanted, ele funciona como uma manipulação de imagens:
```
@client.command()
async def wanted(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author  #essas linhas servem para o caso da pessoa só escrever !wanted - ele irá retornar o comando c a imagem da pessoa q escreveu

    wanted = Image.open("Procurado1.jpg")
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((149, 148))
    wanted.paste(pfp, (102, 171))
    wanted.save("cara.jpg")
    await ctx.send(file=discord.File("cara.jpg"))
```
Seguindo a lógica do Bot 02(policial)...eu escolhi uma foto de PROCURADO/WANTED(acabei achando mais lgl as gringas estilo velho oeste), então o image.open vai pegar essa imagem escolhida, poderia ser qualquer uma outra...

![Procurado1](https://user-images.githubusercontent.com/102563782/168195235-d516029a-c4b2-46fe-b94b-be0c8adba4a2.jpg)

O user.avatar_url_as se refere a imagem de perfil do usuário, essa imagem vai ser "pega", "lida", "redefinida" e "colada" por cima da foto Procurado1.jpg, a parte do - pfp, (102, 171)) - significa: pfp é a foto e o 102,171 são as "coordenadas" do ponto onde será colada a foto, com isso vc pode manipular a vontade o ponto onde vai colocar a foto(no Paint vc consegue visualizar esses números no rodapé a esquerda escrito px dps dos números).

O wanted.save vai salvar a montagem criada no msm local da foto original, com isso sempre q vc der o comando um novo cara.jpg é criado, na vdd substituído pelo já existente.
Exemplos: sem escrever nada dps do comando e mandando o @ de alguém:

![Amostras](https://user-images.githubusercontent.com/102563782/168202158-71b5bd65-a0c0-4d1c-ad19-559a5c5c82c5.JPG)


## Quarta Parte

Nessa parte vou explicar um pouco sobre os comandos por voz que coloquei no Bot 02...eu aprendi por meio desse tutorial no youtube, ele ensina a criar um bot do zero, mas eu foquei principalmente na parte 3/4/5 onde ele fala sobre a reprodução de audio:

* [Tutorial Bot para o Discord em Python](https://www.youtube.com/watch?v=pL2EuhSV7tw)

No meu caso eu queria reproduzir arquivos como se fossem binds c memes, peguei vários arquivos do site MyInstant. E troquei o nome join e leave pela linguagem Q da polícia(QAP = Na escuta e QAR = Desligar) c/ um adicional de sempre que o bot entrar na sala ele irá reproduzir o arquivo mp3 escolhido.

**OBS.: O arquivo .mp3 SEMPRE tem q estar na mesma pasta do arquivo python!! O recomendado é sempre q iniciar um projeto criar uma pasta do projeto, daí vc coloca o arquivo .py, as imagens e os .mp3 junto.**

```
client = commands.Bot(command_prefix="!")


@client.command()
async def QAP(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('seuarquivoaqui.mp3')
        player = voice.play(source)
    else:
        await ctx.send('Você nem tá no canal certo o doida(o)!!')
# Se não quiser q ele reproduza o arquivo deixe o comando apenas com: channel = ctx.author.voice.channel
                                                                     #    await channel.connect()
                                                                 # else:
                                                                     #    await ctx.send('Você nem tá no canal certo o doida(o)!!')
                                                                     
@client.command()
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    song = arg + '.mp3'
    source = FFmpegPCMAudio(song)
    player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

@client.command()
async def QAR(ctx):
    if ctx.voice_client:
        await ctx.send('Tô vazando, vlw, flws!!')
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('Ainda bem que eu nem estou aí!!')
```
Com esses comandos(QAP e QAR) o bot se junta a vc, ele só vai pro canal de voz q vc estiver, se vc ñ estiver em nenhum ele não vai aparecer, por isso os else, tb não é possível trocar diretamente eles de canal...tem q dar o comando de sair e dps o de se juntar.
  

Bom esses foram alguns exemplos básicos, eu sou bem iniciante e não tenho tanto conhecimento assim porém estou estudando e praticando, sei q existe uma infinidade de possibilidades para a criação do comando, espero de alguma forma ter ajudado!!!
   

<div align="center">

![Satis](https://user-images.githubusercontent.com/102563782/167547545-c6e99b05-0e61-4096-b7fd-3240ab76b46c.jpg)

</details>

<details>    
<summary><b>BOT FALADOR</b></summary>
<br/>
    
Para o Bot reproduzir arquivos de áudio eu segui o passo a passo desse vídeo: https://www.youtube.com/watch?v=M_6_GbDc39Q, instalando o FFmpeg pelo site deles: https://ffmpeg.org/ e colocando a pasta com os .exe no diretório /C:, nos meus testes, arquivos .mp3, .wav e .ogg(áudios do whatsapp) reproduziram  de forma normal.
    
   
Primeiro vamos fazer com que o bot se junte a nós, por isso temos que já estar em um canal de voz para que ele te siga. Nesse comando nós podemos fazer ele básico, aonde ele só se junta a vc no canal de voz, ou com um som adicional sempre q ele se junta a vc no canal. Lembrando que todos os arquivos de audio devem ficar na mesma pasta que o arquivo do Bot.
    
Comando Básico:    
```
@client.command()
async def junto(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('Você nem tá no canal o doida(o)!!') 
```
Comando com áudio para tocar sempre q o bot entrar no canal de voz:
```
@client.command()
async def junto(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cheguei.mp3')
        player = voice.play(source)
    else:
        await ctx.send('Você nem tá no canal certo o doida(o)!!')   
```
PS.: Com esse comando se vc puxar o bot, trocar de canal de voz e tentar puxar novamente o bot, ele não irá te seguir, vc tem q dar o disconnect nele e "puxá-lo" novamente.

Os comandos seguintes são autoexplicativos, !fila cria a fila(ele vai botar o pedido na fila mas se não tiver nada tocando ele não vai dar o play!!!), precisa ter dado o comando !play para aí "acionar" a fila, sendo assim o !play toca a música, o !pause para a música e o !resume volta a tocar a música no momento do pause, o !stop para e tira a música, o !resume não funciona dps do stop.

Agora vou explicar sobre o gTTs(Google text-to-speech), no site da documentação tem todas as línguas e "sotaques" disponíveis, por padrão o sotaque do pt é o português brasileiro, por isso só precisei utilizar o lang="pt".
Documentação com as línguas e sotaques disponíveis: https://gtts.readthedocs.io/en/latest/module.html#localized-accents
    
Site onde achei a solução para o comando gTTs funcionar c o bot: https://localcoder.org/how-to-play-gtts-mp3-file-in-discord-voice-channel-the-user-is-in-discord-py    
    
```
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
```
    
Para trocar a língua basta alterar o lang...e para adicionar o sotaque escreva dps do lang: tld="..." 
    
PS.: Vc pode escrever o texto em francês, espanhol, alemão com a língua falada em português-br, porém o bot vai reproduzir como se fosse uma brasileira falando outras línguas, vai errar a pronúncia da acentuação e etc.
    
Aproveitando q esse comando primeiro salva a frase escrita e dps reproduz, vc pode criar e salvar frases aleatórias(como pensamento do dia, piadas, frases de filmes e etc), salvá-las e ir trocando o nome do arquivo, dps é só botar o comando com os arquivos salvos, assim como fiz no exemplo a seguir:
```
@client.command()
async def frase(ctx):
    frases = \
        ['frase1.mp3', 'frase2.mp3', 'frase3.mp3', 'frase4.mp3', 'frase5.mp3', 'frase6.mp3', 'frase7.mp3',
         'frase8.mp3', 'frase9.mp3', 'frase10.mp3']

    voice = ctx.guild.voice_client
    ria = random.choice(frases)
    player = voice.play(discord.FFmpegPCMAudio(ria))
```
Eu peguei 10 frases/pensamentos do dia e fui salvando, dps botei para reproduzir no random choice, mas vc pode nomear um comando para cada fala ou botar mto mais. 
    
 
Por fim o !leave tira o bot do canal de voz, com isso para trocar ele de canal basta dar o !leave e dps o !join.
    
E é isso...aproveite, divirta-se!!!
<p align="center">  
<img width="340" height="340" src="https://media.giphy.com/media/L3crA8hi8CdRyxZaSY/giphy.gif">
<p/> 
</details>
