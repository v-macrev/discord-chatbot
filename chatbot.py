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

# Test the chatbot by sending it a message and printing its response
message = input("Say something to the chatbot: ")
response = send_message(message)
print(response)

# Run the bot using your Discord bot token
client.run("MTA5NTgwOTQ0Mjk0OTM3MDAwNg.Gg6Pr7.U72226WxS_1_b-qC_6YtJ1Uv0fP-JsUf0p_mKE")
