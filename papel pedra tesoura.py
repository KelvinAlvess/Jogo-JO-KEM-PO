from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)
print('''\nDigite sua opção\n
\033[31m[0]pedra
\033[33m[1]papel
\033[34m[2]tesoura\n''')
jogador = int(input('Qual sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('\033[33mO computador jogou:\t{:^30}'.format(itens[comp]))
print('\033[34mVocê jogou:        \t{:^30}\n'.format(itens[jogador]))
if comp == 0:
    if jogador == 0:
        print('\033[33mEMPATE!')
    elif jogador == 1:
        print('\033[34mPARABÉNS VOCÊ VENCEU!')
    elif jogador == 2:
        print('\033[31mINFELIZMENTE VOCÊ PERDEU!')
        print('nada')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
if comp == 1:
    if jogador == 0:
        print('\033[31mINFELIZMENTE VOCÊ PEREDEU!')
    elif jogador == 1:
        print('\033[33mEMPATE!')
    elif jogador == 2:
        print('\033[34mPARABÉNS VOCÊ VENCEU!')
    else:
        print('\33[31mJOGADA INVÁLIDA!')
if comp == 2:
    if jogador == 0:
        print('\033[34mPARABÉNS VOCÊ VENCEU!')
    elif jogador == 1:
        print('\033[31mINFELIZMENTE VOCÊ PERDEU!')
    elif jogador == 2:
        print('\033[33mEMPATE!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')

