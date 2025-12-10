from arma import Arma                  

class Giocatore:                       # Definizione della classe Giocatore
    def __init__(self, nome: str, salute_massima: int, forza: int, destrezza: int):
        self.nome = nome               # Nome del giocatore

        # Imposta la salute massima, assicurandosi che sia almeno 1
        self.salute_massima = max(1, salute_massima)

        # All'inizio la salute attuale è uguale a quella massima
        self.salute = self.salute_massima

        # Forza compresa tra 1 e 20
        self.forza = max(1, min(20, forza))

        # Destrezza compresa tra 1 e 20
        self.destrezza = max(1, min(20, destrezza))

        # L’arma può essere un oggetto Arma o None se non equipaggiata
        self.arma: Arma | None = None

        
        self.buff = {"forza": 0, "destrezza": 0}

    def equipaggia(self, arma: Arma):
        self.arma = arma               # Assegna un'arma al giocatore

    def modificatore(self, valore: int) -> int:
        # Calcola il modificatore  
        return (valore - 10) // 2

    def è_vivo(self) -> bool:
        # Ritorna True se la salute è maggiore di 0
        return self.salute > 0

    def subisce(self, danno: int) -> int:
        # Impedisce che il danno vada sotto zero
        danno_effettivo = max(0, danno)

        # Riduce la salute assicurandosi che non scenda sotto 0
        self.salute = max(0, self.salute - danno_effettivo)

        return danno_effettivo         # Ritorna il danno realmente subito

    def attacca(self, nemico: "Giocatore") -> dict:
        # Se il giocatore non ha arma, attacca con le mani nude
        if self.arma is None:
            danno_base = 1             # Danno minimo delle mani nude
            stat_eff = self.modificatore(self.forza + self.buff["forza"])
            tipo_arma = "mani nude"
        else:
            # Ottiene il danno base dell'arma
            danno_base = self.arma.get_danno()

            # Usa la forza per armi da mischia, destrezza per armi a distanza
            if self.arma.tipo == "mischia":
                stat_eff = self.modificatore(self.forza + self.buff["forza"])
            else:
                stat_eff = self.modificatore(self.destrezza + self.buff["destrezza"])

            tipo_arma = self.arma.nome

        # Calcola danno totale evitando i valori negativi
        danno_totale = max(0, danno_base + stat_eff)

        # Il nemico subisce il danno
        danno_inflitto = nemico.subisce(danno_totale)

        # Restituisce un dizionario con i dettagli dell'attacco
        return {
            "attaccante": self.nome,
            "difensore": nemico.nome,
            "danno": danno_inflitto,
            "arma": tipo_arma,
            "stat_eff": stat_eff
        }

    def aggiungi_buff(self, stat: str, valore: int):
        # Aggiunge un buff alla statistica indicata se esiste
        if stat in self.buff:
            self.buff[stat] += valore

    def heal(self, valore: int) -> int:
        # Calcola quanto può essere curato senza superare la salute massima
        curato = min(valore, self.salute_massima - self.salute)

        # Aumenta la salute
        self.salute += curato
        return curato                  

    def stato(self) -> dict:
        # Restituisce un dizionario con tutte le informazioni del giocatore
        return {
            "nome": self.nome,
            "salute": self.salute,
            "salute_massima": self.salute_massima,
            "forza": self.forza,
            "destrezza": self.destrezza,
            "buff_forza": self.buff["forza"],
            "buff_destrezza": self.buff["destrezza"],
            "arma": str(self.arma) if self.arma else "mani nude"
        }

    def tick_buffs(self):
        pass

