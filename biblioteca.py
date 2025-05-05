def piramide(num):
    for i in range (1, num + 1):
        for j in range(0,i):
            print(i, end= " ")
        print()

def vogais(texto):
    cont = 0
    for x in range (len(texto)):
        if texto[x]=="a" or texto[x]=="e" or texto[x]=="i" or texto[x]=="o" or texto[x]=="u":
            cont=cont+1
    print(cont)

def estoque(produto, qtd, valorUnitario):
    valorTotal = qtd*valorUnitario
    return produto, valorTotal

def verifinum (num):
    if num > 0:
        return "P"
    if num == 0:
        return "Z"
    else:
        return "N"


