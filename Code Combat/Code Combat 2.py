import random

# Funzione per simulare una singola partita
def simula_partita():
   
    vita_player_1 = random.randint(80, 100)
  
    scudo_player_1 = random.randint(5, 10)
  
    dadi_player_1 = [random.randint(1, 6) for _ in range(4)]  # 4d6

    
    vita_player_2 = random.randint(80, 100)
  
    scudo_player_2 = random.randint(5, 10)
  
    dadi_player_2 = [random.randint(1, 12) for _ in range(2)]  # 2d12

   
    turni = 0
  
    while vita_player_1 > 0 and vita_player_2 > 0:
      
        turni += 1
      
        print(f"***Turn {turni}***")
        
        # Calcolo attacco Player 1
      
        attacco_player_1 = sum(dadi_player_1)
      
        danno_player_1 = max(attacco_player_1 - scudo_player_2, 0)
      
        vita_player_2 -= danno_player_1
      
        print(f"[Player1] Damage: {danno_player_1} ({attacco_player_1}-{scudo_player_2})")
      
        print(f"[Player2] Health: {vita_player_2}")
        
        # Calcolo attacco Player 2
      
        attacco_player_2 = sum(dadi_player_2)
      
        danno_player_2 = max(attacco_player_2 - scudo_player_1, 0)
      
        vita_player_1 -= danno_player_2
      
        print(f"[Player2] Damage: {danno_player_2} ({attacco_player_2}-{scudo_player_1})")
      
        print(f"[Player1] Health: {vita_player_1}")
      
        print()

    
    if vita_player_1 > 0 and vita_player_2 <= 0:
      
        return 1, turni  # Player 1 vince
      
    elif vita_player_2 > 0 and vita_player_1 <= 0:
      
        return 2, turni  # Player 2 vince
    else:
        return 0, turni  # Pareggio

# Simulazione di 1000 partite
partite = 1000

vittorie_player_1 = 0

vittorie_player_2 = 0

pareggi = 0

turni_totali = 0

for _ in range(partite):
  
    risultato, turni = simula_partita()
    
    if risultato == 1:
      
        vittorie_player_1 += 1
      
    elif risultato == 2:
      
        vittorie_player_2 += 1
      
    else:
      
        pareggi += 1

    turni_totali += turni



vittorie_totali = vittorie_player_1 + vittorie_player_2

vittoria_percentuale_player_1 = (vittorie_player_1 / vittorie_totali) * 100

vittoria_percentuale_player_2 = (vittorie_player_2 / vittorie_totali) * 100

media_turni = turni_totali / partite

# Output dei risultati finali

print(f"Vittorie Player 1: {vittorie_player_1} ({vittoria_percentuale_player_1}%)")

print(f"Vittorie Player 2: {vittorie_player_2} ({vittoria_percentuale_player_2}%)")

print(f"Pareggi: {pareggi} ({(pareggi / partite) * 100}%)")

print(f"Numero medio di turni: {media_turni}")

