x= int(input("Digita un numero intero:")) 
if x<19:
  x = 25 - x
if x % 2 == 0:
   x = x * x - 32
else: 
    if (x > 13):
      x = 2 * x - 25
    else:  
        x = x -2
print(x)
if x % 2 == 0:
  y = input("Digita il tuo nome: ")
  w = input("Digita il tuo cognome: ")
  z = int(input("Digita il tuo numero di registro:"))
  l =len(y)
  l1 = len(w)
  if z % 2 == 0 or z % 5 == 0:
    c = y[:-1] + w[1:]
  else: 
      if l > 4 and l1 >= 5:
        c = y[-3:] + w[:4]
      else:
          c = (y) + (w)
else:
    s1 = str(input("Digita una parola: "))
    s2 = str(input("Digita un altra parola: "))
    n1 = int(input("Digita un numero: "))
    n2 = int(input("Digita un altro numero: "))
    c1 = s1[:n1]
    c2 = s2[n1:n2+1]
    c3 = s1[n2:]
    c = c1+c2+c3
print(c)

