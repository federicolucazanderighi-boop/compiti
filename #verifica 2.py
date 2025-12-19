#verifica 2
s = str(input("Inserisci la stringa: "))
l = len(s)
n_s=""
posizione = 0
while l > posizione:
    if s[posizione] != "a" and s[posizione] != "e" and s[posizione] != "i" and s[posizione] != "o" and s[posizione] != "u":
        n_s = n_s + s[posizione] + "o" + s[posizione]
    else:
        n_s = n_s +s[posizione]
    posizione += 1
print (n_s)