cabina=[1,2,3,4,5]
cpr=input('Ingrese el costo por rueda:')
motos=0
dinerocab=[0,0,0,0,0]
ccabina=[0,0,0,0,0]
cantruedas=1												
montom=0
motos=0
while cantruedas!= 0:
	cantruedas=input('Ingrese la cantidad de ruedas de su vehiculo : \n (Ingrese 0 para el resultado final):   ')
	cabinas=input('Ingrese la cabina a la que se dirigio : ')
	if cabinas == 1 :
		ccabina[0] =ccabina[0]+1
		dinerocab[0] =+ cpr*cantruedas

	if cabinas == 2 :
		ccabina[1]=ccabina[1]+1
		dinerocab [1] =+ cpr*cantruedas

	if cabinas == 3 :
		ccabina[2] =ccabina[2]+1
		dinerocab[2] =+ cpr*cantruedas

	if cabinas == 4 :
		ccabina[3] =ccabina[3]+1
		dinerocab[3] =+ cpr*cantruedas

	if cabinas == 5 :
		ccabina[4] =ccabina[4]+1
		dinerocab[4] =+ cpr*cantruedas

	if cantruedas == 2 :
		motos =motos+1

	if dinerocab[0] > montom :
		montom=dinerocab[0]

	if dinerocab[1] > montom :
		montom=dinerocab[1]

	if dinerocab[2] > montom :
		montom=dinerocab[2]

	if dinerocab[3] > montom :
		montom=dinerocab[3]

	if dinerocab[4] > montom :
		montom=dinerocab[4]

totalcabinas=dinerocab[0]+dinerocab[1]+dinerocab[2]+dinerocab[3]+dinerocab[4]
totalvehiculos=ccabina[0]+ccabina[1]+ccabina[2]+ccabina[3]+ccabina[4]
for i in range(5):
	print 'El monto de la cabina ',cabina[i],'es :',dinerocab[i]
	print 'Cantidad de vehiculos en la cabina ',cabina[i],': ',ccabina[i]
	print '################################################################'
print 'El monto de las 5 cabinas es de :  ',totalcabinas
print '################################################################'
print 'La cantidad de motos que pasaron fue :  ',motos
print '################################################################'
print 'El promedio total recaudado es de :    ',totalcabinas/totalvehiculos
print '################################################################'
print 'El monto mayor cobrado fue :',montom
txt = open('reporte.txt','w')
for i in range(5):
	print>>txt,'El monto de la cabina ',cabina[i],'es :',dinerocab[i]
	print>>txt,'Cantidad de vehiculos en la cabina ',cabina[i],': ',ccabina[i]
print>>txt,'################################################################'
print>>txt,'El monto de las 5 cabinas es de :  ',totalcabinas
print>>txt,'################################################################'
print>>txt,'La cantidad de motos que pasaron fue :  ',motos
print>>txt,'################################################################'
print>>txt,'El promedio total recaudado es de :    ',totalcabinas/totalvehiculos
print>>txt,'################################################################'
print>>txt,'El monto mayor cobrado fue : ',montom
txt.close ()