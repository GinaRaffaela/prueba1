print ('Ministerio del Transporte')
totalvehiculos = 0

print ('Digite cantidad de automoviles que cruzaron “Los Libertadores”')
automovil = int(input())
print ('Digite cantidad de station que cruzaron “Los Libertadores”')
station = int(input())
print ('Digite cantidad de jeep que cruzaron “Los Libertadores”')
jeep = int(input())
print ('Digite cantidad de camiones que cruzaron “Los Libertadores”')
camion = int (input())
print ('Digite cantidad de motocicletas que cruzaron “Los Libertadores”')
motocicleta = int (input())
totalvehiculos = automovil + station + jeep + camion + motocicleta
print ('El total de vehiculos que cruzaron "Los Libertadores":', totalvehiculos)
print ('Porcentaje de vehiculos segun su tipo')
auto1 = automovil * 100 / totalvehiculos
auto2 = station * 100 / totalvehiculos
auto3 = jeep * 100 / totalvehiculos
auto4 = camion * 100 / totalvehiculos
auto5 = motocicleta * 100 / totalvehiculos
print ('automovil:', auto1)
print ('station:', auto2)
print ('jeep:' ,auto3)
print ('camiones:', auto4)
print ('motocicletas:', auto5)
