import numpy
import numpy as np
import utils

__author__ = 'pbiester'

# http://asecuritysite.com/Coding/hill


def num2str(arr, dim):
    message = ""
    arr = numpy.array(arr)
    for i in range(0, len(arr)):
        for j in range(0, dim):
            char = chr(int(arr[i][j]) + 65)
            if char == '[':
                message += ' '
            else:
                message += char
    return message


def str2num(message):
    message = str(message).upper()
    arr = []
    for e in message:
        if e == ' ':
            arr.append(ord("[") - 65)
        else:
            arr.append(ord(e) - 65)
    return arr


def arr2matrix(arr, dim):
    arrnew = numpy.zeros(shape=(len(arr)/2, dim))

    for i in range(0, len(arr) / 2):
        for j in range(0, dim):
            arrnew[i][j] = arr[i*dim + j]
    return arrnew


def crypt(m, k):
    message = numpy.mat(m)
    key = numpy.mat(k)
    #a_inv = linalg.inv(message[0])
    produit = message * key
    produit %= 27
    return produit

#https://code.google.com/p/pysecret/source/browse/hill.py
def encrypt(message, matrix, encryption=True):
    """
    Hill encryption (decryption).
    """
    message = message.upper()
    if not utils.invertible(matrix):
        return "La matrice n'est pas inversible"
    if len(message) % 2 != 0:
        message += 'X'
    couple = [list(message[i*2:(i*2)+2]) for i in range(0, len(message)/2)]
    result = [i[:] for i in couple]
    if not encryption:
        # To decrypt, just need to inverse the matrix.
        matrix = utils.inverse_matrix(matrix)
    for i, c in enumerate(couple):
        if c[0].isalpha() and c[1].isalpha():
            result[i][0] = chr(((ord(c[0])-65) * matrix[0][0] + \
                                    (ord(c[1])-65) * matrix[0][1]) % 26 + 65)
            result[i][1] = chr(((ord(c[0])-65) * matrix[1][0] + \
                                    (ord(c[1])-65) * matrix[1][1]) % 26 + 65)
    return "".join(["".join(i) for i in result])

def encryptImage(message, matrix, encryption=True):
    """
    Hill encryption (decryption).
    """
    message = message.upper()
    if not utils.invertible(matrix):
        return "La matrice n'est pas inversible"
    if len(message) % 2 != 0:
        message += 'X'
    couple = [list(message[i*2:(i*2)+2]) for i in range(0, len(message)/2)]
    result = [i[:] for i in couple]
    if not encryption:
        # To decrypt, just need to inverse the matrix.
        matrix = utils.inverse_matrix(matrix)
    for i, c in enumerate(couple):
        if c[0].isalpha() and c[1].isalpha():
            result[i][0] = chr(((ord(c[0])) * matrix[0][0] + \
                                    (ord(c[1])) * matrix[0][1]) % 256)
            result[i][1] = chr(((ord(c[0])) * matrix[1][0] + \
                                    (ord(c[1])) * matrix[1][1]) % 256)
    return "".join(["".join(i) for i in result])

def main():



    key = [[11, 3], [8, 7]]


    crypted = encrypt("atesta", key)
    print("\nChiffree : " )
    print crypted

    r = encrypt(crypted, key, False)
    print("\nDechiffree : " )
    print r

    print encrypt(encrypt("Vivement les vacances !", [[11, 3], [8, 7]]), [[11, 3], [8, 7]], False)


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
