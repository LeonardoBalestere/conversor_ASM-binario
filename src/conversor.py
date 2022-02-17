def processaPonto(linhaPonto):
    linhaPonto = linhaPonto.strip()
    if linhaPonto[:5] == '.text':
        return 1
    return 0


def iniciaProcessoConversão(linhas, linhaAposPonto):
    contadorLinhas = 0
    for linhaAtual in linhas:
        contadorLinhas += 1
        if contadorLinhas < linhaAposPonto:
            break

    #A partir daqui ele será e interpretará o código, pois está após o .text


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
            retorno = iniciaProcessoConversão(linhas, linhaAposPonto)
