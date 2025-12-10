import random
from arma import Arma                   
from giocatore import Giocatore         
from pozione import Pozione            
from view import ConsoleView            
from controller import GameController  

def main():
    # Creazione del primo giocatore "Gimli" con statistiche casuali
    gimli = Giocatore(
        "Gimli",
        salute_massima=random.randint(30, 60),   
        forza=random.randint(5, 20),            
        destrezza=random.randint(5, 20)         
    )
    
    # Creazione del secondo giocatore "Legolas" con statistiche casuali
    legolas = Giocatore(
        "Legolas",
        salute_massima=random.randint(30, 60),
        forza=random.randint(5, 20),
        destrezza=random.randint(5, 20)
    )

    # Creazione di una spada lunga con danno casuale
    spada = Arma(
        "Spada lunga",
        danno_minimo=random.randint(1, 5),
        danno_massimo=random.randint(5, 10),
        tipo="mischia"                          
    )
    
    # Creazione di un arco corto con danno casuale
    arco = Arma(
        "Arco corto",
        danno_minimo=random.randint(1, 4),
        danno_massimo=random.randint(3, 8),
        tipo="distanza"                          
    )
    
    # Equipaggia Gimli con spada o arco in modo casuale
    gimli.equipaggia(spada if random.choice([True, False]) else arco)
    # Equipaggia Legolas con arco o spada in modo casuale
    legolas.equipaggia(arco if random.choice([True, False]) else spada)

    # Definizione delle pozioni di Gimli
    pozioni_gimli = [
        Pozione("Pozione curativa", "cura", random.randint(5, 15)),     
        Pozione("Pozione forza", "buff_forza", random.randint(1, 5))     
    ]
    
    # Definizione delle pozioni di Legolas
    pozioni_legolas = [
        Pozione("Pozione curativa", "cura", random.randint(5, 15)),    
        Pozione("Pozione destrezza", "buff_destrezza", random.randint(1, 5)) 
    ]

    # Creazione della view (console testuale)
    view = ConsoleView()
    # Creazione del game controller con giocatori, view e pozioni
    controller = GameController(view, gimli, legolas, pozioni_gimli, pozioni_legolas)
    # Avvio del loop principale del gioco
    controller.start_game_loop()


if __name__ == "__main__":
    main()
