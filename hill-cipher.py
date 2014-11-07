import numpy

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


# TODO
def decipher(m, k):
    message = numpy.mat(m)
    key = numpy.mat(k)

    print key

    print numpy.size(key, 0)
    print numpy.size(key, 1)

    a_inv = numpy.linalg.inv(key)

    print a_inv
    #print numpy.vec

    x = a_inv * message[0]

    x %= 27

    print x

    return a_inv


def main():
    key = [[2, 3], [7, 5]]

    print num2str(key, 2)

    code = str2num("atesta atesta")
    print code

    transformed = arr2matrix(code, 2)
    print transformed

    crypted = crypt(transformed, key)
    print(num2str(crypted, 2))

    #print decipher(crypted, key)


if __name__ == '__main__':
    main()
