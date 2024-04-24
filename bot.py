from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI

from utils.categories import categories
from utils.classification_utils import problemClassification
from utils.augmentation import new_subject, generate_augQuery, endConversation


import os

class Bot():
    def __init__(self, sys_message=None):
        self.messages = []
        if sys_message:
            self.set_sysMessage(sys_message)
        self.chat_api = ChatOpenAI(
                        openai_api_key=os.environ["OPENAI_API_KEY"],
                        model='gpt-3.5-turbo'
                        )

    def set_sysMessage(self, sys_message):
        self.system_message = SystemMessage(content=sys_message)
        # Initiating the bot from scratch if System Message has changed
        self.messages = [self.system_message]

    def handle_input(self, query):
        self.messages.append(HumanMessage(content=query.content))
        response = self.chat_api(self.messages)
        self.messages.append(response)
        return response
    
  

def EmoBotPatient_dialogue_cycle(df, EmoBot, PatientBot, depression_level):
    # Dialogue Cycle
    f = open(f"outputs/output{depression_level}.txt", "a")

    # Setting Dialogue Parameters
    should_talk = [f'{i}' for i in range(1,10)]
    chain = ["-1", "0"]
    questionarre = {f'{i}':[] for i in range(1,10)}
    end_flag = False

    # Initiate EmoBot Dialogue
    ai_message = EmoBot.handle_input(HumanMessage(content="Hi"))

    while end_flag != True:
        # Store EmoBot message
        print("EmoBot>>>> " + ai_message.content)
        print("EmoBot>>>> " + ai_message.content, file=f)
        print(file=f)

        # Generate and Store Patient Response
        user_inpt = PatientBot.handle_input(ai_message)
        print("Patient>>" + user_inpt.content)
        print("Patient>>" + user_inpt.content, file=f)
        print(file=f)

        inpt_topic = problemClassification(user_inpt.content)
        print(f'*** Current Topic = {inpt_topic}.{categories[int(inpt_topic)]}***', file=f)

        if inpt_topic != "0" or chain.count("0")<3:
            topic = inpt_topic

        if topic != "0":
            questionarre[topic].append(user_inpt.content)

        chain.append(topic)

        if chain[-1] == chain[-2] or chain.count(topic)>=2:
            #change the subject
            #empty_keys = [key for key, value in questionarre.items() if not value]
            # added empty key check to ensure all questionnaire items received a reply
            if topic in should_talk:# and topic not in empty_keys:
                should_talk.remove(topic)
                print(f'--- topic {topic} removed', file=f)

            if len(should_talk) == 0: # changed this to include if one question is empty.
                #end the conversation properly
                augmented_prompt = endConversation(user_inpt)
                end_flag = True
            else:
                nxt = should_talk[0]
                print(f'+++ next:{nxt}', file=f)
                augmented_prompt = new_subject(df, user_inpt.content, topic, nxt)
                topic = nxt
        else:
            # continue the current thread
            augmented_prompt = generate_augQuery(df, user_inpt.content, topic)

        print("\n"+ augmented_prompt+ "\n")

        print('*********', file=f)
        print("should_talk :", file=f)
        print(should_talk, file=f)
        print("chain :", file=f)
        print(chain, file=f)
        print('*********', file=f)

        ai_message = EmoBot.handle_input(HumanMessage(content=augmented_prompt))
    return questionarre


def EmoBotUser_dialogue_cycle(df, EmoBot, user):
    # Dialogue Cycle
    f = open(f"outputs/output{user}.txt", "a")

    # Setting Dialogue Parameters
    should_talk = [f'{i}' for i in range(1,10)]
    chain = ["-1", "0"]
    questionarre = {f'{i}':[] for i in range(1,10)}
    end_flag = False

    # Initiate EmoBot Dialogue
    ai_message = EmoBot.handle_input(HumanMessage(content="Hi"))

    print("You are talking to EmoBot. If you wish to exit the conversation, please type in the word: exit")

    while end_flag != True:
        # Store EmoBot message
        print("EmoBot>>>> " + ai_message.content)
        print("EmoBot>>>> " + ai_message.content, file=f)
        print(file=f)

        # Get and Store User Response
        user_inpt = input("User>>")
        print("User>>" + user_inpt, file=f)
        print(file=f)
        if user_inpt=="exit":
            end_flag = True

        inpt_topic = problemClassification(user_inpt)
        print(f'*** Current Topic = {inpt_topic}.{categories[int(inpt_topic)]}***', file=f)

        if inpt_topic != "0" or chain.count("0")<3:
            topic = inpt_topic

        if topic != "0":
            questionarre[topic].append(user_inpt)

        chain.append(topic)

        if chain[-1] == chain[-2] or chain.count(topic)>=2:
            #change the subject
            #empty_keys = [key for key, value in questionarre.items() if not value]
            # added empty key check to ensure all questionnaire items received a reply
            if topic in should_talk:# and topic not in empty_keys:
                should_talk.remove(topic)
                print(f'--- topic {topic} removed', file=f)

            if len(should_talk) == 0: # changed this to include if one question is empty.
                #end the conversation properly
                augmented_prompt = endConversation(user_inpt)
                end_flag = True
            else:
                nxt = should_talk[0]
                print(f'+++ next:{nxt}', file=f)
                augmented_prompt = new_subject(df, user_inpt, topic, nxt)
                topic = nxt
        else:
            # continue the current thread
            augmented_prompt = generate_augQuery(df, user_inpt, topic)

        print("\n"+ augmented_prompt+ "\n", file=f)

        print('*********', file=f)
        print("should_talk :", file=f)
        print(should_talk, file=f)
        print("chain :", file=f)
        print(chain, file=f)
        print('*********', file=f)

        ai_message = EmoBot.handle_input(HumanMessage(content=augmented_prompt))
    return questionarre