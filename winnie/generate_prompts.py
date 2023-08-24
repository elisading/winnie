import os
import openai


schema = {
    "type": "object",
    "properties": {
        "background": {
            "type": "string",
            "description": "Background information or context for the conversation"
        },
        "dialogue": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "human": {
                        "type": "string",
                    },
                    "bot": {
                        "type": "string"
                    }
                },
                "required": [
                    "human",
                    "bot"
                ]
            }
        }
    },
    "required": [
        "background",
        "dialogue"
    ]
}
openai.api_key = "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"

with open()


completion = openai.ChatCompletion.create(
  model="gpt-4-0613",
  messages=[
    {"role": "system", "content": "You are a sample text generator, who can synthetically generate background, human and bot dialogue."},
    {"role": "user", "content": f"Provide a background, human and bot dialogue based on the following context `{chunk}`"}
  ],
  functions=[{"name": "generate_sample", "parameters": schema}],
  function_call={"name": "generate_sample"},
  temperature=0,
)

print(completion.choices[0].message.function_call.arguments)