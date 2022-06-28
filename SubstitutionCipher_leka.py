from string import ascii_uppercase
from random import randint


def generateKey():
    letters = ascii_uppercase
    cletters = list(letters)
    key = {}
    for l in letters:
        key[l] = cletters.pop(randint(0, len(cletters) - 1))
    return key


def encrypt(key, txt):
    cifra = ''
    for c in txt:
        if c in key:
            cifra += key[c]
        else:
            cifra += c
    return cifra


def get_dcrypr_key(key):
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey


key = generateKey()
print(key)
texto = input('Digite um texto para ser criptografado: ').upper().strip()
cifra = encrypt(key, texto)
print(cifra)
dkey = get_dcrypr_key(key)
mensagem = encrypt(dkey, cifra)
print(mensagem)

