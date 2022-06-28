from string import ascii_uppercase


def gerarChave(n):
    letras = ascii_uppercase  # alfabeto maiúsculo
    chave = {}  # dicionário da chave
    cnt = 0
    for i in letras:
        chave[i] = letras[(cnt + n) % len(letras)]
        cnt += 1
    return chave


def crip(chave, txt):
    cifra = ""
    for i in txt:
        if i in chave:
            cifra += chave[i]
        else:
            cifra += i
    return cifra


def dCrip(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey


def main():
    num = int(input('Digite a chave da mensagem --> '))
    key = gerarChave(num)

    texto = input('Digite um texto para ser codificado --> ').strip().upper()
    cifra = crip(key, texto)
    print(cifra)

    #dkey = gerarChave(26-num)

    # dkey = dCrip(key)
    #     texto = crip(dkey, cifra)
    #     print(texto)
    for k in range(26):
        dkey = gerarChave(k)
        msg = crip(dkey, cifra)
        print(f'{k + 1}ª --> {msg}')

    #     for k, v in key.items():
    #         print(k, v)


if __name__ == '__main__':
    main()
