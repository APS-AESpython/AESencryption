from tkinter.ttk import Style

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

# Declaração de Variaveis globais
global selectOpt, matriz, x, y

x = 0
y = 0

# Matriz STATE
matriz = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

def calculo():
    global inputKey, x, y
    for i in inputKey:
    
        i = format(ord(i), "x")
        matriz[x][y] = i
        x = x + 1
        if x > 3:
            x = 0
            y = y + 1
    #reatribuindo valores do x e y

    x = 0
    y = 0

    #impressão
    print('-' * 30)

    for l in range(0, 4):
        for c in range(0, 4):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()

def chave():
    #global entre funções
    global inputKey
    #inicio
    print(colored(0, 255, 0,"\nDigite o numero da operação a ser realizada\n"))
    print("1 - Chave de 16 caracteres (128bits)")
    print("2 - Chave de 24 caracteres (192bits)")
    print("3 - Chave de 32 caracteres (256bits)")
    selectOpt = (input("Digite uma opção: "))
    selectOpt = int(selectOpt)
    optvalidas = (1, 2, 3,)

    if selectOpt not in optvalidas:
        print(colored(255, 0, 0,'\nERRO, é necessário selecionar um numero listado'))
        chave()

    #chave 1

    if selectOpt == 1:
        # Input da chave de 16 caracteres (16bytes/128bits)
        print("\n OBRIGATORIO CHAVE DE 16 CARACTERES")
        inputKey = input("Digite uma chave de criptografia: ")

        while len(inputKey) != 16:
            print(colored(255, 0, 0, "Erro, chave de criptografia necessita ter 16 caracteres"))
            inputKey = input("Digite uma chave de criptografia de 16 caracteres: ")
        calculo()

    #chave 2

    if selectOpt == 2:
        # Input da chave de 24 caracteres (24bytes/192bits)
        print("\n OBRIGATORIO CHAVE DE 24 CARACTERES")
        inputKey = input("Digite uma chave de criptografia: ")

        while len(inputKey) != 24:
            print(colored(255, 0, 0, "Erro, chave de criptografia necessita ter 24 caracteres"))
            inputKey = (input("Digite uma chave de criptografia de 24 caracteres: "))
        calculo()
        
    #chave 3

    if selectOpt == 3:
        # Input da chave de 32 caracteres (32bytes/256bits)
        print("\n OBRIGATORIO CHAVE DE 32 CARACTERES")
        inputKey = input("Digite uma chave de criptografia: ")

        while len(inputKey) != 32:
            print(colored(255, 0, 0, "Erro, chave de criptografia necessita ter 32 caracteres"))
            inputKey = input("Digite uma chave de criptografia de 32 caracteres: ")
        calculo()

    #global entre funções
    return inputKey

chave()