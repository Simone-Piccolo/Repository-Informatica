def genera_tabula_recta() -> list[list[str]]:
    """Genera e restituisce la tabula recta, una matrice 26x26 di alfabeti traslati."""
    matrice = []
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):  # Scorre ogni lettera dell'alfabeto come punto di partenza
        riga = []
        for j in range(i, 26 + i):  # Scorre l'alfabeto traslando le lettere
            riga.append(alfabeto[j - 26])  # Usa il modulo per mantenere le lettere nell'intervallo
        matrice.append(riga)  # Aggiunge la riga alla matrice
    return matrice  # Restituisce la tabula recta


def cifra(messaggio: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Cifra un messaggio con il cifrario di Vigenère usando la tabula recta."""
    chiave_cifratura = estendi_chiave(chiave, len(messaggio))  # Estende la chiave fino alla lunghezza del messaggio
    
    messaggio_cifrato = ""
    for i in range(len(messaggio)):
        indice_messaggio = tabula_recta[0].index(messaggio[i].upper())  # Trova la posizione della lettera del messaggio nella prima riga della tabula recta
        indice_chiave = tabula_recta[0].index(chiave_cifratura[i].upper())  # Trova la posizione della lettera della chiave
        messaggio_cifrato += tabula_recta[indice_chiave][indice_messaggio]  # Usa la tabula recta per ottenere la lettera cifrata
    
    return messaggio_cifrato.upper()  # Restituisce il testo cifrato in maiuscolo


def decifra(messaggio_cifrato: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Decifra un messaggio cifrato con il cifrario di Vigenère usando la tabula recta."""
    chiave_cifratura = estendi_chiave(chiave, len(messaggio_cifrato))  # Estende la chiave alla lunghezza del messaggio cifrato
    
    messaggio_decifrato = ""
    for i in range(len(messaggio_cifrato)):
        indice_chiave = tabula_recta[0].index(chiave_cifratura[i].upper())  # Trova la posizione della lettera della chiave nella prima riga della tabula recta
        indice_messaggio_cifrato = tabula_recta[indice_chiave].index(messaggio_cifrato[i])  # Trova la posizione della lettera cifrata nella riga corrispondente alla chiave
        messaggio_decifrato += tabula_recta[0][indice_messaggio_cifrato]  # Recupera la lettera originale dalla prima riga della tabula recta
    
    return messaggio_decifrato  # Restituisce il testo decifrato


def normalizza_testo(testo: str) -> str:
    """Rimuove caratteri non alfabetici e converte tutto in maiuscolo per garantire compatibilità con la cifratura."""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    testo_normalizzato = ""
    for carattere in testo.upper():  # Converte tutto in maiuscolo per uniformità
        if carattere in alfabeto:  # Mantiene solo i caratteri alfabetici
            testo_normalizzato += carattere  # Aggiunge la lettera normalizzata
    
    return testo_normalizzato  # Restituisce il testo pulito e in maiuscolo


def estendi_chiave(chiave: str, lunghezza: int) -> str:
    """Espande la chiave fino alla lunghezza richiesta ripetendola ciclicamente."""
    i = 0
    chiave_cifratura = ""
    while len(chiave_cifratura) != lunghezza:
        if i >= len(chiave):  # Se la chiave è finita, riparte dall'inizio
            i = 0
        chiave_cifratura += chiave[i]  # Aggiunge caratteri dalla chiave originale
        i += 1
    
    return chiave_cifratura  # Restituisce la chiave estesa


def main():
    """Funzione principale che gestisce l'interazione con l'utente."""
    print("Cifrario di Vigenère")

    tabula_recta = genera_tabula_recta()  # Genera la tabula recta per l'uso

    scelta = input("Vuoi cifrare (C) o decifrare (D)? ").strip().upper()

    if scelta == "C":  # Opzione per cifrare il messaggio
        messaggio = input("Inserisci il messaggio da cifrare: ")
        chiave = input("Inserisci la chiave: ")
        messaggio = normalizza_testo(messaggio)  # Normalizza il testo per rimuovere caratteri speciali
        chiave = normalizza_testo(chiave)  # Normalizza la chiave
        chiave_estesa = estendi_chiave(chiave, len(messaggio))  # Espande la chiave
        testo_cifrato = cifra(messaggio, chiave_estesa, tabula_recta)  # Cifra il messaggio
        print(f"Testo cifrato: {testo_cifrato}")

    elif scelta == "D":  # Opzione per decifrare il messaggio
        messaggio_cifrato = input("Inserisci il messaggio cifrato: ")
        chiave = input("Inserisci la chiave: ")
        messaggio_cifrato = normalizza_testo(messaggio_cifrato)  # Normalizza il testo cifrato
        chiave = normalizza_testo(chiave)  # Normalizza la chiave
        chiave_estesa = estendi_chiave(chiave, len(messaggio_cifrato))  # Espande la chiave
        testo_decifrato = decifra(messaggio_cifrato, chiave_estesa, tabula_recta)  # Decifra il messaggio
        print(f"Testo decifrato: {testo_decifrato}")

    else:
        print("Scelta non valida.")  # Messaggio di errore per input non valido


if __name__ == "__main__":
    main()  # Avvia il programma