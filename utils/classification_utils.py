from openai import OpenAI
import os

from .categories import categories

def promptForClassification(statement):
    prompt = f"This is a list of category numbers from 0 to 9, followed by what that category is about: {statement}\n Categories:"
    message = prompt
    for i in range(len(categories)):
        message += f"\n {i}." + categories[i]
    return message

def problemClassification(statement):
    message = promptForClassification(statement) + " write the category number only this statement belongs to."
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message + " write the category number only this statement belongs to.",
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=1,
    )
    cat = chat_completion.choices[0].message.content

    if cat.isnumeric() and len(cat)==1:
        return cat
    return '0'
