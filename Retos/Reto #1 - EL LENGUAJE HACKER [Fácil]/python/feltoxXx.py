# Reto #1: EL "LENGUAJE HACKER"

# 
#  Escribe un programa que reciba un texto y transforme lenguaje natural a
#  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
#  Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  con el alfabeto y los números en "leet".
#  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#

LEET = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

def translator(text):

    leet_text = ""

    for word in text:
        if word.upper() in LEET.keys():
            leet_text += LEET[word.upper()]
        else:
            leet_text += word

    return leet_text


if __name__ == '__main__':
    print(translator(input("Texto a traducir: ")))
