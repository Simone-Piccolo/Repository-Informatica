class Pozione:
    def __init__(self, nome: str, effetto: str, valore: int):
        self.nome = nome                    # Nome della pozione
        self.effetto = effetto              # Tipo di effetto: "cura", "buff_forza", "buff_destrezza"
        self.valore = valore                # Valore numerico dell'effetto (es: quanto cura o quanto buff)
        self.usata = False                  #  evitare usi multipli della stessa pozione

    def usa(self, target):
        # Verifica se la pozione è già stata usata: se sì, restituisce errore
        if self.usata:
            return {"errore": "già usata"}

        risultato = {}                      # Dizionario per contenere il risultato dell’uso

        # Caso 1: pozione di cura → chiama il metodo heal() del target
        if self.effetto == "cura":
            curato = target.heal(self.valore)   # Calcola quanto realmente cura
            risultato = {"effetto": "cura", "quantità": curato}

        # Caso 2: pozione che aumenta la forza → aggiunge un buff
        elif self.effetto == "buff_forza":
            target.aggiungi_buff("forza", self.valore)
            risultato = {"effetto": "buff_forza", "quantità": self.valore}

        # Caso 3: pozione che aumenta la destrezza → aggiunge un buff
        elif self.effetto == "buff_destrezza":
            target.aggiungi_buff("destrezza", self.valore)
            risultato = {"effetto": "buff_destrezza", "quantità": self.valore}

        # Segna la pozione come usata, così non può essere riutilizzata
        self.usata = True

        return risultato                    
