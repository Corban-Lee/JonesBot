"""
Entry point for the bot. Run this file to get things started.
"""

import os
import logging
import logging.handlers
import discord
from discord.ext import commands


def setup_logging():
    """
    Setup logging for the bot.
    """
    
    # Setup logging
    log = logging.getLogger('discord')
    log.setLevel(logging.DEBUG)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    # Create the log file handler
    handler = logging.handlers.RotatingFileHandler(
        filename='logs/discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32MB
        backupCount=5
    )

    # Formatter for the log files
    datetime_format = '%d-%m-%Y %H:%M:%S'
    formatter = logging.Formatter(
        '[{asctime}] [{levelname:<8}] {name}: {message}', 
        datetime_format, style='{'
    )
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log

if __name__ == '__main__':
    log = setup_logging()
    
    # Create the bot
    bot = commands.Bot(
        command_prefix='!', intents=discord.Intents().all()
    )
    bot.remove_command('help')  # we wont be needing this
    
    # Load the cogs
    for filename in os.listdir('cogs/'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            
    @bot.event
    async def on_ready():
        """
        Call this function when the bot is ready to receive commands
        """
        output = f'Logged in as {bot.user} (ID: {bot.user.id})'
        log.info(output)

    # Startup the bot using the hidden token
    with open('TOKEN', 'r', encoding='utf-8') as f:
        token = f.read()
    bot.run(token=token)
