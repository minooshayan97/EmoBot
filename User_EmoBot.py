import pickle

from utils.set_key import set_api_key_from_file
from bot import EmoBotUser_dialogue_cycle
from utils.questionnaire import generate_questionarre_txt_file
from utils.data_processing import createDataframe
from bot import Bot

def main():
    print("Waiting for the EmoBot setup. Please wait.")
    #set up dataframe for retrieval
    df = createDataframe("doc/doc3.txt")

    # Initiate the EmoBot
    emoBot_sysMessage = "You are a helpful mental health chat bot. You provide empathetic responses and provide advice to their issuse using context. You try to ask questions to determine if there were any signs of depression in the past 2 weeks."
    EmoBot = Bot(emoBot_sysMessage)

    # perform the conversation
    questionarre = EmoBotUser_dialogue_cycle(df, EmoBot, 'User')

    # save pickle files for future reference
    with open(f'outputs/QAUser.pkl', 'wb') as f:
        pickle.dump(questionarre, f)

    # generate questionarre
    generate_questionarre_txt_file('User', questionarre)

if __name__ == "__main__":
    set_api_key_from_file()
    main()