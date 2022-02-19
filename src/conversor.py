def processaPonto(linhaPonto):
    linhaPonto = linhaPonto.strip()
    if linhaPonto[:5] == '.text':
        return 1
    return 0


def limpaArquivoPosText():
    with open('arquivoPosText', 'w') as arquivo:
        arquivo.write('')


nomeArquivo = input('Digite o nome do arquivo (com o .asm) que será convertido em linguagem de máquina: ')
limpaArquivoPosText()
pontoProcessado = False

with open(nomeArquivo, 'r') as conteúdoArquivo:
    linhas = conteúdoArquivo.readlines()
for linha in linhas:
    if not pontoProcessado:
        if processaPonto(linha) == 1:
            pontoProcessado = True
    else:
        ehComentario = linha.strip()
        if ehComentario == '' or ehComentario[0] != '#':
            with open('arquivoPosText', 'a') as adicionaNoArquivo:
                adicionaNoArquivo.write(linha)
