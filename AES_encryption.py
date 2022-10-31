# Matriz STATE
matrix = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

# Declaração Variaveis
inputText = ''
y = 0
x = 0

# Input do texto de 16 caracteres (16bytes/128bits)
while len(inputText) == 0:
    print("\n MÁXIMO DE 16 CARACTERES")
    inputText = str(input("Digite um texto para ser criptografado: "))

    if len(inputText)>16:
        print("Erro, maior do que o limite de texto!!!")
        inputText = ''

# Inserindo texto na matriz
for i in inputText:
    # Converter o texto para hexadecimal e salvar na matriz
    #i = int(i, 16)
    #i = ord(i)
    matrix[x][y] = i
    x = x+1
    if x > 3:
        x = 0
        y = y + 1

print(matrix)