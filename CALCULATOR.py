#LISTA OPERAZIONI
#creo la lista delle operazioni disponibili e la stampo
lista_op = ["addizione", "sottrazione", "moltiplicazione", "divisione", "esponenza", "binario"]
print("Le operazioni disponibili sono:", lista_op)


#INPUT OPERAZIONE
#chiedo all'utente quale operazione vuole fare
op_scelta = input("Che operazione vuoi fare?    ")


#ADDIZIONE
#se l'utente sceglie addizione, provo a chiedere due valori
if op_scelta == "addizione":
    try:
        add_val_1 = float(input("Scrivi un numero:    "))
        add_val_2 = float(input("Scrivi un altro numero:    "))
#se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
#se l'utente inserisce due valori numerici, stampo il risultato
    else:
        risultato_add = add_val_1 + add_val_2
        print(add_val_1, "+", add_val_2, "=", risultato_add)


#SOTTRAZIONE
#se l'utente sceglie sottrazione, provo a chiedere due valori
elif op_scelta == "sottrazione":
    try:
        sott_val_1 = float(input("Scrivi un numero:    "))
        sott_val_2 = float(input("Scrivi un altro numero:    "))
#se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    else:
        risultato_sott = sott_val_1 - sott_val_2
        print(sott_val_1, "-", sott_val_2, "=", risultato_sott)


#MOLTIPLICAZIONE
#se l'utente sceglie moltiplicazione, provo a chiedere due valori
elif op_scelta == "molteplicazione":
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


#DIVISIONE
#se l'utente sceglie divisione, provo a chiedere due valori
elif op_scelta == "divisione":
    try:
        div_val_1 = float(input("Scrivi un numero:    "))
        div_val_2 = float(input("Scrivi un altro numero:    "))
#se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
#se l'utente inserisce due valori numerici, stampo il risultato
    else:
        risultato_div = div_val_1 / div_val_2
        print(div_val_1, "/", div_val_2, "=", risultato_div)


#ESPONENZA
#se l'utente sceglie esponenza, provo a chiedere due valori
elif op_scelta == "esponenza":
    try:
        esp_val_1 = float(input("Scrivi un numero:    "))
        esp_val_2 = float(input("Scrivi un altro numero:    "))
#se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
#se l'utente inserisce due valori numerici, stampo il risultato    
    else:
        risultato_esp = esp_val_1 ** esp_val_2
        print(esp_val_1, "^", esp_val_2, "=", risultato_esp)


#BINARIO
#se l'utente sceglie binario, provo a chiedere un valore
elif op_scelta == "binario":
    try:
        bin_val_1 = int(input("Scrivi un numero:    "))
#se l'utente inserisce un valore non numerico, stampo un messaggio di errore
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
#se l'utente inserisce un valore numerico, stampo il risultato
    else:
        risultato_bin = bin(bin_val_1)
        print(bin_val_1, "=", risultato_bin)

#INPUT NON VALIDO
#se l'utente inserisce un input non valido, stampo un messaggio di errore
else:
    print("L'input inserito non è valido!")