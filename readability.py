import re

def main():

    while True:

        text = input("Text: ")

        if len(text) > 0:

            break

    letters = count_letters(text)

    words = count_words(text)

    sentences = count_sentences(text)

    cl_index = round(0.0588 * ((letters/words)*100) - 0.296 * ((sentences/words)*100) - 15.8)

    if cl_index < 1:

        print("Before Grade 1")

    elif cl_index > 16:

        print("Grade 16+")

    else:

        print(f"Grade {cl_index}")

    return


def count_letters(target_text):

    pattern = re.compile('[a-z]', re.IGNORECASE)

    matches = pattern.findall(target_text)

    # print(len(matches))
    # letters = len(matches)

    return len(matches)


def count_words(target_text):

    pattern = re.compile('\w+')

    matches = pattern.findall(target_text)

    # words = len(matches)

    return len(matches)


def count_sentences(target_text):

    pattern = re.compile(r'[A-Z][^\.!?]*[.!?]')

    matches = pattern.findall(target_text)

    # sentences = len(matches)

    return len(matches)


if __name__ == "__main__":
    main()