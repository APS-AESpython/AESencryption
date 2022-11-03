"""matriz = []

frase = str(input("Digite uma frase: "))
tamanho = len(frase)
print(tamanho, frase)
matriz = [[0,0,0,0]]*(int(tamanho/4))

print(matriz)"""
global x
x = 10

def bar():
    global x
    x = 15
    return x
bar()
print(x)
