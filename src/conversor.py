nomeArquivo = input('Digite o nome do arquivo: ')
with open(nomeArquivo, 'r') as conteúdoArquivo:
    linhas = conteúdoArquivo.readlines()

for linha in linhas:
    for caracter in linhas:
        while caracter != '.':
            break
        processaPonto(linha)