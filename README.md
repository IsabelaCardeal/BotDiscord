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
* [Tutorial instalação e configuração Python e Pycharm](https://www.devmedia.com.br/instalacao-do-python/40643#:~:text=Na%20tela%20inicial%20do%20PyCharm,e%20depois%20em%20%E2%80%9CSettings%E2%80%9D.&text=Na%20nova%20tela%20da%20Figura,os%20nossos%20c%C3%B3digos%20em%20Python.)

## Terceira Parte
Agora nós vamos para o código em si, no meu caso, vou compartilhar o meu Bot 02, ele é inspirado no Capitão Fábio do filme Tropa de Elite, então alguns comandos tem referência com o personagem e com a profissão policial.
Segue o link do bot:

### [Bot 02](https://github.com/IsabelaCardeal/BotDiscord/blob/master/Finalizado.py) :policeman:

Eu já deixei alguns comentários e explicações no arquivo. Mas logo abaixo vou colocar algumas explicações e variações possíveis.

No caso o uso do intents não é obrigatório para um bot "caseiro", ele é pedido em bots q seja usado em mais de 100 servers.

Agora sobre a diferença em usar o comando com prefixo e sem, mtas pessoas preferem utilizar o prefixo para que não ocorra a interferência do bot em uma conversa ou pergunta ou frase no chat.

OBS.: Como o meu caso é um personagem eu botei alguns de propósito onde ele se "intromete" na conversa.

Vou exemplificar algumas diferenças e como a falta do prefixo pode bagunçar tudo.

Nesse caso sempre que a mensagem começar com 06 ele irá responder, mesmo que vc escreva 0654848, 06belavista, só não vai funcionar se ecrever algum caractere antes.
```
@client.listen("on_message")
async def testa(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('06'):
        await message.channel.send('Xerife, O SENHOR É UM FANFARRÃO!!')
```
Agora nesse, sempre q vc utilizar o if + in message.content.lower(), não importa em qual parte da frase vc coloque o termo, ele sempre vai responder. Exemplo:

```
@client.listen("on_message")
async def testa(message):
    if message.author == client.user:
        return
        
    if '06' in message.content.lower():
        await message.channel.send('Xerife, O SENHOR É UM FANFARRÃO!!')
```
Nesse caso se vc escrever 54654606 ou euqueria06 ou ele sempre vai retornar a msg - ' Xerife, .....' e aí que pode ocorrer o conflito, as vezes a pessoa no chat só queria dizer a hr ou uma outra informação e o bot se "meteu" e respondeu.

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
Bom esses foram alguns exemplos básicos, eu sou bem iniciante e não tenho tanto conhecimento assim porém estou estudando e praticando, sei q existe uma infinidade de possibilidades para a criação do comando, espero de alguma forma ter ajudado!!!

<div align="center">

![Satis](https://user-images.githubusercontent.com/102563782/167547545-c6e99b05-0e61-4096-b7fd-3240ab76b46c.jpg)



