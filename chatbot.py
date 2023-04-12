import discord
import openai
import os

# Set up the Discord client and ChatGPT API key
client = discord.Client()
openai.api_key = os.getenv("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")

# Define the function that sends messages using the ChatGPT API
async def generate_message(content):
    prompt = f"Conversation with a Discord user:\nUser: {content}\nAI:"
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
    return response["choices"][0]["text"]

# Define the function that runs when the bot is ready
@client.event
async def on_ready():
    print("Logged in as", client.user.name)

# Define the function that runs when a message is received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Generate a response using the ChatGPT API
    response = await generate_message(message.content)
    
    # Send the response back to the Discord channel
    await message.channel.send(response)

# Run the bot using your Discord bot token
client.run("MTA5NTgwOTQ0Mjk0OTM3MDAwNg.Gg6Pr7.U72226WxS_1_b-qC_6YtJ1Uv0fP-JsUf0p_mKE")
