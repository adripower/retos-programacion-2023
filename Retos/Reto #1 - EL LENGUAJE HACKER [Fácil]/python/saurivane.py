"""/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 """
 
letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0", " "]

valores=["4","I3","[",")","3","|=","&","#","1",",_|",">|","1","/\/\\","^/","0","|*","(_,)","I2","5","7","(_)","\/","\/\/","><","j","2","L","R","E","A","S","b","T","B","g","o", " "]

language_hacker = dict(zip(letras,valores))

print("Introduzca el texto a convertir")
convertir = input().lower()
resultado = ""
for letter in convertir:
    resultado += language_hacker[letter]

print("Su texto hackeado es "  + resultado)