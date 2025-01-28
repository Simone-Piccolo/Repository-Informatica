import random

Hp=50

Turni=0

print("f/n initial healt points:{Hp} \n")

while Hp > 0:
  
  Dado= random.randint(1,6)

  Hp= (Hp-Dado)

  print(f"danno subito: {Dado}")

  print(f" vita rimanente:{Hp}")

  Turni= Turni+1

print("il tuo personaggio è stato sconfitto")

print(f" quanti turni sono stati giocati: {Turni}")
