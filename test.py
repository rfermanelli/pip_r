numero_studenti = int(input("Inserisci numero di studenti: "))
i = 0
studenti = []
s = []
while i < numero_studenti:
    s= {"nome" : input("Inserisci nome: "),
                   "età" : int(input("inserisci età: ")),
                   "voto_finale" : float(input("inserisci voto finale: "))
                   }
    studenti.append(s)
    i = i + 1
    s = []
for studente in studenti:
    print("Nome:", studente["nome"], "   Voto finale:", studente["voto_finale"])
totale_voti = 0
contatore_voti = 0
while contatore_voti < numero_studenti:
    totale_voti = totale_voti + studente["voto_finale"]
    contatore_voti = contatore_voti + 1
media_totale = totale_voti / contatore_voti
print(totale_voti)
print("Media di tutti i voti: ",media_totale)