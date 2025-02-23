import random

# Funzione per generare i parametri di ciascun personaggio

def crea_personaggio(classe):
  
    if classe == 'Guerriero':
      
        vita = random.randint(100, 120)
      
        energia = random.randint(8, 10)
      
        difesa = random.randint(4, 8)
      
        attacco = random.randint(2, 12)  # 2d6
      
        abilita = 'Berserk'
      
    elif classe == 'Mago':
      
        vita = random.randint(70, 90)
      
        energia = random.randint(14, 18)
      
        difesa = random.randint(3, 5)
      
        attacco = random.randint(1, 20)  # 1d20
      
        abilita = 'Concentrazione assoluta'
      
    elif classe == 'Ladro':
      
        vita = random.randint(80, 100)
      
        energia = random.randint(10, 12)
      
        difesa = random.randint(3, 5)
      
        attacco = random.randint(3, 12)  # 3d4
      
        abilita = 'Pugnali acidi'
      
    elif classe == 'Chierico':
      
        vita = random.randint(80, 100)
      
        energia = random.randint(10, 12)
      
        difesa = random.randint(4, 6)
      
        attacco = random.randint(1, 12)  # 1d12
      
        abilita = 'Favore degli dei'
    
    return {
        'classe': classe,
        'vita': vita,
        'energia': energia,
        'difesa': difesa,
        'attacco': attacco,
        'abilità': abilita
    }

# Funzione per creare un party

def crea_party():
  
    party = [
        crea_personaggio('Guerriero'),
        crea_personaggio('Mago'),
        crea_personaggio('Ladro'),
        crea_personaggio('Chierico')
    ]
    return party

# Funzione per lanciare un dado

def lancia_dado(num_dadi, facce):
  
    return sum(random.randint(1, facce) for _ in range(num_dadi))

# Funzione per attaccare un avversario

def attacca(attaccante, difensore):
  
    if attaccante['energia'] < 2:
      
        # Il personaggio non ha abbastanza energia, quindi si riposa
      
        attaccante['energia'] = 12  # ricarica al massimo l'energia
      
        print(f"{attaccante['classe']} riposa e ricarica energia.")
      
        return
    
    # Consuma 2 punti di energia per l'attacco
  
    attaccante['energia'] -= 2
    
    danno = attaccante['attacco'] - difensore['difesa']
  
    danno = max(danno, 0)  # Il danno non può essere negativo
  
    difensore['vita'] -= danno
    
    print(f"{attaccante['classe']} attacca {difensore['classe']} causando {danno} danni.")
    
    # Se il difensore ha vita <= 0, viene eliminato
  
    if difensore['vita'] <= 0:
      
        print(f"{difensore['classe']} è stato eliminato!")
    
    # Verifica abilità speciale
  
    if attaccante['abilità'] == 'Berserk':
      
        lancia_berserk(attaccante)
      
    elif attaccante['abilità'] == 'Concentrazione assoluta':
      
        lancia_concentrazione(attaccante)
      
    elif attaccante['abilità'] == 'Pugnali acidi':
      
        lancia_pugnali_acidi(attaccante)
      
    elif attaccante['abilità'] == 'Favore degli dei':
      
        lancia_favore(attaccante, difensore)

# Funzioni per abilità speciali

def lancia_berserk(guerriero):
  
    risultato = lancia_dado(1, 6)
  
    if risultato >= 5:
      
        print(f"{guerriero['classe']} effettua un altro attacco!")
      
        guerriero['energia'] -= 2  # Consuma energia per il secondo attacco
      
    elif risultato >= 3:
      
        perdita_vita = guerriero['vita'] // 5
      
        guerriero['vita'] -= perdita_vita
      
        print(f"{guerriero['classe']} perde il 20% della vita: {perdita_vita} punti vita.")
      
    else:
        perdita_vita = guerriero['vita'] // 5
      
        guerriero['vita'] -= perdita_vita
      
        print(f"{guerriero['classe']} perde il 20% della vita: {perdita_vita} punti vita.")

def lancia_concentrazione(mago):
  
    risultato = lancia_dado(1, 6)
  
    if risultato >= 5:
      
        aumento = random.randint(1, 4)
      
        mago['attacco'] += aumento
      
        print(f"{mago['classe']} aumenta il suo attacco di {aumento}.")

def lancia_pugnali_acidi(ladro):
  
    risultato = lancia_dado(2, 4)
  
    if risultato == 7 or risultato == 8:
      
        print(f"{ladro['classe']} riduce la difesa degli avversari del 25%.")

def lancia_favore(chierico, party):
  
    risultato = lancia_dado(2, 6)
    
    # Trova il personaggio con la vita più bassa
  
    personaggio_da_curare = party[0]  
  
    for p in party:
      
        if p['vita'] < personaggio_da_curare['vita']:
          
            personaggio_da_curare = p  # Se trovo uno con meno vita, lo scelgo

    cura = risultato
  
    personaggio_da_curare['vita'] += cura
  
    print(f"{chierico['classe']} cura {personaggio_da_curare['classe']} di {cura} punti vita.")
  

# Eseguo il combattimento tra due party

party1 = crea_party()

party2 = crea_party()

# Simulazione di un round di attacchi 

attacca(party1[0], party2[0])  # Guerriero di party1 attacca Guerriero di party2

attacca(party2[0], party1[0])  # Guerriero di party2 attacca Guerriero di party1
