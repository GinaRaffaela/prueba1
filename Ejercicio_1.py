print ('proyecto familiar llamado verduras SASA')
canasta = 16000
a = 1000
b = 2000
c = 3000

print ('El valor de la canasta de frutas y verduras es de $16.000')
print ('¿Cuantas canastas va a comprar?')
compra = int(input ())
totalcompra= compra * canasta
print ('el valor de las canastas es de', totalcompra)
if (totalcompra > 32000):
    print ('Su costo de envio es gratis, su total a pagar es de', totalcompra)
else:
    print ('Debe pagar costos de envio')
print ('indique la alternativa correcta: \n a: misma comuna \n b: comuna aledaña \n c: otro')
resp = input()
if (resp == 'a'):
    costoenvio = a
    totalpagar = costoenvio + totalcompra
    print ('el total a pagar es', totalpagar)
elif (resp == 'b'):
    costoenvio = b
    totalpagar = costoenvio + totalcompra
    print ('el total a pagar es', totalpagar)
elif (resp == 'c'):
    costoenvio = c
    totalpagar = costoenvio + totalcompra
    print ('el total a pagar es', totalpagar)
print ('Gracias por comprar con nosotros')
