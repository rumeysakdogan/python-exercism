def response(hey_bob):
    """Predicts response of Bob according to
    given phrase.

    Args:
        hey_bob (str): sentence said to Bob

    Returns:
        str: Bob's response
    """

    is_silent = True
    not_silent = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                  "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in hey_bob:
        if i in not_silent:
            is_silent = False

    if hey_bob.strip().endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif "" == hey_bob or hey_bob.isspace() and is_silent:
        return "Fine. Be that way!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
