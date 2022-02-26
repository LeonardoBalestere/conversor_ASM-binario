def tipoJump(instrução):
    resultado = []
    opcode = tipoCodigo[instrução[0]][0]
    resultado.append(bin(opcode)[2:].zfill(6))

    endereço = int(instrução[1]) / 4
    imm = bin(endereço)[2:].zfill(26)
    resultado.append(imm)

    binario = ''.join(resultado)
    hexadecimal = hex(int('0b' + binario, 2))[2:].zfill(8)
    return hexadecimal, binario


def tipoRegReg(instrução):  # Tipo Registrador registrador
    resultado = []
    shift = 0

    opcode = tipoCodigo[instrução[0]][0]
    resultado.append(bin(opcode)[2:].zfill(6))

    if instrução[0] == 'sll' or instrução[0] == 'srl':
        shift = int(instrução[3])
        resultado.append(bin(opcode)[2:].zfill(5))

        rt = getRegistrador(instrução[2])
        resultado.append(bin(rt)[2:].zfill(5))

    elif instrução[0] == 'mul':
        rs = getRegistrador(instrução[2])
        resultado.append(bin(rs)[2:].zfill(5))

        rt = getRegistrador(instrução[3])
        resultado.append(bin(rt)[2:].zfill(5))

        resultado.append(bin(shift)[2:].zfill(10))

    elif instrução[0] == 'div':
        rs = getRegistrador(instrução[1])
        resultado.append(bin(rs)[2:].zfill(5))

        rt = getRegistrador(instrução[2])
        resultado.append(bin(rt)[2:].zfill(5))

        resultado.append(bin(shift)[2:].zfill(10))

    else:
        rs = getRegistrador(instrução[2])
        resultado.append(bin(rs)[2:].zfill(5))

        rt = getRegistrador(instrução[3])
        resultado.append(bin(rt)[2:].zfill(5))

        rd = getRegistrador(instrução[1])
        resultado.append(bin(rd)[2:].zfill(5))

        resultado.append(bin(shift)[2:].zfill(5))


    # func = insCodes[instrução[0]][1]
    # result.append(bin(func)[2:].zfill(6))

    binario = ''.join(resultado)
    hexadecimal = hex(int('0b' + binario, 2))[2:].zfill(8)
    return hexadecimal, binario


def tipoRegI(instrução):  # Tipo Registrador I
    resultado = []
    opcode = tipoCodigo[instrução[0]][0]
    resultado.append(bin(opcode)[2:].zfill(6))

    if instrução[0] == 'sw' or instrução[0] == 'lw':
        formataImm = instrução[2].split('(')

        rs = getRegistrador(formataImm[1][:-1])
        resultado.append(bin(rs)[2:].zfill(5))

        rt = getRegistrador(instrução[1])
        resultado.append(bin(rt)[2:].zfill(5))

        imm = bin(int(formataImm[0]))[2:]
        resultado.append(imm.zfill(16))

    else:
        rs = getRegistrador(instrução[2])
        resultado.append(bin(rs)[2:].zfill(5))

        rt = getRegistrador(instrução[1])
        resultado.append(bin(rt)[2:].zfill(5))

        if instrução[0] == 'beq':
            novoPc = (int(instrução[3]) - 4) / 4
            aux = bin(novoPc)[2:]
            resultado.append(aux.zfill(16))

        elif instrução[0] == 'andi' or instrução[0] == 'addi':
            aux = 0
            aux2 = bin(int(instrução[3])).find('0b')
            if aux2 != 0:
                aux = 1
            final = bin(int(instrução[3]))[aux2 + 2:]
            resultado.append(str(aux) + final.zfill(15))

    binario = ''.join(resultado)
    hexadecimal = hex(int('0b' + binario, 2))[2:].zfill(8)
    return hexadecimal, binario


def tipoMoveFrom(instrução):
    aux = 0
    resultado = []
    opcode = tipoCodigo[instrução[0]][0]
    resultado.append(bin(opcode)[2:].zfill(6))

    rs = getRegistrador(instrução[1])
    resultado.append(bin(rs)[2:].zfill(5))

    resultado.append(bin(aux)[2:].zfill(11))

    binario = ''.join(resultado)
    hexadecimal = hex(int('0b' + binario, 2))[2:].zfill(8)
    return hexadecimal, binario


def syscall(instruction):
    return '0x0000000c', '0o0000000000000000000000000001100'


registradores = {
    'zero': 0, 'at': 1, 'v0': 2, 'v1': 3,
    'a0': 4, 'a1': 5, 'a2': 6, 'a3': 7,
    't0': 8, 't1': 9, 't2': 10, 't3': 11,
    't4': 12, 't5': 13, 't6': 14, 't7': 15,
    's0': 16, 's1': 17, 's2': 18, 's3': 19,
    's4': 20, 's5': 21, 's6': 22, 's7': 23,
    't8': 24, 't9': 25, 'k0': 26, 'k1': 27,
    'gp': 28, 'sp': 29, 'fp': 30, 'ra': 31,
    'hi': 32, 'lo': 33
}

tipoCodigo = {
    'add': (0, 0x20), 'sll': (0, 0x00), 'and': (0, 0x24), 'nor': (0, 0x27),
    'or': (0, 0x25), 'slt': (0, 0x2a), 'srl': (0, 0x02), 'sub': (0, 0x22),
    'mul': (0, 0x72),

    'div': (0, 0x02),

    'mfhi': (0, 0x00), 'mflo': (0, 0x00),

    'addi': (0x8, 0), 'lw': (0X23, 0), 'beq': (0x4, 0), 'sw': (0x2b, 0),
    'subi': (0, 0), 'andi': (0xc, 0),

    'j': (0x2, 0)
}

tipoIntrodução = {
    'add': tipoRegReg, 'sll': tipoRegReg, 'and': tipoRegReg, 'nor': tipoRegReg,
    'or': tipoRegReg, 'slt': tipoRegReg, 'sll': tipoRegReg, 'srl': tipoRegReg,
    'sub': tipoRegReg, 'mul': tipoRegReg,

    'div': tipoRegReg,

    'mfhi': tipoMoveFrom, 'mflo': tipoMoveFrom,

    'addi': tipoRegI, 'lw': tipoRegI, 'beq': tipoRegI, 'sw': tipoRegI,
    'subi': tipoRegI, 'andi': tipoRegI,

    'j': tipoJump,

    'syscall': syscall
}


def getRegistrador(value):
    return registradores[value[1:]]


def getInstruções(linha):
    linhaSplit = linha.replace('\t', ', ')
    linhaSplit = linhaSplit[:-1].split(", ")
    for i in range(0, len(linhaSplit)):
        linhaSplit[i] = linhaSplit[i].strip()
    return linhaSplit


def converteParaHexadecimal(linha):
    linhaSeparada = getInstruções(linha)
    if linhaSeparada[0] == 'subi':
        linhaAntiga = linhaSeparada[:]
        linhaSeparada[0] = 'addi'
        linhaSeparada[3] = str(-1 * int(linhaSeparada[3]))
        print('taking ', linhaAntiga, 'as ---->', linhaSeparada)
    linhaConvertida = tipoIntrodução[linhaSeparada[0]](linhaSeparada)
    return linhaConvertida


def ehText(linhaPonto):
    linhaPonto = linhaPonto.strip().lower()
    if linhaPonto[:5] == '.text':
        return 1
    return 0


def limpaArquivo(arquivoLimpar):
    with open(arquivoLimpar, 'w') as arquivo:
        arquivo.write('')


def adicionaArquivoBinario(codigo):
    with open('arquivoConvertido', 'a') as arquivo:
        arquivo.write(f'{codigo}\n')


limpaArquivo('arquivoPosText')
limpaArquivo('arquivoConvertido')
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
        teste = converteParaHexadecimal(linha)
        adicionaArquivoBinario(teste)
