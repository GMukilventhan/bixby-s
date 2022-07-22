#!/usr/bin/python3
from Class.User import *
from Class.BbruteForce import *

Mukil = User("Z4d")


forcage = BbruteForce(Mukil)

# Allowed characters
stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
# Tab with 10 random words inside
passwordSet = ["man", "si", "v"]

print(forcage.brute_force_with_combinaison(stringType))
