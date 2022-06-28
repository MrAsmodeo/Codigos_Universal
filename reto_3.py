# solucion Reto 3 

#entradas
x= int(input())        
bike_x = []         

#proceso

for i in range(x):     
  bike_x.append(input().split())

#funcion para calcular entre los rangos requeridos 

def calculate():
  prices = []
  for i in bike_x:
    if int (i[0]) >= 240 and int(i[0]) <= 300 \
    and int(i[1]) >= 160 and int(i[1]) <= 180 \
    and int(i[2]) >= 240 and int (i[2]) <= 275 \
    and int(i[3]) <= 50:

      prices.append(int(i[4]))

  return  prices

result = calculate()

if len(result) ==0:
  print("NO DISPONIBLE")
else:
  for i in result:
    print(i)