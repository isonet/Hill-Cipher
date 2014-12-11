# coding=utf-8
import numpy
import numpy as np
import utils
from PIL import Image

__author__ = 'pbiester'

# http://asecuritysite.com/Coding/hill




def encrypt_text(message, key):
    # Nos messages sont seulement en majuscule
    message = message.upper()

    # Verifier si la matrice clé est inversible
    if not utils.invertible(key):
        # TODO utiliser un throw exception
        return "La matrice n'est pas inversible"

    # Si la longueur du message n'est pas paire on ajoute un 'X'
    if len(message) % 2 != 0:
        message += 'X'

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
        crypted = (ord(c[0])-65) * key[0][0] + (ord(c[1])-65) * key[0][1]
        crypted_mod = crypted % 26 + 65
        result[i][0] = chr(crypted_mod)

        crypted = (ord(c[0])-65) * key[1][0] + (ord(c[1])-65) * key[1][1]
        crypted_mod = crypted % 26 + 65
        result[i][1] = chr(crypted_mod)

    # Creer n string de retour
    return_string = ""
    for e in result:
        return_string += e[0] + e[1]

    return return_string

def decrypt_text(message, key):
    # Pour decrypter il suffit d'inverser la matrice clé
    return encrypt_text(message, utils.inverse_matrix(key))

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

    # Verifier si la matrice clé est inversible
    if not utils.invertible(key):
        # TODO utiliser un throw exception
        return "La matrice n'est pas inversible"

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

    #key = utils.inverse_matrix(key)
    #print utils.inverse_matrix(key)
    #key = numpy.linalg.inv(key)
    key = [[197, 80], [47, 77]]

    # Verifier si la matrice clé est inversible
    #if not utils.invertible(key):
    #    # TODO utiliser un throw exception
    #    return "La matrice n'est pas inversible"

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
        result_1d.append(int(e[0]))
        result_1d.append(int(e[1]))

    im = Image.new('L', (height, width))
    im.putdata(result_1d)
    im.save(output_filename)

def main():

    # LiCo. La matrice doit être inversible modulo 256/26
    key26 = [[11, 3], [8, 7]]
    key256 = [[253, 176], [65, 245]]
    key256_inverse = [[197, 80], [47, 77]]

    crypted = encrypt_text("atesta", key26)
    print("\nChiffree : " )
    print crypted

    r = decrypt_text(crypted, key26)
    print("\nDechiffree : " )
    print r

    encrypt_image("data/original.png", "data/crypted.png", key256)

    decrypt_image("data/crypted.png", "data/clear.png", key256)



if __name__ == '__main__':
    main()
