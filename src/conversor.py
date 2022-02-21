def ehText(linhaPonto):
    linhaPonto = linhaPonto.strip().lower()
    if linhaPonto[:5] == '.text':
        return 1
    return 0


def limpaArquivoPosText():
    with open('arquivoPosText', 'w') as arquivo:
        arquivo.write('')


def adicionaArquivoBinario(codigo):
    with open('arquivoConvertido', 'a') as arquivo:
        arquivo.write(f'{codigo} ')


def processaLinha(linha):
    for palavra in linha:
        if palavra == 'syscall':
            adicionaArquivoBinario('cod01syscall')
            #TODO
            #Pegar os códigos (syscall, add, addi, beq etc..) em binário e continuar a lógica
            #não esquecer a verificação das $ caso seja um add e etc...



limpaArquivoPosText()
pontoProcessado = False

with open('assembly.asm', 'r') as conteúdoArquivo:
    linhas = conteúdoArquivo.readlines()

for linha in linhas:
    if not pontoProcessado:
        if ehText(linha) == 1:
            pontoProcessado = True
    else:
        linhaFormatada = linha.strip().lower()
        if linhaFormatada != '' and linhaFormatada != '\n' and linhaFormatada[0] != '#':
            with open('arquivoPosText', 'a') as adicionaNoArquivo:
                adicionaNoArquivo.write(linhaFormatada + '\n')

with open('arquivoPosText', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        linha = linha.lower().split()
        processaLinha(linha)
