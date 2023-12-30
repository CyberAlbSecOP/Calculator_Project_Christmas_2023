lista_op = ["addizione", "sottrazione", "moltiplicazione", "divisione", "esponenza", "binario"]
print("Le operazioni disponibili sono:", lista_op)
op_scelta = input("Che operazione vuoi fare?    ")
if op_scelta == "addizione":
    try:
        add_val_1 = float(input("Scrivi un numero:    "))
        add_val_2 = float(input("Scrivi un altro numero:    "))
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    else:
        risultato_add = add_val_1 + add_val_2
        print(add_val_1, "+", add_val_2, "=", risultato_add)
elif op_scelta == "sottrazione":
    try:
        sott_val_1 = float(input("Scrivi un numero:    "))
        sott_val_2 = float(input("Scrivi un altro numero:    "))
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    else:
        risultato_sott = sott_val_1 - sott_val_2
        print(sott_val_1, "-", sott_val_2, "=", risultato_sott)
elif op_scelta == "molteplicazione":
    try:
        molt_val_1 = float(input("Scrivi un numero:    "))
        molt_val_2 = float(input("Scrivi un altro numero:    "))
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    else:
        risultato_molt = molt_val_1 * molt_val_2
        print(molt_val_1, "*", molt_val_2, "=", risultato_molt)
elif op_scelta == "divisione":
    try:
        div_val_1 = float(input("Scrivi un numero:    "))
        div_val_2 = float(input("Scrivi un altro numero:    "))
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    else:
        risultato_div = div_val_1 / div_val_2
        print(div_val_1, "/", div_val_2, "=", risultato_div)
elif op_scelta == "esponenza":
    try:
        esp_val_1 = float(input("Scrivi un numero:    "))
        esp_val_2 = float(input("Scrivi un altro numero:    "))
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    else:
        risultato_esp = esp_val_1 ** esp_val_2
        print(esp_val_1, "^", esp_val_2, "=", risultato_esp)
elif op_scelta == "binario":
    try:
        bin_val_1 = int(input("Scrivi un numero:    "))
    except ValueError as e:
        print("I valori inseriti non sono numeri!")
    else:
        risultato_bin = bin(bin_val_1)
        print(bin_val_1, "=", risultato_bin)
else:
    print("L'input inserito non è valido!")