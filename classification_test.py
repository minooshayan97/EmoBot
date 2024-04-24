
from utils.set_key import set_api_key_from_file
from utils.classification_utils import problemClassification

def main():
    # Testing problem classification
    statements = [
        "hello",
        "i'm very happy today.",
        "It's so difficult to do so many things when I'm tired.",
        "I had a nightmare the other night.",
        "things are going as always.",
        " I am having trouble concentration, and also have been talking too fast",
        "I have been overeating and always sleepy and low energy"
    ]

    for s in statements:
        print(s)
        cat = problemClassification(s)
        #print(categories[int(cat)])
        print(cat)


if __name__ == "__main__":
    set_api_key_from_file()
    main()