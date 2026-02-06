# Moltiplicazione tra due polinomi
def moltiplica_polinomi(p1, p2):
    """Moltiplica due polinomi rappresentati come liste di coefficienti"""
    if not p1 or not p2:
        return []
    
    risultato = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            risultato[i + j] += p1[i] * p2[j]
    return risultato

# Lettura dei polinomi
print("=== MOLTIPLICAZIONE TRA POLINOMI ===\n")

grado1 = int(input("Inserisci il grado del primo polinomio: "))
lista1 = []
for i in range(grado1 + 1):
    coeff = int(input(f"Coefficiente x^{i} del primo polinomio: "))
    lista1.append(coeff)

grado2 = int(input("\nInserisci il grado del secondo polinomio: "))
lista2 = []
for i in range(grado2 + 1):
    coeff = int(input(f"Coefficiente x^{i} del secondo polinomio: "))
    lista2.append(coeff)

# Moltiplicazione
risultato = moltiplica_polinomi(lista1, lista2)

# Stampa i risultati
print("\nPrimo polinomio:", lista1)
print("Secondo polinomio:", lista2)
print("Risultato moltiplicazione:", risultato)


