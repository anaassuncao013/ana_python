def cript(nome, frase, valor_cripto):
    descritor = open (nome,"a")
    new_frase = ''
    for letra in frase:
        new_frase += chr((ord(letra)+valor_cripto)%127)
    descritor.write(new_frase)

def descrip (nome, valor_cripto):
    descritor = open (nome, "r")
    new_frase = ''
    for letra in descritor.read():
        new_frase += chr((ord(letra)-valor_cripto)%127)
    print(new_frase)

while True:
    a = "banco_01.txt"
    b = 10
    c = input("Digite aqui: ")

    if c == "cansei":
        break
    else:
        cript (a,c,b)
        descrip (a,b)