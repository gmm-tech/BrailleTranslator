points = {
    "a": [1],
    "b": [1, 2],
    "c": [1, 4],
    "d": [1, 4, 5],
    "e": [1, 5],
    "f": [1, 2, 4],
    "g": [1, 2, 4, 5],
    "h": [1, 2, 5],
    "i": [2, 4],
    "j": [2, 4, 5],
    "k": [1, 3],
    "l": [1, 2, 3],
    "m": [1, 3, 4],
    "n": [1, 3, 4, 5],
    "o": [1, 3, 5],
    "p": [1, 2, 3, 4],
    "q": [1, 2, 3, 4, 5],
    "r": [1, 2, 3, 5],
    "s": [2, 3, 4],
    "t": [2, 3, 4, 5],
    "u": [1, 3, 6],
    "v": [1, 2, 3, 6],
    "w": [2, 4, 5, 6],
    "x": [1, 3, 4, 6],
    "y": [1, 3, 4, 5, 6],
    "z": [1, 3, 5, 6],
    " ": [],
}

def text_to_braille(text):
    braille = ""  # string that will hold the braille characters

    for letter in text:  # for each letter in the text
        total = 0  # sum of the dot values for this letter
        for point in points[letter]:  # for each dot number of this letter
            total += 1 << (point - 1)  # shift 1 left (point - 1) places to get this dot's value

        braille += (chr(0x2800 + total)) 

    return braille

braille = text_to_braille(input("Type something: "))

print(braille)