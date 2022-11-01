import datetime
import discord

def hiC(ctx, member):
    if member == None: # if no member is provided..
        member = ctx.author # make member the author
    nya=" Nya!!!!! =＾● ⋏ ●＾="
    hour=datetime.datetime.now()#extract the hour for the actual date time
    if(hour.hour<12):
        greeting="Buenos dias "
    if(hour.hour>=12 and hour.hour<19):
        greeting="Buenas tardes "
    if(hour.hour>=19):
        greeting="Buenas noches "
    greeting+=f"{member.mention} {nya}"
    return greeting


def purposeC(ctx):
    purpose="El internet es un lugar horrible Nya!!!, tanto yo NekoByte como mi creador SenpaiSuchil estamos aqui para hacerlo un lugar peor Nya!!!! (^・ω・^ )✧"
    return purpose

def danceC(ctx):
    member=ctx.author
    description=f"**{member.name}** está balando Nya!!!!! ฅ(*ΦωΦ*) ฅ"
    embed=discord.Embed(description=description, color=0xfa7fc1)
    embed.set_image(url="https://i.pinimg.com/originals/1f/9f/a8/1f9fa860ca43a0ad04348985660ae7c8.gif")
    return embed


def comfyC(ctx):
    member=ctx.author
    description=f"Parece que **{member.display_name}** está bastante comfy Nya!!!!! (=^-ω-^=)"
    embed=discord.Embed(description=description, color=0xfa7fc1)
    embed.set_image(url="https://i.pinimg.com/originals/32/eb/02/32eb021102883da780bad5b2d30bfc58.gif")
    return embed

def blushC(ctx):
    member=ctx.author
    description=f"oya oya???? parece que **{member.name}** se a sonrojado >.<"
    embed=discord.Embed(description=description, color=0xfa7fc1)
    embed.set_image(url="https://i.pinimg.com/originals/5f/7e/f9/5f7ef97c2b44bdb309f7b1fcabaa148f.gif")
    return embed

def backroomC(ctx, user):
    member=ctx.author    
    description=f"Con mis poderes de gato borracho **{member.display_name}** a enviado a **{user.display_name}** directo los *Backrooms*. Esperamos que sufras una muerte terrible por parte de las creaturas que habitan ahí Nya!!! (ฅ^･ω･^ ฅ)"
    embed=discord.Embed(description=description, color=0xfa7fc1)
    embed.set_image(url="https://i.pinimg.com/originals/d3/d5/a2/d3d5a2176e76462406b6c49b80c621d1.jpg")
    return embed