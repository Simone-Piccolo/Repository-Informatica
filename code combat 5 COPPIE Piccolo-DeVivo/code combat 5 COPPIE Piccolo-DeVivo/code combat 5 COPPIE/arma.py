import random                    

class Arma:                       
    def __init__(self, nome: str, danno_minimo: int, danno_massimo: int, tipo: str):
        # Metodo costruttore che inizializza una nuova istanza della classe 'Arma'
        
        self.nome = nome          # Salva il nome dell’arma nell’attributo 'nome'
        
        # Imposta il danno minimo, assicurandosi che non sia mai inferiore a 1
        self.danno_minimo = max(1, danno_minimo)
        
        # Imposta il danno massimo, assicurandosi che sia almeno uguale al danno minimo
        self.danno_massimo = max(self.danno_minimo, danno_massimo)
        
        # Controlla se il tipo dell’arma è valido: deve essere 'mischia' o 'distanza'
        if tipo in ["mischia", "distanza"]:
            self.tipo = tipo      # Se valido, assegna il tipo all’attributo 'tipo'
        else:
            # Se non valido, solleva un errore 
            raise ValueError("Il tipo deve essere 'mischia' o 'distanza'.")

    def get_danno(self) -> int:
        # Metodo che restituisce un danno casuale tra minimo e massimo
        return random.randint(self.danno_minimo, self.danno_massimo)

    def __str__(self):
        # Metodo speciale che restituisce una stringa rappresentativa dell'oggetto
        return f"{self.nome} ({self.danno_minimo}-{self.danno_massimo} danni, tipo: {self.tipo})"

