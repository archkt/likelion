import os
import openai

openai.api_key = "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"
# "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" # Not mine!!! Don't use it 

response = openai.Completion.create(
  engine="davinci",
  prompt="Create an outline for an essay about Walt Disney and his contributions to animation:\n\nI: Introduction",
  temperature=0.7,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response["choices"][0]["text"])