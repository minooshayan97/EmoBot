from utils.questionnaire import fillingQuestionarre
from utils.categories import categories
from utils.questions import questions
from utils.set_key import set_api_key_from_file


def main():

    QA = {
    '1': ["Yes, I have been feeling very interested in the things I used to enjoy. I used to love going out with friends and participating in activities, like now.",
    "i'm going out with lots of friends these days.", "no, i would like to work harder on my readings and asssignment."],

    '2': ["I'm feeling a bit down lately. I've been having trouble sleeping and it's been affecting my mood and focus during the day. I don't have any issues with my eating habits, but the lack of sleep is really getting to me.",
    "I've been feeling quite fatigued and low on energy lately. I find it hard to concentrate on my studies and I've been feeling more irritable than usual. It's been a struggle to get through the day without feeling overwhelmed by everything.",
    "I haven't really talked to anyone about how I've been feeling. I've been trying to handle it on my own, but it's been getting harder to cope with everything. That's why I decided to come to the university counseling services today. I realized that I need some help to work through these feelings and get back on track.",
    "Thank you for your support. I appreciate it. I've been feeling really drained and unmotivated lately. It's been a struggle to get out of bed in the morning and find the energy to attend classes or study. I used to be more driven and focused, but now everything feels like a chore. I just want to feel like myself again.",
    "Yes, I think seeking guidance from a professional could be really beneficial for me at this point. I've been struggling with these issues for a while now, and it's becoming increasingly difficult to manage on my own. I believe that working with a professional could help me explore more tailored strategies to improve my sleep and emotional well-being. Thank you for suggesting this - I will definitely consider reaching out for further support."],

    '3': ["I've tried some relaxation techniques like deep breathing and mindfulness exercises to help calm my mind before bedtime, but they haven't been very effective in improving my sleep quality. I've also been avoiding caffeine and screens before bed, but it's still a struggle to fall asleep and stay asleep throughout the night. I'm open to exploring more strategies to manage my emotions and improve my sleep, as I know how crucial they are for my overall well-being.",
    "To incorporate this positive mindset into my daily routine, especially in terms of improving my sleep quality, I plan to prioritize self-care practices that promote relaxation and stress reduction. This may include setting a consistent sleep schedule, creating a calming bedtime routine, and engaging in activities that help me unwind before bed. I also aim to practice mindfulness and gratitude to cultivate a positive mindset and reduce feelings of anxiety or overwhelm. By focusing on self-care and maintaining a positive outlook, I believe I can create a more conducive environment for better sleep and overall well-being. Thank you for your support and guidance in helping me develop these strategies.",
    "I feel motivated and encouraged to implement these strategies into my daily routine with the goal of improving my sleep quality and overall well-being. Your support and guidance have been invaluable in helping me develop these self-care practices, and I'm grateful for your encouragement along the way. If you have any additional tips or resources to enhance these strategies or if there are other ways you can support me in this process, I would greatly appreciate it. Knowing that I have someone to turn to for guidance and encouragement makes a significant difference in my journey towards well-being. Thank you for being a supportive listener and for your continued assistance."],

    '4': ["I haven't noticed any significant changes in my appetite. I still have a regular eating pattern and don't experience any major changes in my food intake. However, I have been feeling more irritable and on edge, which I think could be related to my lack of proper sleep. It's been difficult to manage my emotions and reactions to things, especially when I'm feeling so exhausted all the time.",
    "As an AI, I don't have a physical body or the ability to eat food, but I can provide information and support on nutrition-related topics. If you have any questions or need guidance on nourishing yourself through food, feel free to ask, and I'll do my best to assist you. Your well-being is important, and taking care of your nutritional needs is a vital part of maintaining overall health. Let me know how I can support you further in this area.",
    "Thank you for your understanding and willingness to provide support. I appreciate your offer to assist with nutrition-related topics if needed. Currently, my focus has been more on addressing my sleep issues and emotional well-being, but I recognize the importance of maintaining healthy eating habits for overall wellness. I haven't experienced any significant changes in my appetite or eating habits, but I will keep an eye on how I nourish myself through food as I continue to work on my well-being. If I have any questions or concerns about my eating habits in the future, I'll be sure to reach out. Thank you for your support and guidance."],
    }


    for k in QA.keys():
        print(categories[int(k)])
        cat = fillingQuestionarre(QA[k], k)
        print(f"On scale of 0 to 3, over the last 2 weeks, rate how often has this person been bothered by {questions[k]}: ", cat)
        print()

if __name__ == "__main__":
    set_api_key_from_file()
    main()
