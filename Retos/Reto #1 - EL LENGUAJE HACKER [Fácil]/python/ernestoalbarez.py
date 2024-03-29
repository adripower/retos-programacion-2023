def str_to_leet(input_string):
    leet = {
        'a': '4',
        'b': '13',
        'c': '[',
        'd': ')',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': ',_|',
        'k': '>|',
        'l': '1',
        'm': '/\\/\\',
        'n': '^/',
        'o': '0',
        'p': '|*',
        'q': '(_,)',
        'r': '12',
        's': '5',
        't': '7',
        'u': '(_)',
        'v': '/',
        'w': '\\/\\/',
        'x': '><',
        'y': 'j',
        'z': '2',
        '1': 'L',
        '2': 'R',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '6': 'b',
        '7': 'T',
        '8': 'B',
        '9': 'g',
        '0': 'o'
    }

    return ''.join(
        [leet[c] if c in leet else c for c in input_string.lower()]
    )
