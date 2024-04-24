from utils.set_key import set_api_key_from_file
from utils.augmentation import provide_context
from utils.data_processing import createDataframe

def main():
    df = createDataframe("doc/doc3.txt")

    inpts = [
        "I can't sleep well at night.",
        "every daya feels gloomy.",
        "I'm often so tired that I can't do anything."
    ]

    for inpt in inpts:
        print("Statement: ")
        print(inpt)
        print("Retrieved context: ")
        print(provide_context(df, inpt))


if __name__ == "__main__":
    set_api_key_from_file()
    main()