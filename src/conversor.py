def processaPonto(linhaPonto):
    linhaPonto = linhaPonto.strip()
    if linhaPonto[:5] == '.text':
        return 1
    return 0


nomeArquivo = input('Digite o nome do arquivo: ')
with open(nomeArquivo, 'r') as conteúdoArquivo:
    linhas = conteúdoArquivo.readlines()
for linha in linhas:
    linhaAposPonto = 0
    for caracter in linhas:
        linhaAposPonto += 1
        while caracter != '.':
            break

        if processaPonto(linha) == 1:
            #Significa que achou o .text, posso continuar o código daqui, mais fácil que chamar uma função
