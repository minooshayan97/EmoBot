from openai import OpenAI
import os
from .categories import categories
from .questions import questions

def promptForQuestionarre(statements, Q):
    qna = ' '.join(statements)
    prompt = f"Here are given some questions and answers related to {categories[int(Q)]} as a factor of mental health well-being. How would you rate the following question about this person?"
    message = prompt + "\n questions and answers:" + qna + f"\n On scale of 0 to 3, over the last 2 weeks, rate how often has this person been bothered by {questions[Q]}."
    message += "0: Not at all, 1: Several days, 2: More than half the days, 3: Nearly every day"
    return message

def fillingQuestionarre(statements, Q):
    message = promptForQuestionarre(statements, Q)
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message + "ONLY output the number 0 to 3.",
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=1,
    )
    rate = chat_completion.choices[0].message.content
  
    if (rate.isnumeric()):
        return rate

    return 'not enough data to respond.'


def generate_questionarre_txt_file(depression_level, questionarre):
    f = open(f"outputs/questionarre{depression_level}.txt", "a")
    for k in questionarre.keys():
        print(categories[int(k)], file=f)
        cat = fillingQuestionarre(questionarre[k], k)
        print(f"On scale of 0 to 3, over the last 2 weeks, rate how often has this person been bothered by {questions[k]}: " + cat , file=f)
        print(file=f)
