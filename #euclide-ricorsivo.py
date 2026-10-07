#euclide_ricorsivo
def euclide(a, b):
    if b == 0:
        return a
    else:
        return euclide(b, a % b)
print(euclide(48, 18))
