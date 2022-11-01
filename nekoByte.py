from discord.ext import commands
from discord.ext import commands, tasks
import discord

class myBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg_sent = False

        