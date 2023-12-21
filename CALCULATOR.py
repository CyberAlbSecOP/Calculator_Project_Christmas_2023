#ADDIZIONE
add_val_1 = float(input("Scrivi un numero:    "))
#definisco prima variabile = int / float
add_val_2 = float(input("Scrivi un altro numero:    "))
#definisco seconda variabile = int / float
risultato_add = add_val_1 + add_val_2
print(add_val_1, "+", add_val_2, "=", risultato_add)
#eseguo addizione e stampo risultato

#SOTTRAZIONE
sott_val_1 = float(input("Scrivi un numero:    "))
#definisco prima variabile = int / float
sott_val_2 = float(input("Scrivi un altro numero:    "))
#definisco seconda variabile = int / float
risultato_sott = sott_val_1 - sott_val_2
print(sott_val_1, "-", sott_val_2, "=", risultato_sott)
#eseguo sottrazione e stampo risultato

#MOLTIPLICAZIONE
molt_val_1 = float(input("Scrivi un numero:    "))
#definisco prima variabile = int / float
molt_val_2 = float(input("Scrivi un altro numero:    "))
#definisco seconda variabile = int / float
risultato_molt = molt_val_1 * molt_val_2
print(molt_val_1, "*", molt_val_2, "=", risultato_molt)
#eseguo moltiplicazione e stampo risultato

#DIVISIONE
div_val_1 = float(input("Scrivi un numero:    "))
#definisco prima variabile = int / float
div_val_2 = float(input("Scrivi un altro numero:    "))
#definisco seconda variabile = int / float
risultato_div = div_val_1 / div_val_2
print(div_val_1, "/", div_val_2, "=", risultato_div)
#eseguo divisione e stampo risultato

#ESPONENZA
esp_val_1 = float(input("Scrivi un numero:    "))
#definisco prima variabile = int / float
esp_val_2 = float(input("Scrivi un altro numero:    "))
#definisco seconda variabile = int / float
risultato_esp = esp_val_1 ** esp_val_2
print(esp_val_1, "**", esp_val_2, "=", risultato_esp)
#eseguo esponenza e stampo risultato

#CONVERSIONE IN BINARIO
conv_bin_num = (input("Inserisci un numero intero:    "))
#definisco numero intero
try:
    conv_bin_num_int = int(conv_bin_num)
except ValueError as e:
    print("Il valore inserito non è un numero intero!") 
else:
    print(conv_bin_num_int, "=", bin(conv_bin_num_int))
#converto intero in binario e stampo