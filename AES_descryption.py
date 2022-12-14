# Matriz da chave
matrixKey = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
#Matriz Galois Field
matrixGF = [
    [2,3,1,1],
    [1,2,3,1],
    [1,1,2,3],
    [3,1,1,2],
]
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)
# Declaração Variaveis
inputKey = ''
inputPhrase = []
selectOpt = 0
y = 0
x = 0
y1 = 0
x1 = 0
s_list = []
FinalList = []
vezes = 1
breakPhrase2 = []
breakPhrase3 = []

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

    elif selectOpt == 2:
        # Input da chave de 24 caracteres (24bytes/192bits)
        inputPhrase, inputKey = options(inputKey,24)

    elif selectOpt == 3:
        # Input da chave de 32 caracteres (32bytes/256bits)
        inputPhrase, inputKey = options(inputKey,32)

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
    # Reset matriz frase e variavel vezes
    matrixPhrase = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    vezes = 1

    # Quebra o input em partes de 16
    breakPhrase = inputPhrase[0:32]

    # Deleta cada indice de 0 a 16
    for i in inputPhrase[0:32]:
        inputPhrase.remove(i)

    for i in range(int(len(breakPhrase)/2)):
        print(i)
        breakPhrase2 = breakPhrase[0:2]
        for i in breakPhrase[0:2]:
            breakPhrase.remove(i)
        breakPhrase3.append(int(''.join(breakPhrase2),16))
        print(breakPhrase2,i)
        print(breakPhrase3)

    # Guarda a frase quebrada na matriz
    for i in breakPhrase3:
        matrixPhrase[x1][y1] = i
        x1 = x1+1
        if x1 > 3:
            x1 = 0
            y1 = y1 + 1
    x1 = 0
    y1 = 0
    print(matrixPhrase)

    # Criptografia
    #print(matrixPhrase, "Matriz Original")
    # Fazendo o xor da frase com a chave
    for i in range(4):
        for j in range(4):
            matrixPhrase[j][i] = matrixPhrase[j][i] ^ matrixKey[j][i]
    print(matrixPhrase, "Matriz depois do xor inicial")

    while vezes <= 1:
        # SubBytes (S-box)
        for l in range(len(matrixPhrase)):
            for j in range(4):
                for i in range(4):
                    for k in range(len(s_box)):
                        if hex(matrixPhrase[j][i]) == s_box[k]:
                            matrixPhrase[j][i] = s_box[k]

        print(matrixPhrase, "matriz xor depois da S_box")

        # ShiftRows
        matrixPhrase[0][1], matrixPhrase[1][1], matrixPhrase[2][1], matrixPhrase[3][1] = matrixPhrase[3][1], matrixPhrase[0][1], matrixPhrase[1][1], matrixPhrase[2][1]
        matrixPhrase[0][2], matrixPhrase[1][2], matrixPhrase[2][2], matrixPhrase[3][2] = matrixPhrase[2][2], matrixPhrase[3][2], matrixPhrase[0][2], matrixPhrase[1][2]
        matrixPhrase[0][3], matrixPhrase[1][3], matrixPhrase[2][3], matrixPhrase[3][3] = matrixPhrase[1][3], matrixPhrase[2][3], matrixPhrase[3][3], matrixPhrase[0][3]
        print(matrixPhrase, "matriz xor depois da ShiftRows")


        # MixColumns
        for j in range(4):
            for i in range(4):
                matrixPhrase[i][j] = matrixPhrase[i][j] ^ matrixGF[j][i]
        print(matrixPhrase, "matriz xor depois da Galois Field")

        # AddRoundKey
        for j in range(4):
            for i in range(4):
                matrixPhrase[i][j] = matrixPhrase[i][j] ^ matrixKey[j][i]
        print(matrixPhrase, "matriz xor depois da chave nova")
        #print(vezes)

        vezes = vezes + 1
    
    for j in range(4):
        for i in range(4):
            FinalList.append(matrixPhrase[i][j])

    print("LISTA FINAL: ",FinalList)

for i in range(len(FinalList)):
    FinalList[i] = chr(FinalList[i])

#print("acabou")
print("FRASE CRIPTOGRAFADA: ",''.join(FinalList))