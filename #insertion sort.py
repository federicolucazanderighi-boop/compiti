#insertion sort
def ordinamento_numeri(l1):
    for i in range( len(l1)):
        h = l1[i]
        j = i - 1
        while j >= 0 and h < l1[j]:
            l1[j + 1] = l1[j]
            j -= 1
            l1[j + 1] = h
    return l1
nume=int(input("Quanti numeri ci saranno nella lista?:"))
numeri = []
for i in range(nume):
    numeri.append(int(input("Inserisci il numeri:")))





print(ordinamento_numeri(numeri))
