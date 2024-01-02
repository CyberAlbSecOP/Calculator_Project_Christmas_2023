#LISTA OPERAZIONI
#creo la lista delle operazioni disponibili e la stampo
lista_op = ["addizione", "sottrazione", "moltiplicazione", "divisione", "esponenza", "binario"]
print("Le operazioni disponibili sono:", lista_op)


#INPUT OPERAZIONE
#chiedo all'utente quale operazione vuole fare
op_scelta = input("Che operazione vuoi fare?    ")
#se l'utente inserisce un'operazione non valida, stampo un messaggio di errore
while op_scelta not in lista_op:
    print("Operazione non valida! Controlla l'ortografia! Inserisci un'operazione tra quelle disponibili:", lista_op)
    op_scelta = input("Che operazione vuoi fare?    ")


#ADDIZIONE
#definisco la funzione addizione
def addizione():
    #creo un ciclo while per ripetere la richiesta di valori finché l'utente non inserisce due valori numerici
    while True:
        #provo a chiedere due valori
        try:
            add_val_1 = float(input("Scrivi un numero:    "))
            add_val_2 = float(input("Scrivi un altro numero:    "))
            #se l'utente inserisce due valori numerici, stampo il risultato
            risultato_add = add_val_1 + add_val_2
            print(add_val_1, "+", add_val_2, "=", risultato_add)
            #se l'utente inserisce due valori numerici, esco dal ciclo while
            break
        #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
        except ValueError:
            print("I valori inseriti non sono numeri!")
#se l'utente sceglie addizione, eseguo la funzione addizione
if op_scelta == "addizione":
    addizione()