import random as r
import os
import time as tm

### mensagem inicial
os.system('cls') or None
print('============================\n!!!!!!!! JO-KEN-PO !!!!!!!!!\n============================\n') 
tm.sleep(2)
input('Pressione enter para começar ')               

### definicao das variaveis de contagem de placar
placar_player = 0
placar_cpu = 0

### coletar nome do jogador

os.system('cls') or None
player = input('Antes de começar, informe o seu nome: \n\n')

### lista para evidenciar as opções

lista = [
'0 - Papel',
'1 - Pedra',
'2 - Tesoura'
]

### loop com o jogo
while True:
    os.system('cls') or None
    escolha = int(input('Faça a sua jogada:\n0 - Papel | 1 - Pedra | 2 - Tesoura\n\n'))
       
    if escolha >= 0 and escolha <= 2:
        resposta_aleatoria = r.randint(0,2)
        if (escolha == 0 and resposta_aleatoria == 1) or (escolha == 1 and resposta_aleatoria == 2) or (escolha == 2 and resposta_aleatoria == 0):
            os.system('cls') or None
            print('Sua jogada foi {} e a jogada do Oponente foi {}!\n'.format(lista[escolha].split(' - ')[1],lista[resposta_aleatoria].split(' - ')[1]))
            tm.sleep(1)
            input('Pressione enter para continuar ')  
            os.system('cls') or None
            print('========================\nVocê venceu esta rodada!\n========================\n')
            tm.sleep(1)
            input('Pressione enter para continuar ')    
            placar_player += 1
            os.system('cls') or None
            print('=================\nPLACAR\n=================\n{}: {}\nCPU: {}\n=================\n'.format(player,placar_player,placar_cpu))
        elif (escolha == 0 and resposta_aleatoria == 2) or (escolha == 1 and resposta_aleatoria == 0) or (escolha == 2 and resposta_aleatoria == 1):
            os.system('cls') or None
            print('Sua jogada foi {} e a jogada do Oponente foi {}!\n'.format(lista[escolha].split(' - ')[1],lista[resposta_aleatoria].split(' - ')[1]))
            tm.sleep(1)
            input('Pressione enter para continuar ')  
            os.system('cls') or None
            print('========================\nVocê perdeu esta rodada!\n========================\n')
            tm.sleep(1)
            input('Pressione enter para continuar ')   
            placar_cpu += 1
            os.system('cls') or None
            print('=================\nPLACAR\n=================\n{}: {}\nCPU: {}\n=================\n'.format(player,placar_player,placar_cpu))
        elif (escolha == 0 and resposta_aleatoria == 0) or (escolha == 1 and resposta_aleatoria == 1) or (escolha == 2 and resposta_aleatoria == 2):
            os.system('cls') or None
            print('Sua jogada foi {} e a jogada do Oponente foi {}!\n'.format(lista[escolha].split(' - ')[1],lista[resposta_aleatoria].split(' - ')[1]))
            tm.sleep(1)
            input('Pressione enter para continuar ')  
            os.system('cls') or None
            print('=========================\nVocê empatou esta rodada!\n=========================\n')
            tm.sleep(1)
            input('Pressione enter para continuar ')   
            os.system('cls') or None
            print('=================\nPLACAR\n=================\n{}: {}\nCPU: {}\n=================\n'.format(player,placar_player,placar_cpu))
    elif escolha > 2 or escolha <0:
        os.system('cls') or None
        print('Escolha invalida. Repita o procedimento.') 
        continue              
    else:
       break
    
    tm.sleep(1)
    repeat = int(input('Deseja jogar novamente?\n 0 - Sim | 1 - Não\n\n'))
    if repeat == 0:
        continue
    else:
        break

### mensagem final após jogador optar por não prosseguir o jogo        
os.system('cls') or None
print('=================\nPLACAR FINAL\n=================\nPlayer: {}\nCPU: {}\n=================\n'.format(placar_player,placar_cpu))
tm.sleep(1)
input('Pressione enter para continuar ')   
os.system('cls') or None
print('===================\nObrigado por Jogar!\n===================')
tm.sleep(1)
os.system('cls') or None
### fim do Código