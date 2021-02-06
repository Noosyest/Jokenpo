from time import sleep

def corrente(msg, tam=4):
	print(f'{"-="*tam} {msg} {"-="*tam}')


def show(msg, endl='\n', time=.05):
	for l in msg:
		print(f'{l}', end='', flush=True)
		sleep(time)
	print(endl, end='')
	return ''


def leiaInt(msg, repeat=False):
	if not repeat:
		try:
			num = int(input(msg))
		except:
			print('\033[31mERRO: Essa opção não é válida :/\033[m')
			sleep(2)
		else:
			return num
	else:
		while True:
			try:
				num = int(input(msg))
			except:
				print('\033[31mERRO: Essa opção não é válida :/\033[m')
				sleep(2)
			else:
				return num


def cabecalho(msg, tam=42):
	print('-'*tam)
	print(msg.center(tam))
	print('-'*tam)
	

def menu(lista):
	for c, i in enumerate(lista):
		print(f'\033[33m{c}- \033[34m{i}\033[m')
	num = leiaInt(show('\033[32mSua opção: \033[m', endl=''))
	return num


def jokenpo(jogador_1, jogador_2, nome_1='jogador_1', nome_2='jogador_2'):
	show('JOKEN', endl='')
	show('...', time=1)
	print('PÔ!')
	sleep(.5)
	jogadores = [jogador_1, jogador_2]
	resultado = dict()
	opcoes = ['PEDRA','PAPEL', 'TESOURA']
	jogador_1 = opcoes[jogador_1]
	jogador_2 = opcoes[jogador_2]
	resultado[nome_1] = jogador_1
	resultado[nome_2] = jogador_2
	
	return resultado



def vencedor(dic):
	count = jogador_1 = jogador_2 = 0
	for k, v in dic.items():
		if count == 0:
			jogador_1 = v
		else:
			jogador_2 = v
		count += 1
	if jogador_1 == jogador_2:
		cabecalho('EMPATE')
		show(f'\033[33mAMBOS ESCOLHERAM {jogador_1}\033[m',time=.01)
	elif jogador_1 == 'PEDRA' and jogador_2 == 'TESOURA':
		corrente('PARABÉNS!')
		show('\033[32mVOCÊ VENCEU!',time=.1)
		show(f'O COMPUTADOR ESCOLHEU {jogador_2} E VOCÊ ESCOLHEU {jogador_1}\033[m',time=.01)
	elif jogador_1 == 'TESOURA' and jogador_2 == 'PEDRA':
		corrente('QUE PENA')
		show('\033[31mVOCÊ PERDEU!',time=.1)
		show(f'O COMPUTADOR ESCOLHEU {jogador_2} E VOCÊ ESCOLHEU {jogador_1}\033[m',time=.01)
	elif jogador_1 == 'TESOURA' and jogador_2 == 'PAPEL':
		corrente('PARABÉNS!')
		show('\033[32mVOCÊ VENCEU!',time=.1)
		show(f'O COMPUTADOR ESCOLHEU {jogador_2} E VOCÊ ESCOLHEU {jogador_1}\033[m',time=.01)
	elif jogador_1 == 'PAPEL' and jogador_2 == 'TESOURA':
		corrente('QUE PENA')
		show('\033[31mVOCÊ PERDEU!',time=.1)
		show(f'O COMPUTADOR ESCOLHEU {jogador_2} E VOCÊ ESCOLHEU {jogador_1}\033[m',time=.01)
	elif jogador_1 == 'PAPEL' and jogador_2 == 'PEDRA':
		corrente('PARABÉNS!')
		show('\033[32mVOCÊ VENCEU!',time=.1)
		show(f'O COMPUTADOR ESCOLHEU {jogador_2} E VOCÊ ESCOLHEU {jogador_1}\033[m',time=.01)
	elif jogador_1 == 'PEDRA' and jogador_2 == 'PAPEL':
		corrente('QUE PENA')
		show('\033[31mVOCÊ PERDEU!', time=.1)
		show(f'O COMPUTADOR ESCOLHEU {jogador_2} E VOCÊ ESCOLHEU {jogador_1}\033[m',time=.01)
		
		
def sair(msg):
	try:
		resposta = str(input(msg)).upper().strip()[0]
	except:
		print('\033[31mERRO: Digite uma opção válida!\033[m')
		return '0'
	else:
		return resposta
	
		

	
		










	
