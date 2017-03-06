#!/usr/bin/python
# coding=utf-8
import hill

# LiCo. La matrice doit être inversible modulo 256/27
key27 = [[11, 3], [8, 7]]

chiffre = hill.encrypt_text("May the demogods be kind", key27)
dechifre = "May the demogods be kind"

print ("\nClé : ")
print key27

print ("\nPhrase chiffre : ")
print chiffre

print ("\nPhrase dechiffre: ")
print dechifre

print("\nAttaque...")

k = hill.attack_hill_bruteforce(chiffre, dechifre)
print "\nCle de chiffrement trouvee : " + str(k)