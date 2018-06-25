import os
import discord
from ruamel import yaml
from datetime import datetime


error_message = f'''
config.yml not found.
Created {os.path.abspath('config.yml')}
Please edit config.yml with relevant info, then run again.
Press enter to close.
'''


try:
    with open('config.yml', 'r') as c:
        config = yaml.load(c, Loader=yaml.Loader)
except FileNotFoundError:
    with open('config.yml', 'w') as c:
        config = {
            'token': '',
            'guilds': [100000000000000000]
        }
        yaml.dump(config, c)
    print(error_message)
    input()
    exit()


client = discord.Client()


@client.event
async def on_message(message):
    if message.guild.id in config['guilds']:
        await message.guild.ack()
        print(f'Marked server {message.guild} as read at {datetime.now()}')


if __name__ == '__main__':
    client.run(config['token'], bot=False)
