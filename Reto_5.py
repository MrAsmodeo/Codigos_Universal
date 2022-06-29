# Reto 5

def leer_datos():
  operacion = input()
  producto = input().split()
  producto[0] = int(producto[0])
  producto[2] = float(producto[2])
  producto[3] = int(producto[3])

  return operacion, producto


def borrar(base_datos, producto):
  if producto[0] in base_datos:
    base_datos.pop(producto[0])
    return True
  else:
    return False

def actualizar(base_datos, producto):
  if producto[0] in base_datos:
    clave = producto[0]
    producto.pop(0)
    base_datos[clave] = producto
    return True
  else:
    return False 

def agregar(base_datos, producto):
  if producto[0] in base_datos:
    return False 
  else:
    clave = producto[0]
    producto.pop(0)
    base_datos[clave] = producto
    return True

def precio_mayor(base_datos):
  mayor = list(base_datos.keys())
  mayor = mayor[0]

  for i in base_datos:
    if(base_datos[i][1]) > base_datos[mayor][1]:
      mayor = i
  return base_datos[mayor][0]

def promedio_precios(base_datos):
  promedio = 0
  for i in base_datos:
    promedio += base_datos[i][1]
  promedio / len(base_datos)
  return promedio

def precio_menor(base_datos):
  menor = list(base_datos.keys())[0]
  for i in base_datos:
    if base_datos[i][1] < base_datos[menor][1]:
      menor = i
  return base_datos [menor][0]

def valor_inventario(base_datos):
  valor_inventario= 0.0
  for i in base_datos:
    valor_inventario +=  base_datos[i][1] * base_datos[i][2]
  return valor_inventario

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

operacion, producto = leer_datos()

if operacion == 'AGREGAR':
  bandera = agregar(productos, producto)
elif operacion == 'BORRAR':
  bandera = (productos, producto)
elif operacion == 'ACTUALIZAR':
  bandera = actualizar(productos, producto)

if bandera == False :
  print('ERROR')
else:
  print(precio_mayor(productos), precio_menor(productos), round(promedio_precios(productos),1), round(valor_inventario(productos),1))