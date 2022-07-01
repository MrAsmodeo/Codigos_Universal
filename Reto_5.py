#reto final 
from logging import basicConfig


productos = {
    1: ["Manzanas", 5000.0, 25],
    2: ["Limones", 2300.0, 15], 
    3: ["Peras", 2700.0, 33],  
    4: ["Arandanos", 9300.0, 5],  
    5: ["Tomates", 2100.0, 42], 
    6: ["Fresas", 4100.0, 3], 
    7: ["Helado", 4500.0, 41], 
    8: ["Galletas", 500.0, 8], 
    9: ["Chocolates", 3500.0, 80], 
    10:["Jamon", 15000.0, 10]
}

def leer_datos (): 
  operacion = input()
  producto =input().split()
  producto[0] = int(producto[0])
  producto[2] = float(producto[2])
  producto[3] = int (producto[3])
  return operacion, producto

def agregar(base_datos, producto):
  if producto[0] in base_datos:
    return False
  else: 
    codigo = producto[0]
    producto.pop(0)
    base_datos[codigo] = producto
    return True 

def actualizar(base_datos, producto):
  if producto[0] in base_datos:
    codigo = producto[0]
    producto.pop(0)
    base_datos[codigo] = producto
    return True
  else:
    return False


def borrar(base_datos, producto):
  if producto[0] in base_datos:
    base_datos.pop(producto[0])
    return True
  else:
    return False

def precio_mayor (base_datos):
  mayor = list(base_datos.keys())
  mayor = mayor[0]
  for i in base_datos:
    if base_datos[i][1] > base_datos[mayor][1]:
      mayor = i
  return base_datos[mayor][0]

def precio_menor (base_datos):
  menor = list(base_datos.keys())
  menor = menor[0]
  for i in base_datos:
    if base_datos[i][1] < base_datos[menor][1]:
      menor = i
  return base_datos[menor][0]

def promedio(base_datos):
  promediov = 0 
  for i in base_datos:
    promediov += base_datos[i][1]
  promediov = promediov/ len(base_datos)
  return promediov

def valor_inventario(base_datos):
  inventario = 0
  for i in base_datos:
    inventario += base_datos[i][2] * base_datos[i][1]
  return inventario 

def imprimir_valores(base_datos):
    precioM = precio_mayor(base_datos)
    preciom = precio_menor(base_datos)
    promediov = round(promedio(base_datos),1)
    inventario = round(valor_inventario(base_datos),1)
    print(precioM, preciom, promediov, inventario)

operacion, producto = leer_datos()

if operacion == 'ACTUALIZAR':
  bandera = actualizar(productos, producto)
elif operacion =='BORRAR':
  bandera = borrar(productos, producto)
elif operacion == 'AGREGAR':
  bandera = agregar(productos, producto)

if bandera == True:
  imprimir_valores(productos)
else:print('ERROR')