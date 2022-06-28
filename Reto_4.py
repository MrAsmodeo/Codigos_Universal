# Solucion Reto 4

# recepción de valores 
from typing import Counter


N_tiles, K_sensor = input().split()
M_tiles = input().split()

#conversor a  int 

N_tiles = int(N_tiles)
K_sensor = int(K_sensor)

# Op 1 list

for x in range (0, len(M_tiles), 1):
    M_tiles[x] = int(M_tiles[x])

# Inicialisamos

total_failures = 0
faults_detected = 0

# inicialisamos un dic

dictionary = dict()
counter = 0

# Op 2 Dict 
for value in M_tiles:
    if (value in dictionary):
        total_failures += 1
    if (value in dictionary) and (counter - dictionary.get(value) <= K_sensor):
        faults_detected += 1
    dictionary[value] = counter
    counter += 1
#Print Salida 
print(total_failures, faults_detected, len(M_tiles))