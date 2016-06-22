#!/usr/bin/env python
#-*- coding: UTF-8 -*-
def cuentavocales(frase):
	contadorvocales=0
	for letra in frase:
		if letra == 'a' or letra == 'A':
			contadorvocales+=1
		elif letra == 'e' or letra == 'E':
			contadorvocales+=1
		elif letra == 'i' or letra == 'I':
			contadorvocales+=1
		elif letra == 'o' or letra == 'O':
			contadorvocales+=1
		elif letra == 'u' or letra == 'U':
			contadorvocales+=1
	print('Cantidad de vocales:\n -> '),contadorvocales
frase=raw_input('Ingrese una frase para contar sus vocales: ')
cuentavocales(frase)