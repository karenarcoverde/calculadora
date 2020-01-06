# Programa karen-arcoverde.py
# Autora: Karen dos Anjos Arcoverde
# Data: 02/05/2018
#
# Calculadora com operacao de multiplicacao, potenciacao, mmc, mdc, fatorial
#

def multiplicacao (valor1,valor2):

        if (valor2 == 0): 
	# Quando o segundo valor eh zero, nao tem como diminuir 1 dele, entao ele eh 
	# uma excecao da recursao. Logo qualquer numero multiplicado por zero tem 
	# como resultado o valor zero
                return 0
        elif (valor2 == 1): 
	# So entra nesse if quando o valor2 eh 1, entao ele retorna o primeiro valor 
	# e fica retornando para as outras funcoes ate o valor2 voltar a ser seu valor original
                return valor1
        return valor1 + multiplicacao(valor1,valor2-1)
	# Diminui 1 do segundo valor ate que ele chegue no caso base onde o valor eh 1






def potenciacao (valor1,valor2):

	# Inicializacao de valores
	aux = valor1
	contmulti = 1 
	multiplicacao = 0
	if(valor2 == 0): # Qualquer numero elevado a 0 eh 1
		return 1
	while(valor2 > 1): 
		while(contmulti <= valor1): # Multiplicacao de dois em dois numeros
			multiplicacao = multiplicacao + aux
			# Soma o numero varias vezes para fazer a multiplicacao de 2 em 2
			contmulti += 1

		contmulti = 1
		aux = multiplicacao 
		# Guarda o valor da multiplicacao anterior para usa-lo na proxima multiplicacao
		multiplicacao = 0
		valor2 -= 1 # O numero de vezes que faz a multiplicacao de 2 em 2 eh sempre o valor2 - 1 
	return aux # Retorna o resultado final das multiplicacoes, que eh a potenciacao





def mmc (valor1,valor2):
	
	if (valor1 == 0 or valor2 == 0): # Excecao do metodo do calculo de mmc
		return 0
	if (valor1 >= valor2):	
		# Inicializacao de valores
		mmc = 1
		cont = valor1
		while (cont <= valor1*valor2):
 		# No pior dos casos, o menor multiplo comum eh o resultado da 
		# multiplicacao dos dois valores pedidos.
			if(cont % valor1 == 0 and cont % valor2 == 0): 
			# Se a condicao for satisfeita, o valor minimo eh achado
				mmc = cont
				cont = valor1*valor2 
				# Para sair do looping, ja que foi achado o valor minimo,
				# coloca-se um valor acima da condicao final do while 
				# para que ele nao satisfaca o que o while pede
			cont += 1 
			# Soma um no contador ate que satisfaca as duas condicoes do if
		return mmc 
	
	if (valor1 < valor2): 
	# Faz a mesma logica mas agora para o primeiro valor digitado menor que o segundo

	# Inicializacao de valores

		mmc = 1
		cont = valor2
		while (cont <= valor1*valor2): 
			if (cont % valor1 == 0 and cont % valor2 == 0): 
				mmc = cont
				cont = valor1*valor2 
			cont += 1 
	return mmc







def mdc (valor1,valor2):

	# Inicializacao de valores

	mdc = 1
	cont = 1
	if (valor1 == 0 and valor2 != 0): # Excecoes do metodo de calculo do mdc 	
		return valor2
	if (valor1 != 0 and valor2 == 0):
		return valor1
	if (valor1 == 0 and valor2 == 0):
		return 'Nao existe'
	if (valor1 >= valor2): 
		while (cont <= valor2): 
		# O maximo divisor so pode ser menor ou igual ao menor valor digitado
			if (valor1 % cont == 0 and valor2 % cont == 0):
				mdc = cont
			cont+=1 
			# Soma ate descobrir quem eh o maximo numero que divide 
			# os dois valores ao mesmo tempo
		return mdc
	
	if (valor1 < valor2): 
	# Faz a mesma logica mas agora para o primeiro valor digitado menor que o segundo
		while (cont <= valor1):
			if (valor1 % cont == 0 and valor2 % cont == 0):
				mdc = cont
			cont += 1
	return mdc






	
def fatorial (valor):

        if (valor == 0): # Visto que fatorial de 0 eh 1
                return 1
        else:
                return valor*fatorial(valor-1)
		# Diminui 1 ate satisfazer o caso base do if para poder retornar 1 a funcao que o 
		# chamou e assim vai retornando o resultado multiplicado ate 
		# a variavel valor voltar ser a original






def entrada_de_valores (memoria): 

	pergunta  = input('Digite "s" para usar o valor da memoria ou "n" para nao usar\n')
	# Leitura dos valores
	valor = 0
	if (pergunta == 's'):
	# Pega o valor guardado do resultado da ultima operacao para fazer a mesma operacao com esse numero
    		valor = memoria	
	else:
		valor  = int(input('Entre com um valor inteiro maior ou igual a zero\n'))
		while (valor < 0): # Confere se o usuario digitou o valor maior que zero ou positivo
    			valor  = int(input('Nao eh permitido numero negativo. Entre com um valor inteiro\n'))
	return valor






def memoria (memoria): 

	# Para saber se o usuario quer guardar o resultado achado da operacao 
	# para usar na operacao do mesmo tipo
        zerar = input('Digite "Nao" para nao salvar a memoria ou "Sim" para salvar\n')
        if (zerar == 'Nao'):
                return 0
        return memoria




#################### Programa Principal ####################

def menu ():

	# Inicializacao de valores

	operacao = 0
	memoria_multiplicacao = 0
	memoria_potenciacao = 0
	memoria_mmc = 0
	memoria_mdc = 0
	memoria_fatorial = 0

	print('OBSERVACOES: CADA OPERACAO POSSUI SUA MEMORIA.\nTAL MEMORIA SO PODE SER USADA PARA OPERACAO DO MESMO TIPO.')
	print('SO PODE DIGITAR NUMERO INTEIRO MAIOR OU IGUAL A ZERO')
	print()

	while (operacao != 6):

		print ('\t\t Menu')
		print ('1. Multiplicacao de dois numeros inteiros')
		print ('2. Potenciacao de dois numeros inteiros')
		print ('3. M.M.C. entre dois numeros inteiros')
		print ('4. M.D.C. entre dois numeros inteiros')
		print ('5. Fatorial de um numero inteiro')
		print ('6. Sair')
		 
		print ()
		operacao = int(input())
		print()

		if (operacao == 1):

			memoria_multiplicacao = multiplicacao(entrada_de_valores(memoria_multiplicacao),entrada_de_valores(memoria_multiplicacao))
			# Entra primeiro na funcao entrada de valores para o usuario digitar um numero 
			# e chama mais uma vez para o segundo, depois retorna o valor dos dois numeros 
 			# digitados e entra na funcao multiplicacao para calcular a operacao de multiplicacao
			print ()
			print ('Resultado:', memoria_multiplicacao)
			# Imprime o resultado final da multiplicacao dos dois valores
			print ()
			memoria_multiplicacao = memoria(memoria_multiplicacao) 
			# Entra na funcao memoria para saber se guarda o resultado achado da multiplicacao
                        
		# A mesma logica se repete para as outras condicoes
		elif (operacao == 2):

			print ('Digite o valor da base')
			base = entrada_de_valores(memoria_potenciacao)

			print ('Digite o valor do expoente')
			expoente = entrada_de_valores(memoria_potenciacao)
			
			memoria_potenciacao = potenciacao(base, expoente)
			print ()
			print ('Resultado:', memoria_potenciacao)
			print ()
			memoria_potenciacao = memoria(memoria_potenciacao)

		elif (operacao == 3):

			memoria_mmc = mmc(entrada_de_valores(memoria_mmc),entrada_de_valores(memoria_mmc))
			print ()
			print ('Resultado:', memoria_mmc)
			print ()
			memoria_mmc = memoria(memoria_mmc)
                        
		elif (operacao == 4):

			memoria_mdc = mdc(entrada_de_valores(memoria_mdc),entrada_de_valores(memoria_mdc))
			print ()
			print ('Resultado:', memoria_mdc)
			print ()
			memoria_mdc = memoria(memoria_mdc)
                        
		elif (operacao == 5):

			memoria_fatorial = fatorial(entrada_de_valores(memoria_fatorial))
			print ()
			print ('Resultado:', memoria_fatorial)
			print ()
			memoria_fatorial = memoria(memoria_fatorial)

########## Chamada o menu()
menu ()
