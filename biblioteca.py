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
    elif num == 0:
        return "Z"
    else:
        return "N"

def Somar(n1, n2):
    total = n1+n2
    print (total)

def Somar2(*num):
    soma=0
    for x in range(len(num)):
        soma+=num[x]
    print(soma)

def letras(texto):
    cont = 0
    for x in range (len(texto)-1,-1, -1):
        print(texto[x],end= " ")
        if texto[x] not in " ":
            cont+=1
    print(f"\n {cont}")

def listaRepetida(L):
    novaLista = []
    for x in L:
        if x not in novaLista:
            novaLista.append(x)
    print(10,12,12,31,4,4,5,31,6,7,6,8)
    print(novaLista)
