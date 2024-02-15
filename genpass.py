import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>/[]*&$#@():{}^-_+=?!"

while True:
    try:
        len = int(input("Tamanho da senha?: "))
        qty = int(input("Quantidade de senhas?: "))
    except ValueError:
        print("Entrada invalida")
    else: 
        for x in range(0,qty):
            Passwd = ""
            for i in range(0,len):
                passchar = random.choice(char)
                Passwd = Passwd + passchar
            print("Senha gerada: ", Passwd)
        break


print("\n powered by @c-eduardo08")
