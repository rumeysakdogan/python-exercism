def translate(text):
    """Translates from English to Pig Latin.

    Args:
        word (str): a given word

    Returns:
        str: pig latin version of given word.
    """
    vowels = ["a", "e", "o", "u", "i"]
    pig_word = ""

    for word in text.split():
        if word[0] in vowels:
            pig_word += word + "ay"
        if word[0] not in vowels:
            if word[:2] in ["yt", "xr"]:
                pig_word += word + "ay"
            elif word[1:3] == "qu":
                pig_word = word[3:] + word[:3] + "ay"
            elif len(word) == 2 and word[1] == "y":
                pig_word += word[1] + word[0] + "ay"
            elif word[1] in vowels:
                if word[:2] == "qu":
                    pig_word += word[2:] + word[:2] + "ay"
                else:
                    pig_word += word[1:] + word[0] + "ay"
            elif word[1] not in vowels:
                if word[2] == "y":
                    pig_word += word[2:] + word[:2] + "ay"
                elif word[2] not in vowels:
                    pig_word += word[3:] + word[:3] + "ay"
                else:
                    pig_word += word[2:] + word[:2] + "ay"

            if len(text.split()) != 1:
                pig_word += " "

    return pig_word.strip()
