# Matrizes
# Matriz da chave
matrixKey = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
# Matriz da Frase
matrixPhrase = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

# Variaveis
global bytesize_key, inputKey, inputPhrase, ultimo
bytesize_key = 0
inputKey = ''
inputPhrase = ''

y = 0
x = 0
y1 = 0
x1 = 0
init = 0
control = 0
index = 0
primeiro = 0
ultimo = 16

# Codigo

# Tipo de operação (Introdução)
def iniciar():
    # opções print
    print("\nDigite o tipo de operação a ser realizada")
    print("1 - Chave de 16 caracteres (128bits)")
    print("2 - Chave de 24 caracteres (192bits)")
    print("3 - Chave de 32 caracteres (256bits)")

    # Input da opção

    selectOpt = int(input("Digite uma opção: "))

    # Verificação do input

    selectOptlist = [1, 2, 3,] # lista de valores aceitaveis

    while selectOpt not in selectOptlist:
        print("\n \n \nErro, opção inexistente")
        iniciar()

    if selectOpt == 1:
        # Input da chave de 16 caracteres (16bytes/128bits)
        bytesize_key = 16
    elif selectOpt == 2:
        # Input da chave de 24 caracteres (24bytes/192bits)
        bytesize_key = 24
    else:
        # Input da chave de 32 caracteres (32bytes/256bits)
        bytesize_key = 32

    # Verificação e criação da chave

    print("\n OBRIGATORIO {} CARACTERES".format(bytesize_key))
    inputKey = str(input("Digite uma chave de criptografia: "))

    while len(inputKey) != bytesize_key:
        print("\n OBRIGATORIO {} CARACTERES".format(bytesize_key))
        inputKey = str(input("Digite uma chave de criptografia: "))
        

    inputPhrase = str(input("\nDigite uma frase para ser criptografada:"))

    savekeys()

    return bytesize_key, inputKey, inputPhrase

def savekeys():
    # Guardar chave de encriptação dentro da matriz
    for i in inputKey:
        i = ord(i)
        matrixKey[x][y] = i
        x = x+1
        if x > 3:
            x = 0
            y = y + 1
    # Guardar frase de encriptação dentro da matriz
    for i in matrixPhrase:
        i = ord(i)
        matrixKey[x][y] = i
        x = x+1
        if x > 3:
            x = 0
            y = y + 1
    print('fim')

iniciar()