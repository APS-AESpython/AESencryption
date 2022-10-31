# Matriz STATE
matrix = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

# Declaração Variaveis
inputKey = ''
y = 0
x = 0
selectOpt = 0

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
        while len(inputKey) == 0:
            print("\n OBRIGATORIO 16 CARACTERES")
            inputKey = str(input("Digite uma chave de criptografia: "))

            if len(inputKey)>16:
                print("Erro, maior do que o limite definido!!!")
                inputKey = ''
            elif len(inputKey)<16:
                print("Erro, menor do que o numero necessario de caracteres!!!")
                inputKey = ''

    elif selectOpt == 2:
        # Input da chave de 24 caracteres (24bytes/192bits)
        while len(inputKey) == 0:
            print("\n OBRIGATORIO 24 CARACTERES")
            inputKey = str(input("Digite uma chave de criptografia: "))

            if len(inputKey)>24:
                print("Erro, maior do que o limite definido!!!")
                inputKey = ''
            elif len(inputKey)<24:
                print("Erro, menor do que o numero necessario de caracteres!!!")
                inputKey = ''

    elif selectOpt == 3:
        # Input da chave de 32 caracteres (32bytes/256bits)
        while len(inputKey) == 0:
            print("\n OBRIGATORIO 32 CARACTERES")
            inputKey = str(input("Digite uma chave de criptografia: "))

            if len(inputKey)>32:
                print("Erro, maior do que o limite definido!!!")
                inputKey = ''
            elif len(inputKey)<32:
                print("Erro, menor do que o numero necessario de caracteres!!!")
                inputKey = ''

    else:
        print("Erro, opção inexistente")
        selectOpt = 0

# Inserindo a chave na matriz
for i in inputKey:
    # Converter a chave para hexadecimal e salvar na matriz
    #i = int(i, 16)
    #i = ord(i)
    i = format(ord(i), "x")
    matrix[x][y] = i
    x = x+1
    if x > 3:
        x = 0
        y = y + 1

print(matrix)