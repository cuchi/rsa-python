from random import randrange
from genericsFunctions import MDC
from genericsFunctions import MDCEst
from genericsFunctions import testMod

def primalityFermat( nParamTest ):
	nTrial = 1
	nNumTrial = 20 # Seta a quantidade de tentativas em 20
	nNumTest = nParamTest

	if nNumTest != 1:
		while nTrial <= nNumTrial:
			nTrial += 1
			# Gera um n�mero aleat�rio de  1 at� nNumTest - 1
			nNumRand = randrange(1, nNumTest )

			# Avalia se o numero possui outro m�ximo denominador comum
			# que n�o 1, caso tenha n�o � primo
			if (MDC(nNumRand,nNumTest) != 1):
				return False

			# Avalia pelo Teste de Fermat se o n�mero � composto
			nTest = testMod(nNumRand,(nNumTest - 1),nNumTest)
			if ( nTest != 1):
				return False
	return True
