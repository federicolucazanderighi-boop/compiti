#massimo
a=int(input("Quanti numeri vuoi inserire:"))
b=int(input("inserisci un numero: "))
c=1
massimo=b
while c<a:
    b=int(input("inserisci un numero"))
    c+=1
    if b>massimo:
        massimo=b
print(massimo)
