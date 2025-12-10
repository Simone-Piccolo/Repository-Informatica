import random                     

class GameController:               # Definisce la classe che controlla il flusso della partita
    def __init__(self, view, giocatore1, giocatore2, pozioni_p1=None, pozioni_p2=None):
        self.view = view            # Riferimento all'interfaccia/view per mostrare messaggi all'utente
        self.p1 = giocatore1        # Giocatore 1 
        self.p2 = giocatore2        # Giocatore 2 
        self.p1_pozioni = pozioni_p1 or []  # Lista di pozioni per il giocatore 1 (vuota se None)
        self.p2_pozioni = pozioni_p2 or []  # Lista di pozioni per il giocatore 2 (vuota se None)

    def start_game_loop(self):
        self.view.show_welcome()    # Mostra messaggio di benvenuto tramite la view
        self.view.show_initial_stats(self.p1.stato(), self.p2.stato())  # Mostra le statistiche iniziali dei due giocatori

        turno = 1                   # Contatore del turno (parte da 1)
        # Loop principale: continua finché entrambi i giocatori sono vivi
        while self.p1.è_vivo() and self.p2.è_vivo():
            self.view.show_turn_header(turno)  # Visualizza header del turno corrente

            # Prepara la lista dei giocatori in formato (attaccante, difensore, lista_pozioni)
            giocatori = [(self.p1, self.p2, self.p1_pozioni), (self.p2, self.p1, self.p2_pozioni)]
            random.shuffle(giocatori)  # Mescola l'ordine per decidere chi agisce prima in questo turno

            # Per ogni coppia (attaccante, difensore, pozioni) nello stesso turno...
            for attaccante, difensore, pozioni in giocatori:
                # ...esegui l'azione solo se entrambi sono ancora vivi (uno potrebbe essere morto prima nel turno)
                if attaccante.è_vivo() and difensore.è_vivo():
                    self.handle_turn(attaccante, difensore, pozioni)

            turno += 1  # Incrementa il contatore dei turni

        # Al termine del loop, determina il vincitore (chi è ancora vivo)
        vincitore = self.p1.nome if self.p1.è_vivo() else self.p2.nome
        self.view.show_winner(vincitore)  # Mostra il vincitore tramite la view

    def handle_turn(self, attaccante, difensore, pozioni):
        # Se il giocatore ha pozioni disponibili e la scelta casuale restituisce True, userà una pozione
        if pozioni and random.choice([True, False]):
            pozione = pozioni.pop(0)  # Prende la prima pozione e la rimuove dall'inventario
            self.view.show_potion_decision(attaccante.nome, pozione.nome)  # Mostra la decisione di usare la pozione
            risultato = pozione.usa(attaccante)  # Applica l'effetto della pozione sul bersaglio (qui l'attaccante)

            # Gestione del risultato dell'uso della pozione
            if "errore" in risultato:
                # Se la pozione restituisce errore (es. già usata), mostra errore
                self.view.show_potion_success(attaccante.nome, f"Errore: {risultato['errore']}")
            elif risultato["effetto"] == "cura":
                # Se l'effetto è cura, verifica se ha curato effettivamente qualcosa
                if risultato["quantità"] == 0:
                    self.view.show_cannot_heal(attaccante.nome)  # Messaggio se la cura non ha effetto (HP già pieni)
                else:
                    # Messaggio dettagliato con HP aggiornati
                    curato_msg = f"-> {attaccante.nome} (HP: {attaccante.salute}/{attaccante.salute_massima})"
                    self.view.show_potion_success(attaccante.nome, f"{risultato['effetto']} +{risultato['quantità']}", curato_msg)
            else:
                # Altri tipi di effetto (es. buff): mostra successo con la quantità del buff
                self.view.show_potion_success(attaccante.nome, f"{risultato['effetto']} +{risultato['quantità']}")
        else:
            # Altrimenti l'attaccante esegue un attacco sul difensore
            info_attacco = attaccante.attacca(difensore)
            self.view.show_attack_result(info_attacco)  # Mostra il risultato dell'attacco tramite la view
            if not difensore.è_vivo():
                # Se il difensore è morto dopo l'attacco, mostra messaggio di morte
                self.view.show_player_dead(difensore.nome)

        # Dopo l'azione (pozione o attacco) mostra gli HP aggiornati di entrambi i giocatori
        self.view.show_hp_status(self.p1.stato(), self.p2.stato())

        # Aggiorna i buff di entrambi i giocatori (metodo da implementare in Giocatore)
        attaccante.tick_buffs()
        difensore.tick_buffs()
