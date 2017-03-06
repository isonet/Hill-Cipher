#!/usr/bin/python
# coding=utf-8
import hill

# LiCo. La matrice doit être inversible modulo 256/27
key27 = [[11, 3], [8, 7]]

phrase = "The quick brown fox jumps over the lazy dog"
print ("\nPhrase : ")
print phrase

crypted = hill.encrypt_text("The quick brown fox jumps over the lazy dog", key27)
print ("\nChiffree : ")
print crypted

clear = hill.decrypt_text(crypted, key27)
print ("\nDechiffree : " )
print clear