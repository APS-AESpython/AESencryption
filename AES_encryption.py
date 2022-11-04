# Matriz da chave
matrixKey = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

# Declaração Variaveis
inputKey = ''
inputPhrase = []
selectOpt = 0
y = 0
x = 0
y1 = 0
x1 = 0

# Função para input da chave e da frase 
def options(inputKey,tamanho):
    inputPhrase = []
    while len(inputKey) != tamanho:
        print("\n OBRIGATORIO {} CARACTERES".format(tamanho))
        inputKey = str(input("Digite uma chave de criptografia: "))
        if not len(inputKey) == tamanho:
            print('Tamanho de chave incorreto')
    if len(inputKey) == tamanho:
        inputPhrase = list(input("\nDigite uma frase para ser criptografada:"))
    return inputPhrase, inputKey

# Tipo de operação (Introdução)
while selectOpt == 0:
    print("\nDigite o tipo de operação a ser realizada")
    print("1 - Chave de 16 caracteres (128bits)")
    print("2 - Chave de 24 caracteres (192bits)")
    print("3 - Chave de 32 caracteres (256bits)")
    # Problema quando digita um caracter
    selectOpt = int(input("Digite uma opção: "))

    if selectOpt == 1:
        # Input da chave de 16 caracteres (16bytes/128bits)
        inputPhrase, inputKey = options(inputKey,16)
        print(inputPhrase, inputKey)

    elif selectOpt == 2:
        # Input da chave de 24 caracteres (24bytes/192bits)
        inputPhrase, inputKey = options(inputKey,24)
        print(inputPhrase, inputKey)

    elif selectOpt == 3:
        # Input da chave de 32 caracteres (32bytes/256bits)
        inputPhrase, inputKey = options(inputKey,32)
        print(inputPhrase, inputKey)

    else:
        print("Erro, opção inexistente")
        selectOpt = 0

# y coluna -- x linha
# Guardar itens da chave na matriz
for i in inputKey:
    i = ord(i)
    matrixKey[x][y] = i
    x = x+1
    if x > 3:
        x = 0
        y = y + 1

# Código para realizar a criptografia
while len(inputPhrase) != 0:
    # Matriz da Frase
    matrixPhrase = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]

    # Quebra o input em partes de 16
    breakPhrase = inputPhrase[0:16]

    # Deleta cada indice de 0 a 16
    for i in inputPhrase[0:16]:
        inputPhrase.remove(i)

    # Guarda a frase quebrada na matriz
    for i in breakPhrase:
        i = ord(i)
        matrixPhrase[x1][y1] = i
        x1 = x1+1
        if x1 > 3:
            x1 = 0
            y1 = y1 + 1
    x1 = 0
    y1 = 0

    # Resto da criptografia
    print(matrixPhrase)

print(matrixKey)
print("acabou")