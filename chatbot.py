import discord
import openai_secret_manager
import openai

# Set up OpenAI API credentials
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["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"]

# Define the prompt to start the conversation
prompt = "Hello, how are you doing today?"

# Define the completion parameters
completion_parameters = {
    "prompt": prompt,
    "temperature": 0.7,
    "max_tokens": 50,
    "n_top": 1,
    "stop": "\n"
}

# Define a function to send a message to the chatbot and receive its response
def send_message(message):
    # Add the user's message to the prompt
    prompt_with_message = f"{prompt}\nUser: {message}\nBot:"

    # Use the OpenAI API to generate the bot's response
    response = openai.Completion.create(engine="davinci", **completion_parameters, prompt=prompt_with_message)

    # Extract the bot's response from the API response and return it
    bot_response = response.choices[0].text.strip()
    return bot_response

# Create a client object to connect to Discord
client = discord.Client()

# Add an event listener for the "ready" event, which is called when the bot is ready to start receiving messages
@client.event
async def on_ready():
    print(f"Bot is online and logged in as {client.user}")

# Add an event listener for the "message" event, which is called when a message is received
@client.event
async def on_message(message):
    # Ignore messages sent by the bot
    if message.author == client.user:
        return

    # Call the send_message() function to get a response from the chatbot
    response = send_message(message.content)

    # Send the bot's response back to the channel
    await message.channel.send(response)

# Run the bot using your Discord bot token
client.run("MTA5NTgwOTQ0Mjk0OTM3MDAwNg.Gg6Pr7.U72226WxS_1_b-qC_6YtJ1Uv0fP-JsUf0p_mKE")

