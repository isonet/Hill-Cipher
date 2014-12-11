# coding=utf-8
import numpy
import numpy as np
import utils

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

def encrypt_image(filename, key):

    from PIL import Image
    i = Image.open(filename)

    # Verifier le type de l'image
    if i.mode != 'L':
        print "Seulement des images du type echelle de gris sont supportés"

    # Retourne les pixels mais c'est pas une liste
    pixels_l = i.load()
    width, height = i.size

    pixels = []
    for x in range(width):
        for y in range(height):
            pixels = pixels_l[x, y]

    print pixels

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

def main():



    key = [[11, 3], [8, 7]]

    crypted = encryptText("atesta", key)
    print("\nChiffree : " )
    print crypted

    r = decryptText(crypted, key)
    print("\nDechiffree : " )
    print r



    from PIL import Image
    i = Image.open("image2.png")
    print i.mode

    pixels = i.load() # this is not a list, nor is it list()'able
    width, height = i.size

    pixelString = ""
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            #bw_value = int(round(sum(cpixel) / float(len(cpixel))))
            #print cpixel
            #print (cpixel)
            pixelString += (chr(cpixel))

    #print pixelString
    cr = encryptImage(pixelString, key)
    #print cr
    dcr = encryptImage(cr, key, False)

    strNum = ""
    for i in range(0, 256):
        print i
        strNum += chr(i)
    print strNum
    encStr = encrypt(strNum, [[11, 3], [8, 7]])
    print encStr
    decStr=""

    decStr += str(ord(encrypt(encStr[i], [[11, 3], [8, 7]], False)))
    print decStr
    if(i != ord(dec[0])):
        print "errorTEST"

    count=0
    cT = 0
    for c, d in zip(cr, dcr):
        cT += 1
        if(c != d):
            count += 1
            print "error"
    print str(count)
    print str(cT)
    #print dcr
    lstImage = numpy.zeros((width, height))
    count = 0
    c2 = 0
    for e in dcr:
        lstImage[c2] = ord(e)
        if(count > width):
            c2 += 1
            count = 0
        count += 1
        #lstImage.append(ord(e))

    print lstImage.shape
    #arrImage = numpy.asarray(lstImage)
    #arrImage = np.reshape(arrImage, (width, -1))
    #print arrImage

    img = Image.fromarray(lstImage, 'L')
    img.save('my.png')

    a = chr(255)
    print("\n\n" + str(a) + " : " + str(ord(a)))


if __name__ == '__main__':
    main()
