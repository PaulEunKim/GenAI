import responses
import generate_image
import discord


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


async def generate_ai(message, user_message, is_private):
    try:
        response = generate_image.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.reactions = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} {user_message} {channel}')

        # if user_message[0] == 'h':
        #     user_message = user_message[1:]  # [1:] Removes the '?'
        #     await send_message(message, user_message, is_private=False)

        if user_message[0:9] == 'generate ':
            user_message = user_message[9:]  # [1:] Removes the ''
            await generate_ai(message, user_message, is_private=False)
        else:
            await generate_ai(message, user_message, is_private=False)

    TOKEN = 'MTEyMDc4ODk5NTU2NDEwOTg0NQ.GoQiYh.tOjbrbLzjh-WZRgNjBoAYKq2qx26Jz9yW5vHjE'
    client.run(TOKEN)
