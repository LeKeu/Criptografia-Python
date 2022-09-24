from random import randint, choice
from string import ascii_lowercase, ascii_uppercase
import os
from pyperclip import copy


def criptografar(texto, chave):
    alfb = ascii_lowercase + ascii_uppercase
    txtCrip = ''
    for i in range(len(texto)):
        txtCrip += texto[i]
        for k in range(chave):
            txtCrip += choice(alfb)
    return txtCrip


def descriptografar(textoCrip, chave):
    descrip = [textoCrip[n] for n in range(0, len(textoCrip), chave + 1)]
    return ''.join(descrip)


if __name__ == "__main__":
    ficar = True
    while ficar:
        os.system('cls' if os.name == "nt" else 'clear')
        print("\nCRIPTOGRAFANDO DESCRIPITOGRAFANDO\n")
        esc = input("[1] Criptografar texto\n[2] Descriptografar texto\n[0] Sair\n- ")
        match esc:
            case '0':
                ficar = False
            case '1':
                txt = input("Texto a ser criptografado:\n- ").strip()
                chave = int(input("Chave a ser usada (número entre 1 e 10):\n- "))
                if 1 <= chave <= 10:
                    res = criptografar(txt, chave)
                    input(f"--> {res}\nFrase codificada copiada para o seu clipboard\nPressione qualquer tecla para continuar\n- ")
                    copy(res)
            case '2':
                print(
                    "IMPORTANTE\nO texto a ser descriptografado precisa ter sido criptografado por este código ou por "
                    "outro que utiliza a mesma lógica!\nDigite '0' para voltar.\nObrigada :D\n")
                txtC = input("Digite o texto a ser descriptografado:\n- ").strip()
                if txtC == '0':
                    print("Volte sempre!")
                else:
                    saber = input("Voce sabe a chave?\n[S] Sim\n[N] Nao\n- ").strip()
                    if saber in 'Ss':
                        chaveC = int(input("Chave a ser usada (número entre 1 e 10):\n- "))
                        if txtC == '0':
                            print("Pressione qualquer tecla para sair\n- ")
                        else:
                            if 1 <= chaveC <= 10:
                                res = descriptografar(txtC, chaveC)
                                input(f"--> {res}\nPressione qualquer tecla para continuar\n- ")
                            else:
                                print("Tente novamente")
                    elif saber in 'Nn':
                        for i in range(1, 11):
                            print(f"CHAVE {i} = {descriptografar(txtC, i)}")
                        input("\nPressione qualquer tecla para continuar\n- ")
            case other:
                print("Tente novamente")
