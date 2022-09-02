"""
Cog to test some functionality.
"""

from discord.ext import commands


class Admin(commands.Cog):
    """
    Admin cog class
    """

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        """
        Method called when the cog has been loaded.
        """
        output = f'Loaded Cog (NAME: {self.__class__.__name__})'
        print(output)


async def setup(bot):
    """
    Setup function.
    Required for all cog files.
    Used by the bot to load this cog.
    """

    cog = Admin(bot)
    await bot.add_cog(cog)
