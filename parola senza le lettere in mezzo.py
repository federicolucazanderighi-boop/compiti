# parola senza le lettere in mezzo
nome=input("Inserisci un nome:")
l = len(nome)
d = l // 2
r = l % 2
if r == 0:
    nome1= nome[:d-1] + nome[d+1:]
else:
    nome1= nome[:d] + nome[d+1:]
print(nome1)
