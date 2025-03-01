import random

def genera_matrice(n: int, numeri_validi: list):
  
    """Genera una matrice n x n con numeri casuali."""
  
    matrice = []
  
    numeri_disponibili = numeri_validi[:]  # Per creare una copia della lista in modo che non venga modificata la lista originale
  
    for _ in range(n):
      
        riga = []
      
        for _ in range(n):
          
            num = random.choice(numeri_disponibili)
          
            riga.append(num)
          
            numeri_disponibili.remove(num)
          
        matrice.append(riga)
      
    return matrice

def verifica_quadrato_magico(matrice):
  
    """Verifica se la matrice è un quadrato magico."""
  
    risultato_righe = []
  
    contatore = 0
  
    for riga in matrice:
      
        for elemento in riga:
          
            contatore += elemento
          
        risultato_righe.append(contatore)
      
        contatore = 0
      
    for i in range(len(risultato_righe)):
      
        if risultato_righe[i] != risultato_righe[0]:
          
            return False
          
    return True
  

def stampa_matrice(matrice, costante_magica=None):
  
    """Stampa la matrice in un formato leggibile, aggiungendo la costante se è disponibile."""
  
    for i in range(len(matrice)):
      
        for j in range(len(matrice[i])):
          
            print(matrice[i][j], end=" ")
          
        print("\n")

def main():
  
    """Funzione principale che genera e verifica quadrati magici."""
  
    numeri_validi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  
    while True:
      
        matrice = genera_matrice(3, numeri_validi)
      
        verifica = verifica_quadrato_magico(matrice)
      
        if verifica:
          
            break
          
        else:
          
            continue
          
    return f"{matrice} è un quadrato perfetto"

if __name__ == "__main__":
    print(main())
