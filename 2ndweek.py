import datetime
def assistente_virtuale(comando):
    if comando == "Qual è la data di oggi?":
        oggi = datetime.datetoday() 	       #datetime.date.today() verificato su internet..da libreria
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."
    return risposta
while True				 		# while True:
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))


'''
il programma dato propone un assistente virtuale che è in grado di rispondere a 3 domande : qual è la data di oggi, che ore sono e come ti chiami. Nel caso in cui l utente digiti male la richiesta o faccia una domanda non prevista l assistente risponde che non ha capito la domanda.
Al di la' degli errori di sintassi trovati sopra e corretti con commento, un importante errore è che l assistente virtuale esordisce come primo output con " Cosa vuoi sapere?" all utente. L utente non sa a cosa puo' rispondere l assistente.
Quindi nel programma sotto ho introdotto alcune migliorie per far sapere all utente cosa puo' fare l assistente 

Benvenuto! Puoi chiedere:
1 Qual è la data di oggi?
2 Che ore sono?
3 Come ti chiami?
4 Per terminare.
Cosa vuoi sapere?Seleziona il numero corrispondente 

questo sara' il primo output dell assistente così che l utente sa cosa puo' fare.
poi la selezione è numerica cosi' che non ci siano problemi di utilizzo da parte dell utente (maiuscole, minuscole , errori di grammatica) e rendendo l assistente virtuale facilmente friubile.
dopo ogni selezione l assistente continua a chiedere all utente 
Cosa vuoi sapere?Seleziona il numero corrispondente 
finchè l utente non seleziona 4, a quel punto l assistente risponde Arrivederci ed esce.

'''





import datetime


def assistente_virtuale(comando):
    if comando == "1":
        oggi = datetime.date.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "2":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "3":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."
    return risposta

print("Benvenuto! Puoi chiedere:")
print("1 Qual è la data di oggi?")
print("2 Che ore sono?")
print("3 Come ti chiami?")
print("4 Per terminare.")

while True:
    comando_utente = input("\nCosa vuoi sapere?Seleziona il numero corrispondente ")
    if comando_utente == "4":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))


