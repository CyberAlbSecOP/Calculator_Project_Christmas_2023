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


#SOTTRAZIONE
#definisco la funzione sottrazione
def sottrazione():
    #provo a chiedere due valori
    try:
        sott_val_1 = float(input("Scrivi un numero:    "))
        sott_val_2 = float(input("Scrivi un altro numero:    "))
#se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    #se l'utente inserisce due valori numerici, stampo il risultato
    else:
        risultato_sott = sott_val_1 - sott_val_2
        print(sott_val_1, "-", sott_val_2, "=", risultato_sott)
#se l'utente sceglie sottrazione, eseguo la funzione sottrazione
if op_scelta == "sottrazione":
    sottrazione()


#MOLTIPLICAZIONE
#definisco la funzione moltiplicazione
def moltiplicazione():
    #provo a chiedere due valori
    try:
        molt_val_1 = float(input("Scrivi un numero:    "))
        molt_val_2 = float(input("Scrivi un altro numero:    "))
#se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    #se l'utente inserisce due valori numerici, stampo il risultato
    else:
        risultato_molt = molt_val_1 * molt_val_2
        print(molt_val_1, "*", molt_val_2, "=", risultato_molt)
#se l'utente sceglie moltiplicazione, eseguo la funzione moltiplicazione
if op_scelta == "moltiplicazione":
    moltiplicazione()

#DIVISIONE
#definisco la funzione divisione
def divisione():
    #provo a chiedere due valori
    try:
        div_val_1 = float(input("Scrivi un numero diverso da zero:    "))
        div_val_2 = float(input("Scrivi un altro numero diverso da zero:    "))
    #se il secondo valore è 0, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    except ZeroDivisionError as e:
        print("Non puoi dividere per 0!")
    #se l'utente inserisce due valori numerici, stampo il risultato
    else:
        risultato_div = div_val_1 / div_val_2
        print(div_val_1, "/", div_val_2, "=", risultato_div)
#se l'utente sceglie divisione, eseguo la funzione divisione
if op_scelta == "divisione":
    divisione()

#ESPONENZA
#definisco la funzione esponenza
def esponenza():
    #provo a chiedere due valori
    try:
        esp_val_1 = float(input("Scrivi un numero diverso da zero:    "))
        esp_val_2 = float(input("Scrivi un altro numero diverso da zero:    "))
        #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
        #se l'utente inserisce due valori numerici, stampo il risultato  
    else:
        risultato_esp = esp_val_1 ** esp_val_2
        print(esp_val_1, "^", esp_val_2, "=", risultato_esp)
#se l'utente sceglie esponenza, eseguo la funzione esponenza
if op_scelta == "esponenza":
    esponenza()

#BINARIO
#definisco la funzione binario
def binario():
    #provo a chiedere un valore
    try:
        bin_val_1 = int(input("Scrivi un numero:    "))
    #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    #se l'utente inserisce un valore numerico, stampo il risultato
    else:
        risultato_bin = bin(bin_val_1)
        print(bin_val_1, "=", risultato_bin)
#se l'utente sceglie binario, eseguo la funzione binario
if op_scelta == "binario":
    binario()