a = input("Digita il tuo nome: ")
b = input("Digita il tuo cognome: ")
c = int(input("Digita il tuo numero di registro: "))
l = len(a)
l1 = len(b)
if c % 2 == 0 or c % 5 == 0:
    d = a[: -1] + b[1:]
else: 
    if l > 4 and l1 >= 5:
        d = a[-3:] + b[:4]
    else:
        d = (b) + (a)
print(d)