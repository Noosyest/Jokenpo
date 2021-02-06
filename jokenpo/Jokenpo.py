from interface import *
from time import sleep
from random import randint

jogador = 3
resposta = 'N'
show('Olá. Vamos jogar jokenpo!')

cabecalho('MENU PRINCIPAL')
while True:
	if resposta == 'N' or jogador == 3:
		escolha = menu(['Ranking', 'Jogar', 'Sair'])
		if escolha == 1:
			cabecalho('JOKENPO')
		if escolha == 2:
			break
	while True:
		computador = randint(0, 2)
		show('Qual você escolhe?')
		jogador = menu(['Pedra', 'Papel', 'Tesoura', 'Menu'])
		if str(jogador) in '0123':
			break
		elif not str(jogador) in '0123' and str(jogador).isnumeric():
			print('\033[31mERRO: Essa opção não existe :/\033[m')
			sleep(2)
	if jogador == 3:
		cabecalho('MENU PRINCIPAL')
		
	else:
		resultado = jokenpo(jogador_1 = jogador, jogador_2 = computador, nome_1='Você', nome_2='Computador')

		cabecalho('RESULTADO')

		count = 1
		for k, v in resultado.items():
			if count == 1:
				jogador = v
			else:
				computador = v
			count += 1
			print(f'\033[32m{k}: \033[33m{v}\033[m')

		vencedor(resultado)
		while True:
			resposta = sair(show('\033[34mQuer continuar? \033[m[S/N]: ', endl='', time=.01))
			if resposta in 'SN':
				break
			elif resposta != '0': 
				print('\033[31mERRO: Digite uma opção válida!\033[m')
		if resposta == 'S':
			show('Então vamos jogar de novo', time=.1)
			cabecalho('NOVO JOGO')
			
		if resposta == 'N':
			cabecalho('MENU PRINCIPAL')
		
		
		
		
		
		
		
