jogo = {'cima-E': ' ', 'cima=M': ' ', 'cima-D': ' ', 'meio-E': ' ', 'meio-M': ' ', 'meio-D': ' ', 'baixo-E': ' ', 'baixo-M': ' ', 'baixo-D': ' '}

def impBoard(board):
    print(board['cima-E'] + '|' + board['cima-M'] + '|' + board['cima-D'])
    print('-+-+-')
    print(board['meio-E'] + '|' + board['meio-M'] + '|' + board['meio-D'])
    print('-+-+-')
    print(board['baixo-E'] + '|' + board['baixo-M'] + '|' + board['baixo-D'])

vez = 'X'

for i in range(9):
    impBoard(jogo)
    print('eh a vez do ' + vez + 'qual a posição')
    move = input()
    jogo[move] = vez
    if vez == 'X':
       vez = '0'
    else:
       vez = 'X'

impBoard(jogo) 