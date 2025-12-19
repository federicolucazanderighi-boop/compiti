parola=str(input('inserisci una parola:  '))
lettera_inserita=str(input('inserisci una lettera:  '))
i=0
j=0
conta=0
while i != len(parola):
    if parola[j]==lettera_inserita:
        conta=conta+1
    i=i+1
    j=j+1
print(conta)