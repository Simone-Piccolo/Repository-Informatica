import random

nomi = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]
cognomi = ["Stoneforge", "Moonshadow", "Starwhisper", "Thunderbeard", "Fireheart", "Ravenwing", "Icebane", "Stormrider", "Swiftfoot", "Dragonflame", "Shadowcloak", "Ironhammer", "Frostbeard", "Silverleaf", "Goldenshield", "Windrider", "Hawkseye", "Deepstone", "Steelheart", "Oakenshield"]

def genera_nome():
  
    nome = random.choice(nomi)
  
    cognome = random.choice(cognomi)
  
    return nome + " " + cognome

def lancia_dadi(num_dadi, facce):
  
    lanci = [random.randint(1, facce) for _ in range(num_dadi)]
  
    lanci.sort()
  
    return lanci[1:-1]  # Rimuove il dado più basso e quello più alto

# Funzione per calcolare il danno e aggiornare la salute

def calcola_danno(nome_giocatore, lanci_dadi, salute_avversario, scudo_avversario):
  
    print(f"{nome_giocatore} ha lanciato: {lanci_dadi}")
  
    danno = sum(lanci_dadi) - scudo_avversario
  
    if danno <= 0:
      
        print(f"{nome_giocatore} Danno: {danno} ({sum(lanci_dadi)}-{scudo_avversario}). L'attacco è stato evitato.")
      
    else:
      
        print(f"{nome_giocatore} Danno: {danno} ({sum(lanci_dadi)}-{scudo_avversario})")
      
    salute_avversario -= danno
  
    return salute_avversario

# Funzione per generare vita e scudo casuali per ogni giocatore

def genera_statistiche():
  
    vita = random.randint(50, 100) 
  
    scudo = random.randint(0, 30)   
  
    return vita, scudo

# Creazione dei due giocatori con nome, vita e scudo casuali

nome_giocatore1 = genera_nome()

nome_giocatore2 = genera_nome()

salute_giocatore1, scudo_giocatore1 = genera_statistiche()

salute_giocatore2, scudo_giocatore2 = genera_statistiche()

turni = 0

while salute_giocatore1 > 0 and salute_giocatore2 > 0:
  
    turni += 1
   
    # Giocatore 1 lancia 6 dadi da 6
  
    dadi_giocatore1 = lancia_dadi(6, 6)
  
    salute_giocatore2 = calcola_danno(nome_giocatore1, dadi_giocatore1, salute_giocatore2, scudo_giocatore2)
  
   
    # Giocatore 2 lancia 4 dadi da 12
  
    dadi_giocatore2 = lancia_dadi(4, 12)
  
    salute_giocatore1 = calcola_danno(nome_giocatore2, dadi_giocatore2, salute_giocatore1, scudo_giocatore1)

    if salute_giocatore1 <= 0:
      
        print(f"{nome_giocatore2} HA VINTO!")
      
        break
      
    elif salute_giocatore2 <= 0:
      
        print(f"{nome_giocatore1} HA VINTO!")
      
        break

    print(f"{nome_giocatore1} Salute: {salute_giocatore1}")
  
    print(f"{nome_giocatore2} Salute: {salute_giocatore2}")
   
print(f"Turni giocati: {turni}")
