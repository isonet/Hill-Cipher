#!/usr/bin/python
# coding=utf-8
import hill

# LiCo. La matrice doit être inversible modulo 256/27
key256 = [[253, 176], [65, 245]]

hill.encrypt_image("demo/original.png", "demo/crypted.png", key256)

hill.decrypt_image("demo/crypted.png", "demo/clear.png", key256)