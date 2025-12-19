numero = input("Inserisci il numero: ")
if numero % 1 != numero:
    print("Errore")
else:
    ultima_cifra = int(numero[-1])
    if ultima_cifra % 2 == 0:
        print("Il numero è pari")
    else:
        print("Il numero è dispari")
