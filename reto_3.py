# solucion Reto 3 

#entradas
N= int(input())        
bicicletas = []         

#proceso

for i in range(N):     
  bicicletas.append(input().split())

#funcion para calcular entre los rangos requeridos 

def calcular():
  precios = []
  for i in bicicletas:
    if int (i[0]) >= 240 and int(i[0]) <= 300 \
    and int(i[1]) >= 160 and int(i[1]) <= 180 \
    and int(i[2]) >= 240 and int (i[2]) <= 275 \
    and int(i[3]) <= 50:

      precios.append(int(i[4]))

  return  precios

resultado = calcular()

if len(resultado) ==0:
  print("NO DISPONIBLE")
else:
  for i in resultado:
    print(i)