num=input('Ingrese un vector numerico(Separados por comas)')
par=[]
impar=[]
def numpi():
	for i in num:
		if i %2==0:
			par.append(i)
		else:
			impar.append(i)
numpi()
print('Numeros pares: '),sorted(par)
print('Numeros impares: '),sorted(impar)