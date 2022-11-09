lista = ['a','b','c','d']
lista2 = []
lista3 = []
tamanho = int(len(lista)/2)

for i in range(tamanho):
    lista2 = lista[0:2]
    for i in lista[0:2]:
        lista.remove(i)
    lista3.append(''.join(lista2))
    print(lista2,i)
print(lista3)