"""
Entry point for the bot. Run this file to get things started.
"""

import logging
import discord
from discord.ext import commands


log = logging.getLogger(__name__)
discord.utils.setup_logging()


class Bot(commands.Bot):
    """
    Bot class is the heart of operations
    """

    def __init__(self):
        super().__init__(
            command_prefix='>',
            intents=discord.Intents.all(),
        )
        
    async def on_ready(self):
        msg = 'Logged in as {0} (ID: {0.id})'.format(self.user)
        log.info(msg)
        
    async def load_cog(self):
        pass
    
    async def unload_cog(self):
        pass

    def run(self):
        self.start(token='')
        

if __name__ == '__main__':
    Bot().run()
