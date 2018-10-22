# Determina o resultado do m�dulo de acordo com o Fator e a Pot�ncia
# Aplica-se o Teorema do Quociente-Resto:
#	- Onde, A = B * Q + R, sendo 0 <= R < B
# e a Multiplica��o Modular:
#	- Onde, (A * B) mod C = (A mod C * B mod C) mod C
# Com isso, elimina-se os m�ltiplos de C e considera-se os Restos para
# as demais m�ltiplica��es
def testMod(nFactor,nPow,nNumMod):
	nMod = 1

	nFactor = nFactor % nNumMod
	# Realiza a opera��o at� pot�ncia ser encerrada
	while nPow > 0:
		# Caso n�o seja divisor de dois,
		# multiplica o resto salvo pelo fator e
		# salva o resto da divis�o
		if ( nPow % 2 == 1 ):
			nMod = ( nMod * nFactor ) % nNumMod
			nPow -= 1
		# Divide o expoente por 2 e salva o valor
		nPow = nPow//2
		# Multiplica o fator em 2 e
		# salva como novo fator o resto da divis�o
		# para utilizar no novo m�dulo
		nFactor = ( nFactor * nFactor ) % nNumMod
	return nMod

# Retorna o Maximo Divisor Comum aplicando o Algoritmo de Euclides
def MDC(nRandom, nTestNum):

	nMDC = nRandom
	# Faz o calculo at� zerar o n�mero do divisor
	# Para tanto, realiza as divis�es pelos restos
	while (nTestNum != 0):
		# Salva o resto da divis�o do n�mero randomico pelo numero testado
		nTmpMod = nMDC % nTestNum
		# Salva como m�ximo divisor comum o n�mero testado
		# e como novo divisor o resto da divis�o atual
		nMDC = nTestNum
		nTestNum = nTmpMod

	return nMDC

# Retorna o valor de X no Algoritmo de Euclides Estendido
# Onde A x X + B x Y = MDC(A,B), sendo :
#	- A o valor da chave p�blica E
#	- B o valor de Phi(N)
def MDCEst(nX,nY):
	# Estrutura de Vari�veis
	# nValueX * nX + nValueY * nY = nX
	# nRest1 * nValueX + nRest2 * nY = nY
	nValueX = 1
	nValueY = 0
	nRest1 = 0
	nRest2 = 1
	nNewRest1 = 0
	nNewRest2 = 0

	'''
	Estrutura de Exemplo
	(1) 13/640 = 0 com resto 13
	(2) 640/13 = 49 com resto 3
	(3) 13/3 = 4 com resto 1

	------------------
	X / Y = C com R
	X = C * Y + R
	Isola-se o R
	R = X - ( C * Y ) ou R = ( 1 * X ) - ( C * Y )
	(1) 13 = ( 1 * 13 ) - ( 0 * 640 )
	(2) 3 = ( 1 * 640 ) - ( 49 * 13 )
	(2) 3 = ( 1 * 640 ) - ( 49 * ( ( 1 * 13 ) - ( 0 * 640 ) ) )
	(2) 3 = ( 1 * 640 ) - ( 49 * 13 ) - ( 0 * 640 )
	(2) 3 = ( 1 * 640 ) - ( 49 * 13 )
	(3) 1 = ( 1 * 13 ) - ( 4 * 3 )
	(3) 1 = ( 1 * 13 ) - ( 4 * ( 1 * 640 ) - ( 49 * 13 ) )
	(3) 1 = ( 1 * 13 ) - ( 4 * 640 ) - ( 196 * 13 )
	(3) 1 = ( 197 * 13 ) - ( 4 * 640 )
	'''
	while ( nY != 0 ):
		nTmpRes = nX % nY
		nQuot = (nX//nY)
		nX = nY
		nY = nTmpRes
		nNewRest1 = nValueX - nQuot * nRest1
		nNewRest2 = nValueY - nQuot * nRest2
		nValueX = nRest1
		nValueY = nRest2
		nRest1 = nNewRest1
		nRest2 = nNewRest2

	return nValueX