print ('Pasteleria')
totalCompra = 0
pielimon = 2500
tortahelada = 5000
tortapanqueque = 10000
quequearandano = 4000
print ('va a comprar pie de limon? (S/N)')
resp = input() 
if (resp == 'S' or resp == 's'):
    print ('cuantos va a comprar?')
    a = int (input())
    totala = a * pielimon
    totalCompra = (a * pielimon) + totalCompra
    print (totala)
print ('va a comprar torta helada? (S/N)')
resp = input ()
if (resp == 'S' or resp == 's'):
    print ('cuantos va a comprar?')
    b = int (input())
    totalb = b * tortahelada
    totalCompra = (b * tortahelada) + totalCompra
    print (totalb)
print ('va a comprar torta panqueque naranja? (S/N)')
resp = input ()
if (resp == 'S' or resp == 's'):
    print ('cuantos va a comprar?')
    c = int (input())
    totalc = c * tortahelada
    totalCompra = (c * tortapanqueque) + totalCompra
    print (totalc)
print ('va a comprar queque de arandano? (S/N)')
resp = input ()
if (resp == 'S' or resp == 's'):
    print ('cuantos va a comprar?')
    d = int (input())
    totald = d * tortahelada
    totalCompra = (d * tortahelada) + totalCompra
    print (totald)
print ('¿Es cliente preferencial? S/N)')
resp = input()
if (resp == 'S' or resp == 's'):
    desc = 0.2
    totalDesc = totalCompra * 0.2
    totalPagar = totalCompra - totalDesc
    print (totalPagar)
print ('¿Esta de cumpleaños? S/N')
resp = input()
if (resp == 'S' or resp == 's'):
    cump = 0.05
    totalcump = totalCompra * 0.05
    totalpagar = totalCompra - totalcump
    print ('su total a pagar es', totalPagar)
else: 
    totalPagar = totalCompra
    print("Total a Pagar es: " , totalPagar)
