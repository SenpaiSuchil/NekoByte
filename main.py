import discord

from music import *
from gestures import *
from nekoByte import *
import wavelink
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apikeys import * #import all the shit that apikeys.py has

intents = discord.Intents.all()
intents.members=True
nekoThreads={}
NekoByte = myBot(command_prefix='-', intents=discord.Intents().all())

TOKEN=DISCORD_TOKEN

def embed_maker(data, ctx):
    title=data['title']#title
    url=data['uri']#url, for some reason is called uri on the dict xd
    #length=time_converter(data['length'])#function that convert the seconds to a minutes
    length=int(data['length'])
    signature=time_converter(length)
    url_len=len(url)
    video_id=url[32:url_len]
    url_thumb=f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
    user=f"Pedido por: {ctx.author.display_name}"
    embed=discord.Embed(title="♫ Ahora suena: ", description=title, url=url)
    embed.set_thumbnail(url=url_thumb)
    embed.add_field(name="**Duración**", value=f"{signature['hour']}:{signature['minutes']}:{signature['sec']}")
    embed.set_footer(text=user, icon_url=ctx.author.avatar.url)
    return embed


def time_converter(time):
    length=int(time)/1000
    total=length/3600
    hour=0
    minute=0
    if(total>=1):
        hour=int(total)#
        
    minutes=(total-hour)*60
    if(minutes>=1):
        minute=int(minutes)#
    secs=(minutes-minute)*60
    sec=int(secs)#
    timestr={"hour": f"{hour}", "minutes": f"{minute}", "sec": f"{sec}"}
    return timestr

    

#NekoByte is the bot's name
#NekoByte=commands.Bot(command_prefix="-", intents=intents)#prefix



@NekoByte.event
async def on_ready(): # This function will notify when the bot is ready on the console
    await NekoByte.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="SenpaiSuchil"))
    print("NekoByte is ready Nya!!!!!")
    print("-----------------------------")
    NekoByte.loop.create_task(node_connect())#gonna connect to the lavalink server when the bot are ready

@NekoByte.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f"Node {node.identifier} is ready Nya!!!")

@NekoByte.event
# async def on_wavelink_track_end(player: wavelink.player, track: wavelink.Track, reason):
#     ctx=player.ctx
#     vc: player=ctx.voice_client

#     try:
#         next_song=vc.queue.get()
#         await vc.play(next_song)
#         data=vc.track.info #get the dict of song's data for a display on a message
#         embed=embed_maker(data, ctx)
#         await ctx.send(embed)
#     except:
#         #An exception when after the track end, the queue is now empty. If you dont do this, it will get error.
#         await vc.stop()
#         print("Queue Empty and stopped, isplaying = ",vc.is_playing())
#function to welcome new members----------
@NekoByte.event
async def on_member_join(member):
    guild = member.guild
    if(guild.system_channel is not None):#NekoByte will detect that one user join to the dscord server and she is gonna say hi to the new member
        msg=f"Bienvenido!!!! {member.mention} a {guild.name} Nya!!!!!. de antemano mi amo y yo pedimos una disculpa por las atrocidades que estas a punto de ver y experimentar Nya!!!!! ฅ(*ΦωΦ*) ฅ"
        await guild.system_channel.send(msg)

#function to alert that one member left
@NekoByte.event
async def on_member_remove(member):
    guild = member.guild
    if(guild.system_channel is not None):#NekoByte will detect that one user left the discord server and NekoByte will display a little cute message
        msg=f"El inutil de {member} acaba de irse a chingar a toda su reputisima madre de: {guild.name} Nya!!!!!. Esperamos que haya dejado este lugar bajo las peores circunstancias posibles Nya!!!!! ฅ(*ΦωΦ*) ฅ"#okay maybe not so cute as i want it
        await guild.system_channel.send(msg)

#this function gonna conect to a server for music streaming, its gonna be called on the event on_ready
async def node_connect():
    await NekoByte.wait_until_ready()
    await wavelink.NodePool.create_node(bot=NekoByte, host='127.0.0.1', port=2333, password='youshallnotpass', https=False)
    #we are running a lavalink server in the same server trying to make this faster than goin to a server in honduras

#function to greetings--------------------
@NekoByte.command(name='hi')
async def hi(ctx, member: discord.Member=None): # this function will greet you depending the hour the message will change
    greeting=hiC(ctx, member)#function from gestures.py
    await ctx.reply(greeting)

#purpose function-----------------------
@NekoByte.command(name='purpose')#function that will display a stupid ass shit about the NekoByte's purpose
async def purpose(ctx):
    purpose=purposeC(ctx)#function from gestures.py
    await ctx.send(purpose)


@NekoByte.command()
async def ping(ctx):
    await ctx.reply('Pong!')#pong
    #this thing will be display some server information on the future

#function that send a dancing gif
@NekoByte.command()
async def dance(ctx):
    #https://i.pinimg.com/originals/5f/7e/f9/5f7ef97c2b44bdb309f7b1fcabaa148f.gif - blush
    #https://i.pinimg.com/originals/1f/9f/a8/1f9fa860ca43a0ad04348985660ae7c8.gif - dance
    #https://i.pinimg.com/originals/32/eb/02/32eb021102883da780bad5b2d30bfc58.gif - comfy
    embed=danceC(ctx)#function from gestures.py
    await ctx.send(embed=embed)

@NekoByte.command()
async def comfy(ctx):
    embed=comfyC(ctx)#fucntion from gestures.py
    await ctx.send(embed=embed)

#function that send a dancing gif
@NekoByte.command()
async def blush(ctx):
    embed=blushC(ctx)
    await ctx.send(embed=embed)

@NekoByte.command()
async def backroom(ctx, user : discord.Member):
    embed=backroomC(ctx, user)
    await ctx.send(embed=embed)


@NekoByte.command()
async def schedule_start(ctx):
    embed=discord.Embed(title="Recordatorio Activado", description="Se recordará que deben de hacer estiramientos!!!!")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/bd/70/fb/bd70fbdab605d8cd9d4d4a2fb81530de.jpg")
    embed.add_field(name="**Duración:**", value=f"Cada Hora ")
    await ctx.send(embed=embed)
    reminder.start()

@NekoByte.command()
async def schedule_stop(ctx):
    reminder.stop()
    await ctx.send(f"recordatorio desactivado!!!!!")

@tasks.loop(seconds=10)
async def reminder():
    channel_to_upload_to = NekoByte.get_channel(997715893079506974)
    for i in range (5):
        await channel_to_upload_to.send("recordatorio activado **@everyone**!!!!!")

#music part:

#command for join into a voice chat
@NekoByte.command(pass_context=True)
async def join(ctx):
    if(ctx.author.voice):#if the author is in a voice channel
        channel=ctx.message.author.voice.channel#now the channel where the bot will enter is the same at the author
        await ctx.reply("YA LLEGÓ SU PAPA HIJOS DE SU PUTA MADRE")#a not very cute message saying that she is on the voice chat rn
        await channel.connect()#NekoByte will join with the author
    else:
        await ctx.reply("Necesitas estar en un canal de voz Nya!!! >.<")#gettin mad because the author are not in a voice channel

#command for leave the voice chat
@NekoByte.command(pass_context=True)
async def leave(ctx):
    if(ctx.voice_client):#if the bot is in a voice chat 
        await ctx.guild.voice_client.disconnect()#will disconnect
        await ctx.reply("Me voy >:c no sin antes tumbarte tu lavabo y robarme tu tanque de gas Nyaaaaaa!!!")#a cute message saying good bye :)
    else:
        await ctx.reply("Oye! no estoy en ningun canal de voz Nya! >:c")#gettin mad because she is not on a voice channel

#command for play music from youtube using lavalink
@NekoByte.command()
async def play(ctx: commands.Context, *, search: wavelink.YouTubeTrack):
    if not getattr(ctx.author.voice, "channel", None): #if the user are not in a voice channel will display this message
        return await ctx.send("Necesitas estar en un canal de voz Nya!!! >.<")

    elif not ctx.voice_client: #set de channel where the bot is gonna enter for the first time
        vc: wavelink.Player=await ctx.author.voice.channel.connect(cls=wavelink.Player)#ay mi madre es el bicho
    
    
    vc: wavelink.Player=ctx.voice_client #if the bot is already in the voice chat will use the actual vc
    await vc.play(search)
    data=vc.track.info #get the dict of song's data for a display on a message
    embed=embed_maker(data, ctx)
    await ctx.send(embed=embed)#display the data on a message
    vc.ctx = ctx
    #setattr(vc, "loop", False)

@NekoByte.command()
async def pause(ctx: commands.context):
    if not getattr(ctx.author.voice, "channel", None): #if the user are not in a voice channel will display this message
        return await ctx.send("Necesitas estar en un canal de voz Nya!!! >.<")

    elif not ctx.voice_client: #set de channel where the bot is gonna enter for the first time
        return await ctx.send("Muy grasioso pero ahorita no estoy de sonidera Nya! >:c")#ay mi madre es el bicho
    
    else:
        vc: wavelink.Player=ctx.voice_client #if the bot is already in the voice chat will use the actual vc
    
    await vc.pause()
    await ctx.send(f"El valedor **{ctx.author.display_name}** paró la musica para preguntar por el dueño de un chevy blanco que acaban de cristalear aca afuera Nya... (⁎˃ᆺ˂)")

@NekoByte.command()
async def resume(ctx: commands.context):
    if not getattr(ctx.author.voice, "channel", None): #if the user are not in a voice channel will display this message
        return await ctx.send("Necesitas estar en un canal de voz Nya!!! >.<")

    elif not ctx.voice_client: #if the bot are not playing any music will send a message
        return await ctx.send("Muy grasioso pero ahorita no estoy de sonidera Nya! >:c")#ay mi madre es el bicho
    
    else:
        vc: wavelink.Player=ctx.voice_client #if the bot is already in the voice chat will use the actual vc
    
    await vc.resume()
    await ctx.send(f"Ya dijeron que el chevy no era de aqui, que continue la bellakera Nya!!!!! ﾍ(=^･ω･^= )ﾉ")

@NekoByte.command()
async def stop(ctx: commands.context):
    if not getattr(ctx.author.voice, "channel", None): #if the user are not in a voice channel will display this message
        return await ctx.send("Necesitas estar en un canal de voz Nya!!! >.<")

    elif not ctx.voice_client: #if the bot are not playing any music will send a message
        return await ctx.send("Muy grasioso pero ahorita no estoy de sonidera Nya! >:c")#ay mi madre es el bicho
    
    else:
        vc: wavelink.Player=ctx.voice_client #if the bot is already in the voice chat will use the actual vc
    
    await vc.stop()
    await ctx.send(f"Banda ya llego la chota diciendo que le paremos al desmadre Nya... ฅ^•ﻌ•^ฅ")





NekoByte.run(TOKEN)


