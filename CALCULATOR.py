#CICLO DI RIPETIZIONE
#creo un ciclo while per ripetere il codice una volta completata l'operazione
while True:
    #creo la funzione calcolatrice
    def calcolatrice():
        
        
        #AVVIO
        print("Calcolatrice in esecuzione!")
        #creo un ciclo while per ripetere l'avvio finché l'utente non inserisce "si" o "no"
        while True:
            #chiedo all'utente se vuole avviare il programma
            avvio = input("Vuoi eseguire un calcolo? (si/no)    ")
            #se l'utente inserisce "si", esco dal ciclo while
            if avvio == "si":
                break
            #se l'utente inserisce "no", stampo un messaggio di arrivederci e chiudo il programma
            elif avvio == "no":
                print("Arrivederci!")
                exit()
            #se l'utente inserisce un valore diverso da "si" o "no", stampo un messaggio di errore
            else:
                print("Risposta non valida!")
        
        
        #LISTA OPERAZIONI
        #creo la lista delle operazioni disponibili e la stampo
        lista_op = ["addizione", "sottrazione", "moltiplicazione", "divisione", "esponenza", "binario", "radice quadrata", "esci"]
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
            #creo un ciclo while per ripetere la richiesta di valori finché l'utente non inserisce due valori numerici
            while True:
                #provo a chiedere due valori
                try:
                    sott_val_1 = float(input("Scrivi un numero:    "))
                    sott_val_2 = float(input("Scrivi un altro numero:    "))
                    #se l'utente inserisce due valori numerici, stampo il risultato
                    risultato_sott = sott_val_1 - sott_val_2
                    print(sott_val_1, "-", sott_val_2, "=", risultato_sott)
                    #se l'utente inserisce due valori numerici, esco dal ciclo while
                    break
                #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
                except ValueError:
                    print("I valori inseriti non sono numeri!")
        #se l'utente sceglie sottrazione, eseguo la funzione sottrazione
        if op_scelta == "sottrazione":
            sottrazione()


        #MOLTIPLICAZIONE
        #definisco la funzione moltiplicazione
        def moltiplicazione():
            #creo un ciclo while per ripetere la richiesta di valori finché l'utente non inserisce due valori numerici
            while True:
                #provo a chiedere due valori
                try:
                    molt_val_1 = float(input("Scrivi un numero:    "))
                    molt_val_2 = float(input("Scrivi un altro numero:    "))
                    #se l'utente inserisce due valori numerici, stampo il risultato
                    risultato_molt = molt_val_1 * molt_val_2
                    print(molt_val_1, "*", molt_val_2, "=", risultato_molt)
                    #se l'utente inserisce due valori numerici, esco dal ciclo while
                    break
                #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
                except ValueError:
                    print("I valori inseriti non sono numeri!")
        #se l'utente sceglie moltiplicazione, eseguo la funzione moltiplicazione
        if op_scelta == "moltiplicazione":
            moltiplicazione()


        #DIVISIONE
        #definisco la funzione divisione
        def divisione():
            #creo un ciclo while per ripetere la richiesta di valori finché l'utente non inserisce due valori numerici
            while True:
                #provo a chiedere due valori
                try:
                    div_val_1 = float(input("Scrivi un numero:    "))
                    div_val_2 = float(input("Scrivi un altro numero:    "))
                    #se l'utente inserisce due valori numerici, stampo il risultato
                    risultato_div = div_val_1 / div_val_2
                    print(div_val_1, "/", div_val_2, "=", risultato_div)
                    #se l'utente inserisce due valori numerici, esco dal ciclo while
                    break
                #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
                except ValueError:
                    print("I valori inseriti non sono numeri!")
                #se l'utente inserisce zero come secondo valore, stampo un messaggio di errore
                except ZeroDivisionError:
                    print("Non puoi dividere per zero!")
        #se l'utente sceglie divisione, eseguo la funzione divisione
        if op_scelta == "divisione":
            divisione()


        #ESPONENZA
        #definisco la funzione esponenza
        def esponenza():
            #creo un ciclo while per ripetere la richiesta di valori finché l'utente non inserisce due valori numerici
            while True:
                #provo a chiedere due valori
                try:
                    esp_val_1 = float(input("Scrivi un numero:    "))
                    esp_val_2 = float(input("Scrivi un altro numero:    "))
                    #se l'utente inserisce due valori numerici, stampo il risultato
                    risultato_esp = esp_val_1 ** esp_val_2
                    print(esp_val_1, "^", esp_val_2, "=", risultato_esp)
                    #se l'utente inserisce due valori numerici, esco dal ciclo while
                    break
                #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
                except ValueError:
                    print("I valori inseriti non sono numeri!") 
        #se l'utente sceglie esponenza, eseguo la funzione esponenza
        if op_scelta == "esponenza":
            esponenza()


        #BINARIO
        #definisco la funzione binario
        def binario():
            #creo un ciclo while per ripetere la richiesta di valori finché l'utente non inserisce un valore numerico
            while True:
                #provo a chiedere un valore
                try:
                    bin_val = int(input("Scrivi un numero:    "))
                    #se l'utente inserisce un valore numerico, stampo il risultato
                    risultato_bin = bin(bin_val)
                    print(bin_val, "in binario è", risultato_bin)
                    #se l'utente inserisce un valore numerico, esco dal ciclo while
                    break
                #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
                except ValueError:
                    print("Il valore inserito non è un numero!")
        #se l'utente sceglie binario, eseguo la funzione binario
        if op_scelta == "binario":
            binario()
                

        #RADICE QUADRATA
        #definisco la funzione radice quadrata
        def radice_quadrata():
            #creo un ciclo while per ripetere la richiesta di valori finché l'utente non inserisce un valore numerico
            while True:
                #provo a chiedere un valore
                try:
                    radq_val = float(input("Scrivi un numero:    "))
                    #se l'utente inserisce un valore numerico, stampo il risultato
                    risultato_radq = radq_val ** 0.5
                    print("La radice quadrata di", radq_val, "è", risultato_radq)
                    #se l'utente inserisce un valore numerico, esco dal ciclo while
                    break
                #se l'utente inserisce un valore non numerico, stampo un messaggio di errore
                except ValueError:
                    print("Il valore inserito non è un numero!")
        #se l'utente sceglie radice quadrata, eseguo la funzione radice quadrata
        if op_scelta == "radice quadrata":
            radice_quadrata()


        #


        #ESCI
        #definisco la funzione esci
        def esci():
            #stampo un messaggio di arrivederci
            print("Uscendo dalla calcolatrice...")
            print("Arrivederci!")
        if op_scelta == "esci":
            esci()

 
    #RICHIAMO LA FUNZIONE CALCOLATRICE
    calcolatrice()