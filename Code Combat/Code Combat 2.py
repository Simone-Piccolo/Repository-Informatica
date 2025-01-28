import random

#Giocatore1

PrimoGiocatore_Hp=(random.randint(80,100))

PrimoGiocatore_Shield=(random.randint(5,10))

PrimoGiocatore_Dadi=4

#Giocatore2

SecondoGiocatore_Hp=(random.randint(80,100))

SecondoGiocatore_Shield=(random.randint(5,10))

SecondoGiocatore_Dadi=2

#Svolgimento del gioco

PrimoGiocatore_Dadi=(random.randint(1,6))

SecondoGiocatore_Dadi=(random.randint(1,12))

while PrimoGiocatore_Hp<=0 and SecondoGiocatore_Hp<=0:
  
  turni=turni+1
  
  Somma1=0
  
  Somma2=0
  
  for i in range(0,4):
    
   Somma1+=random.randint(1,6)
    
   PrimoGiocatore_Hp=Somma1-SecondoGiocatore_Shield
    
   SecondoGiocatore_Hp=PrimoGiocatore_Hp
    
