abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 
'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cifra = []



print('Bem vindo ao programa que calcula o algoritmo de vigenere ')
while True:
    opcao = str(input('quer codificar ou decodificar? [C/D]')).upper().strip()[0]
    if opcao != 'D' and opcao != 'C':
        print('digite apenas D ou C por favor! vou repetir... ')
        continue

    elif opcao == 'C':
        vezes = 0
        txt = str(input('Diga-me o texto a ser codigicado: [acentos nao serao contados] ')).lower().strip()
        txt = txt.replace(' ', '')
        txtlist = list(txt)
        chave = str(input('me diga a chave de codigicacao: ')).lower()
        chave = chave.replace(' ', '')
        chavelist = list(chave)
        if len(chavelist) < len(txtlist):
            while len(txtlist) > len(chavelist):
                chavelist = chavelist + chavelist

        for c in txtlist:
            n1 = abc.index(txtlist[vezes])
            n2 = abc.index(chavelist[vezes])
            cdg = n1 + n2
            letracodigo = abc[cdg]
            cifra.append(letracodigo)
            vezes += 1
        palavra = ''.join(cifra)
        print(f'Seu texto {txt} com a chave {chave} codificado fica: {palavra}')
        cifra.clear()
        chavelist.clear()
        txtlist.clear()
        continue
    elif opcao == 'D':
        vezes = 0
        txt = str(input('me fala o texto que voce quer decodificar: ')).lower().strip()
        txt = txt.replace(' ', '')
        txtlist = list(txt)
        chave = str(input('me fala a chave que foi usada pra codificar o texto: ')).lower().strip()
        chave = chave.replace(' ', '')
        chavelist = list(chave)
        if len(chavelist) < len(txtlist):
            while len(txtlist) > len(chavelist):
                chavelist = chavelist + chavelist
        for c in txtlist:
            n1 = abc.index(txtlist[vezes])
            n2 = abc.index(chavelist[vezes])
            cdg = (n1 - n2) % 26
            letracodigo = abc[cdg]
            cifra.append(letracodigo)
            vezes += 1
        palavra = ''.join(cifra)
        print(f'Seu texto codificado "{txt}" com a chave "{chave}" codificado fica: {palavra}')
        cifra.clear()
        chavelist.clear()
        txtlist.clear()

        continue

    while True:
        opcao2 = str(input('quer codificar/decodificar mais textos? [S/N]: '))
        if opcao2 == 'S':
            usuario = 'S'
            break
        elif opcao2 == 'N':
            usuario = 'N'
            break
        else:
            print('digite apenas S ou N por favor, vou repetir...')
            continue
    if usuario == 'S':
        continue
    elif usario == 'N':
        break
