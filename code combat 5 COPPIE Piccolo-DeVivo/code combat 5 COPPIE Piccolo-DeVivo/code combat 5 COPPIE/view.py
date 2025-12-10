from colorama import Fore, Style, init      # Importa strumenti per colorare il testo in console

init(autoreset=True)                        # Inizializza colorama e resetta automaticamente i colori dopo ogni print

class ConsoleView:                           

    def show_welcome(self):                 
        print(Fore.CYAN + Style.BRIGHT + "\n===================================")
        print(Fore.CYAN + Style.BRIGHT + "     SIMULAZIONE DI COMBATTIMENTO  ")
        print(Fore.CYAN + Style.BRIGHT + "===================================\n")

    def show_initial_stats(self, p1_state: dict, p2_state: dict):
        print(Style.BRIGHT + "STATISTICHE INIZIALI:")  # Titolo della sezione
        for p in [p1_state, p2_state]:                 # Cicla sulle statistiche dei due giocatori
            print(
                f"- {Fore.GREEN}{p['nome']}{Style.RESET_ALL}: "               # Nome del giocatore colorato
                f"HP {Fore.GREEN}{p['salute']}/{p['salute_massima']}{Style.RESET_ALL}, "  # Salute
                f"FOR {p['forza']} (+{p['buff_forza']}), "                   # Stat forza con buff
                f"DEX {p['destrezza']} (+{p['buff_destrezza']}), "           # Stat destrezza con buff
                f"Arma: {Fore.CYAN}{p['arma']}"                               # Arma equipaggiata
            )
        print()                                         

    def show_turn_header(self, numero: int):
        # Mostra il titolo del turno
        print(Fore.MAGENTA + Style.BRIGHT + f"\n----------- TURNO {numero} -----------")

    def show_attack_result(self, info: dict):
        # Mostra il risultato di un attacco
        print(
            f"{Fore.GREEN}{info['attaccante']}{Style.RESET_ALL} "             # Nome attaccante
            f"attacca {Fore.GREEN}{info['difensore']}{Style.RESET_ALL} "     # Nome difensore
            f"[{info['arma']}, stat eff={info['stat_eff']}]: "               # Arma e stat usata
            f"{Fore.RED + Style.BRIGHT}infligge {info['danno']} danni!"      # Danni inflitti
        )

    def show_potion_decision(self, player_name: str, potion_name: str):
        # Mostra che il giocatore ha deciso di usare una pozione
        print(Fore.BLUE + f"{player_name} decide di usare '{potion_name}'")

    def show_potion_success(self, player_name: str, effect_desc: str, current_hp_msg: str = ""):
        # Messaggio di successo nel caso la pozione abbia avuto effetto
        print(Fore.BLUE + f"{player_name} usa la pozione: {effect_desc} {current_hp_msg}")

    def show_cannot_heal(self, player_name: str):
        # Messaggio specifico per il caso in cui il giocatore prova a curarsi con HP già pieni
        print(Fore.YELLOW + f"Azione Cura fallita: {player_name} ha già gli HP al massimo.")

    def show_player_dead(self, player_name: str):
        # Messaggio quando un giocatore viene sconfitto
        print(Fore.RED + Style.BRIGHT + f"💀 {player_name} è stato sconfitto!")

    def show_hp_status(self, p1_state: dict, p2_state: dict):
        # Mostra lo stato aggiornato degli HP dei due giocatori
        print(
            f"HP rimanenti: "
            f"{p1_state['nome']}: {p1_state['salute']}/{p1_state['salute_massima']}, "
            f"{p2_state['nome']}: {p2_state['salute']}/{p2_state['salute_massima']}"
        )

    def show_winner(self, nome: str):
        # Messaggio finale: mostra il vincitore
        print(Fore.YELLOW + Style.BRIGHT + f"\n🎉 {nome} ha vinto la partita! 🎉")
