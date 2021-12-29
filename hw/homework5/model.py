import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(text):
    response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt=text,
    temperature=0.3,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    return response["choices"][0]["text"]

#"Write a restaurant review based on these notes:\n\nName: The Blue Wharf\nLobster great, noisy, service polite, prices good.\n\nReview:"