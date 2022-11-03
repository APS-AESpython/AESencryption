# Variaveis
global ultimo, primeiro, matrixKey, matrixPhrase, x, y, x1, y2

bytesize_key = 0

ultimo = 16
primeiro = 0

y = 0
x = 0
y1 = 0
x1 = 0
init = 0
control = 0
index = 0

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





# Codigo

# Tipo de operação (Introdução)
def iniciar():
    global bytesize_key, inputKey, inputPhrase
    inputKey = ''
    inputPhrase = ''

    print(bytesize_key)

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
    global ultimo, primeiro, x1, y1, x, y

    #print('verificação1:', inputKey, inputPhrase, bytesize_key, '1', matrixKey, '2', matrixPhrase)

    # y coluna -- x linha
    # Guardar itens da chave na matriz
    for i in inputKey:
        i = ord(i)
        matrixKey[x][y] = i
        x = x+1
        if x > 3:
            x = 0
            y = y + 1
        
    
    
    print('matriz frase')
    while ultimo < len(inputPhrase)+16:
        # Guardar itens da frase na matriz
        breakPhrase = inputPhrase[primeiro:ultimo]
        for i in breakPhrase:
            i = ord(i)
            matrixPhrase[x1][y1] = i
            x1 = x1+1
            if x1 > 3:
                x1 = 0
                y1 = y1 + 1
        x1 = 0
        y1 = 0
        breakPhrase = 0
        primeiro = ultimo+1
        ultimo = ultimo+16
        
        verify()
        return matrixKey, matrixPhrase
                

    

def verify():
    
    print('matriz chave \n')
    for x in range(0, 4):
        for y in range(0, 4):
            print(f'[{matrixKey[x][y]:^5}]', end='')
        print()
    print('matriz frase \n')
    for i in range(0, 4):
            for j in range(0, 4):
                print(f'[{matrixPhrase[i][j]:^5}]', end='')
            print()
iniciar()