    if not ctx.author.voice: #if the user are not in a voice channel will display this message
        return await ctx.send("Necesitas estar en un canal de voz Nya!!! >.<")

    if not ctx.voice_client: #set de channel where the bot is gonna enter for first time
        vc: wavelink.Player=await ctx.author.voice.channel.connect(cls=wavelink.Player)#ay mi madre es el bicho
    else:
        vc: wavelink.Player=ctx.author.voice #if the bot is already in the voice chat will use the actual vc
    
    await vc.play(search)#search on the lavalink server for the song
    data=vc.track.info #get the dict of song's data for a display on a message
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
    embed.set_footer(text=user, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)#display the data on a message 




from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


def reminder():
    print('Tick! The time is: %s' % datetime.now())
    


async def scheduler(ctx):
    #localCtx=ctx
    scheduler = BlockingScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(reminder, 'interval', seconds=1)
    

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass