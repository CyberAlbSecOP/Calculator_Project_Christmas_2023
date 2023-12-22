esp_val_1 = input("Scrivi un numero:    ")
#definisco prima variabile = int / float
esp_val_2 = input("Scrivi un altro numero:    ")
#definisco seconda variabile = int / float
try:
    esp_val_1_float = float(esp_val_1)
    esp_val_2_float = float(esp_val_2)
except ValueError as e:
    print("Il valore inserito non è un numero!")
else:
    risultato_esp = esp_val_1 ** esp_val_2
    print(esp_val_1, "**", esp_val_2, "=", risultato_esp)
#eseguo esponenza e stampo risultato
    
#DIVISIONE
div_val_1 = input("Scrivi un numero:    ")
#definisco prima variabile = int / float
div_val_2 = input("Scrivi un altro numero:    ")
#definisco seconda variabile = int / float
try:
    div_val_1_float = float(div_val_1)
    div_val_2_float = float(div_val_2)
except ValueError as e:
    print("I valori inseriti non sono numeri!")
else:
    risultato_div = div_val_1 / div_val_2
    print(div_val_1, "/", div_val_2, "=", risultato_div)
#eseguo divisione e stampo risultato