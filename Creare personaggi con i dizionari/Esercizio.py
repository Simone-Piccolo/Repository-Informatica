import random

print('\n#1: CREAZIONE DEL PERSONAGGIO\n')
# 1. Crea un dizionario inserendo al suo interno:
# 	 - Un nome scelto a caso dalla lista di nomi
#    - Chiedi all'utente di inserire una classe per il proprio personaggio a scelta tra Guerriero, Mago, Chierico, Ladro
#    Memorizza queste informazioni in un dizionario chiamato 'character'.
nomi = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]

# ****************************************

nome = random.choice(nomi)
classe = input("Scegli una classe per il tuo personaggio (Guerriero, Mago, Chierico, Ladro): ")

character = {
    "nome": nome,
    "classe": classe
}

# ****************************************

print('\n#2: ATTRIBUTI DEL PERSONAGGIO\n')
# 2. Aggiungi al dizionario i seguenti attributi generati casualmente:
#    - Punti vita tra 80 e 100
#    - Armatura tra 5 e 10
#    - Tipo di dado d'attacco (es. "1d6") scelto dall'utente

# ****************************************

punti_vita = random.randint(80, 100)
armatura = random.randint(5, 10)
dado_attacco = input("Scegli il tipo di dado d'attacco (es. 1d6): ")

character.update({
    "punti_vita": punti_vita,
    "armatura": armatura,
    "dado_attacco": dado_attacco
})

# ****************************************

print('\n#2.1: AGGIUNTA DELLO ZAINO\n')
# 2.1. Aggiungi al dizionario un nuovo attributo chiamato 'zaino' che sia a sua volta un dizionario contenente:
#      - 'monete': valore casuale tra 20 e 50
#      - 'oggetti': due oggetti casuali estratti dalla lista di oggetti
#      - 'arma': un oggetto casuale estratto dalla lista delle armi

# ****************************************
oggetti = ["Pozione curativa", "Rampino", "Attrezzi da scasso", "Razioni di cibo", "Corda"]
armi = {
	"fisico": ["Spada", "Pugnale", "Arco", "Balestra"],
	"magico": ["Bastone magico", "Bacchetta"]
}

monete = random.randint(20, 50)


oggetti_estratti = []
for _ in range(2):
    oggetto = random.choice(oggetti)
    oggetti_estratti.append(oggetto)
    oggetti.remove(oggetto)  # Rimuovo l'oggetto selezionato per evitare duplicati

arma_estratta = random.choice(armi["fisico"] if character["classe"] != "Mago" else armi["magico"])

character["zaino"] = {
    "monete": monete,
    "oggetti": oggetti_estratti,
    "arma": arma_estratta
}

# ****************************************

print('\n#3: STAMPA DEL PERSONAGGIO\n')
# 3. Stampa a video tutte le informazioni del personaggio, una per riga.

# ****************************************

print(f"Nome del personaggio: {character['nome']}")
print(f"Classe: {character['classe']}")
print(f"Punti vita: {character['punti_vita']}")
print(f"Armatura: {character['armatura']}")
print(f"Dado d'attacco: {character['dado_attacco']}")
print("Zaino:")
print(f"  Monete: {character['zaino']['monete']}")
print("  Oggetti:")
for oggetto in character['zaino']['oggetti']:
    print(f"    - {oggetto}")
print(f"  Arma: {character['zaino']['arma']}")

# ****************************************
	

print('\n#4: FUNZIONI - CREAZIONE PERSONAGGIO\n')
# 4. Trasforma il codice della creazione di un personaggio in una funzione chiamata 'create_character'.
#    La funzione deve restituire un dizionario con i dati del personaggio.

# ****************************************
def create_character():
    nome = random.choice(nomi)
    classe = input("Scegli una classe per il tuo personaggio (Guerriero, Mago, Chierico, Ladro): ")

    punti_vita = random.randint(80, 100)
    armatura = random.randint(5, 10)
    dado_attacco = input("Scegli il tipo di dado d'attacco (es. 1d6): ")

    oggetti = ["Pozione curativa", "Rampino", "Attrezzi da scasso", "Razioni di cibo", "Corda"]
    armi = {
        "fisico": ["Spada", "Pugnale", "Arco", "Balestra"],
        "magico": ["Bastone magico", "Bacchetta"]
    }

    monete = random.randint(20, 50)

    oggetti_estratti = []
    for _ in range(2):
        oggetto = random.choice(oggetti)
        oggetti_estratti.append(oggetto)
        oggetti.remove(oggetto)  # Rimuovo l'oggetto selezionato per evitare duplicati

    arma_estratta = random.choice(armi["fisico"] if classe != "Mago" else armi["magico"])

    character = {
        "nome": nome,
        "classe": classe,
        "punti_vita": punti_vita,
        "armatura": armatura,
        "dado_attacco": dado_attacco,
        "zaino": {
            "monete": monete,
            "oggetti": oggetti_estratti,
            "arma": arma_estratta
        }
    }

    return character
	
# ****************************************

print('\n#5: FUNZIONI - CREAZIONE PARTY\n')
# 5. Trasforma il codice della creazione di un party in una funzione chiamata 'create_party'.
#    La funzione deve restituire una lista di personaggi (lista di dizionari).

# ****************************************
def create_party():
    num_personaggi = int(input("Quanti personaggi vuoi creare per il tuo party? "))
    party = []
    for _ in range(num_personaggi):
        party.append(create_character())
    return party
	
# ****************************************

print('\n#6: FUNZIONI - STAMPA PARTY\n')
# 6. Trasforma il codice della stampa del party in una funzione chiamata 'print_party'.
#    La funzione deve ricevere una lista di dizionari come parametro e stampare i dati di ogni personaggio.

# ****************************************
def print_party(party):
    for character in party:
        print(f"Nome del personaggio: {character['nome']}")
        print(f"Classe: {character['classe']}")
        print(f"Punti vita: {character['punti_vita']}")
        print(f"Armatura: {character['armatura']}")
        print(f"Dado d'attacco: {character['dado_attacco']}")
        print("Zaino:")
        print(f"  Monete: {character['zaino']['monete']}")
        print("  Oggetti:")
        for oggetto in character['zaino']['oggetti']:
            print(f"    - {oggetto}")
        print(f"  Arma: {character['zaino']['arma']}")
        print("-" * 20)
	
# ****************************************
			
print('\nFUNZIONE PRINCIPALE\n')
# La funzione main qui sotto deve essere compatibile con il tuo codice

# ****************************************
def main():
    party = create_party()
    print_party(party)
	
main()
# ****************************************
