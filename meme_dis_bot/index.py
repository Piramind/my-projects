import discord
import requests
import json
import random
import asyncio
from datetime import datetime, timedelta

TOKEN = '${TOKEN}'
CHANNEL_ID = '${CHANNEL_ID}'
MEME_API_URL = 'https://meme-api.herokuapp.com/gimme'

client = discord.Client()

async def send_meme():
    channel = client.get_channel(int(CHANNEL_ID))

    response = requests.get(MEME_API_URL)
    if response.status_code == 200:
        meme_data = json.loads(response.text)
        meme_url = meme_data['url']
        await channel.send(meme_url)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

    while True:
        current_time = datetime.now()
        target_time = current_time.replace(hour=8, minute=0, second=0, microsecond=0)  # Adjust the time here

        if current_time >= target_time:
            await send_meme()

            # Wait for 24 hours
            target_time += timedelta(days=1)
            time_to_wait = target_time - current_time
            await asyncio.sleep(time_to_wait.total_seconds())

        # Check every minute
        await asyncio.sleep(60)

client.run(TOKEN)
