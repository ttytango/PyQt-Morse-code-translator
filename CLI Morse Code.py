def morse_func():
    morse = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        "'": '.----.',
        '/': '-..-.',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...',
        ':': '---...',
        ';': '-.-.-.',
        '=': '-...-',
        '+': '.-.-.',
        '-': '-....-',
        '_': '..--.-',
        '"': '.-..-.',
        '$': '...-..-',
        '!': '-.-.--',
        '@': '.--.-.',
        ' ': '/'
    }
    playing = True
    while playing:
        sentence = input("Please enter some text to encode: ")

        new_list = []
        sentence = sentence.lower()
        sentence_list = list(sentence)

        for c in sentence_list:
            for k, v in morse.items():
                if c == k:
                    new_list += v + "   "
        morse_translation = ''.join(new_list)

        print(morse_translation)

        answer = input("Would you like to play again (y/n)?")
        answer = answer.lower()
        if answer == "y":
            playing = True
        else:
            break


if __name__ == '__main__':
    morse_func()
