"""
Entry point for the bot. Run this file to get things started.
"""

import os
import queue
import asyncio
import logging
import logging.handlers
import discord
from discord.ext import commands


def setup_logging():
    """
    Setup logging for the bot.
    [THIS CURRENTLY DOES NOT WORK AS I AM TRYING TO WORK OUT ASYNC LOGGING]
    """
    
    # Setup logging
    log = logging.getLogger('discord')
    log.setLevel(logging.DEBUG)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    log_queue = queue.Queue(-1)

    # Create the log file handler
    handler = logging.handlers.RotatingFileHandler(
        filename='logs/discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32MB
        backupCount=5
    )
    
    queue_listener = logging.handlers.QueueListener(log_queue, handler)
    queue_listener.start()

    # Formatter for the log files
    datetime_format = '%d-%m-%Y %H:%M:%S'
    formatter = logging.Formatter(
        '[{asctime}] [{levelname:<8}] {name}: {message}', 
        datetime_format, style='{'
    )
    handler.setFormatter(formatter)
    log.addHandler(handler)

async def main():
    """
    Main function.
    """

    # Create the bot
    bot = commands.Bot(
        command_prefix='!', intents=discord.Intents().all()
    )
    bot.remove_command('help')  # we wont be needing this
    
    # Load the cogs
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

    @bot.event
    async def on_ready():
        """
        Automatically called when the bot is ready.
        """
        output = f'Logged in as {bot.user} (ID: {bot.user.id})'
        print(output)

    # Startup the bot using the hidden token
    with open('TOKEN', 'r', encoding='utf-8') as f:
        token = f.read()

    await bot.start(token=token)


if __name__ == '__main__':
    asyncio.run(main())