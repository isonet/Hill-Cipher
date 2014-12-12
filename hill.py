# coding=utf-8
import tools
from PIL import Image

__author__ = 'Paul Biester & Clément Villanueva'


def encrypt_text(message, key):
    # Nos messages sont seulement en majuscule
    message = message.upper()

    # Si la longueur du message n'est pas paire on ajoute un 'X'
    if len(message) % 2 != 0:
        message += '['

    # Creer une liste de couples
    couple = []
    for i in range(0, len(message)/2):
        couple.append(list(message[i*2:(i*2)+2]))

    # Initialiser la liste de sortie
    result = []
    for i in couple:
        result.append(i[:])

    # Parcours de chaque couple (enumerate retourne l'élément et un compteur i)
    for i, c in enumerate(couple):
        # Remplacer des espaces
        c[0] = '[' if (c[0] == ' ') else c[0]
        c[1] = '[' if (c[1] == ' ') else c[1]

        crypted = (ord(c[0])-65) * key[0][0] + (ord(c[1])-65) * key[0][1]
        crypted_mod = crypted % 27 + 65
        result[i][0] = chr(int(crypted_mod))

        crypted = (ord(c[0])-65) * key[1][0] + (ord(c[1])-65) * key[1][1]
        crypted_mod = crypted % 27 + 65
        result[i][1] = chr(int(crypted_mod))

        # Remplacer des espaces
        result[i][0] = ' ' if (result[i][0] == '[') else result[i][0]
        result[i][1] = ' ' if (result[i][1] == '[') else result[i][1]

    # Creer n string de retour
    return_string = ""
    for e in result:
        return_string += e[0] + e[1]

    return return_string


def decrypt_text(message, key):
    # Pour decrypter il suffit d'inverser la matrice clé
    return encrypt_text(message, tools.modMatInv(key, 27))


def encrypt_image(input_filename, output_filename, key):

    i = Image.open(input_filename)

    # Verifier le type de l'image
    if i.mode != 'L':
        print "Seulement des images du type echelle de gris sont supportés"

    # Retourne les pixels mais c'est pas une liste
    pixels_l = i.load()
    width, height = i.size

    pixels = []
    for x in range(width):
        for y in range(height):
            pixels.append(pixels_l[y, x])

    # Si la longueur du message n'est pas paire on ajoute un 'X'
    if len(pixels) % 2 != 0:
        pixels.append(0)

    # Creer une liste de couples
    couple = []
    for i in range(0, len(pixels)/2):
        couple.append(list(pixels[i*2:(i*2)+2]))

    # Initialiser la liste de sortie
    result = []
    for i in couple:
        result.append(i[:])

    # Parcours de chaque couple (enumerate retourne l'élément et un compteur i)
    for i, c in enumerate(couple):
        crypted = c[0] * key[0][0] + c[1] * key[0][1]
        crypted_mod = crypted % 256
        result[i][0] = crypted_mod

        crypted = c[0] * key[1][0] + c[1] * key[1][1]
        crypted_mod = crypted % 256
        result[i][1] = crypted_mod

    result_1d = []
    for e in result:
        result_1d.append(e[0])
        result_1d.append(e[1])

    im = Image.new('L', (height, width))
    im.putdata(result_1d)
    im.save(output_filename)


def decrypt_image(input_filename, output_filename, key):

    encrypt_image(input_filename, output_filename, tools.modMatInv(key, 256))


#def get_key_from_text(cleartext, cryptedtext):
#    AX = Y

def main():

    # LiCo. La matrice doit être inversible modulo 256/26
    key26 = [[11, 3], [8, 7]]
    key256 = [[253, 176], [65, 245]]

    crypted = encrypt_text("The quick brown fox jumps over the lazy dog", key26)
    print ("\nChiffree : ")
    print crypted

    r = decrypt_text(crypted, key26)
    print ("\nDechiffree : " )
    print r

    encrypt_image("data/original.png", "data/crypted.png", key256)

    decrypt_image("data/crypted.png", "data/clear.png", key256)


if __name__ == '__main__':
    main()
