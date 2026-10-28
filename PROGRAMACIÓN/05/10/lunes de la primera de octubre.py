
jugadores = int(input("¿Cuantos jugadores hay?: "))

while jugadores < 2 or jugadores > 6:
 jugadores = int(input("Numero incorrecto..¿Cuantos jugadores hay?: "))

if jugadores >= 2 and jugadores <= 6:
 print("valido")
else:
 print("no valido")

total = 0
expertos = 0

for i in range (jugadores):
 print("jugador", i + 1)

 puntos = int(input("¿Cuantos puntos pondrías a cada jugador?: "))
 while puntos < 0 or puntos > 100:
  puntos = int(input(" Numero incorrecto...¿Cuantos puntos pondrías a cada jugador?: "))

 if puntos >= 0 and puntos <= 49:
  print("principiante")
 elif puntos >= 50 and puntos <= 79:
  print("avanzado")
 else:
  print("experto")
  expertos += 1
total = puntos + total

print("El total de puntos son:", puntos)

media: float = total / jugadores
print("La media de puntos es:", media)