import openai
import random

# Set up OpenAI API credentials
openai.api_key = "INSERT YOUR API KEY HERE"

# Set up the OpenAI GPT-3 language model
model_engine = "text-davinci-002"
prompt = "Generate an inspirational quote:"
max_tokens = 50
temperature = 0.8

# Generate a random inspirational quote
def generate_quote():
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    quote = response.choices[0].text.strip()
    return quote

# Print 10 random inspirational quotes
for i in range(10):
    quote = generate_quote()
    print(f"{i+1}. {quote}")
