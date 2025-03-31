def genera_tabula_recta() -> list[list[str]]:
"""Genera e restituisce la tabula recta, una matrice 26x26 di alfabeti traslati."""
tabula = []
for i in range(26):
riga = []
for j in range(26):
riga.append(chr(((i + j) % 26) + 65))
tabula.append(riga)
return tabula

def normalizza_testo(testo: str) -> str:
"""Rimuove caratteri non alfabetici e converte tutto in maiuscolo."""
risultato = ""
for c in testo:
if ('A' <= c <= 'Z') or ('a' <= c <= 'z'): # Controllo manuale per caratteri alfabetici
if 'a' <= c <= 'z': # Conversione in maiuscolo
risultato += chr(ord(c) - 32)
else:
risultato += c
return risultato

def estendi_chiave(chiave: str, lunghezza: int) -> str:
"""Espande la chiave fino alla lunghezza richiesta ripetendola ciclicamente."""
chiave_estesa = ""
for i in range(lunghezza):
chiave_estesa += chiave[i % len(chiave)]
return chiave_estesa

def cifra(messaggio: str, chiave: str, tabula_recta: list[list[str]]) -> str:
"""Cifra un messaggio con il cifrario di Vigenère usando la tabula recta."""
testo_cifrato = ""
for i in range(len(messaggio)):
riga = ord(chiave[i]) - 65 # Indice della riga (A=0, B=1, ...)
colonna = ord(messaggio[i]) - 65 # Indice della colonna (A=0, B=1, ...)
testo_cifrato += tabula_recta[riga][colonna]
return testo_cifrato

def decifra(messaggio_cifrato: str, chiave: str, tabula_recta: list[list[str]]) -> str:
"""Decifra un messaggio cifrato con il cifrario di Vigenère usando la tabula recta."""
testo_decifrato = ""
for i in range(len(messaggio_cifrato)):
riga = ord(chiave[i]) - 65 # Indice della riga usata in cifratura
colonna = 0
while tabula_recta[riga][colonna] != messaggio_cifrato[i]: # Trova l'indice della colonna
colonna += 1
testo_decifrato += chr(colonna + 65) # Converti indice in lettera
return testo_decifrato

def main():
"""Funzione principale che gestisce l'interazione con l'utente."""
print("Cifrario di Vigenère")

tabula_recta = genera_tabula_recta()

scelta = input("Vuoi cifrare (C) o decifrare (D)? ").strip().upper()

if scelta == "C":
messaggio = input("Inserisci il messaggio da cifrare: ")
chiave = input("Inserisci la chiave: ")
messaggio = normalizza_testo(messaggio)
chiave = normalizza_testo(chiave)
chiave_estesa = estendi_chiave(chiave, len(messaggio))
testo_cifrato = cifra(messaggio, chiave_estesa, tabula_recta)
print(f"Testo cifrato: {testo_cifrato}")

elif scelta == "D":
messaggio_cifrato = input("Inserisci il messaggio cifrato: ")
chiave = input("Inserisci la chiave: ")
messaggio_cifrato = normalizza_testo(messaggio_cifrato)
chiave = normalizza_testo(chiave)
chiave_estesa = estendi_chiave(chiave, len(messaggio_cifrato))
testo_decifrato = decifra(messaggio_cifrato, chiave_estesa, tabula_recta)
print(f"Testo decifrato: {testo_decifrato}")

else:
print("Scelta non valida.")

if __name__ == "__main__":
main()
