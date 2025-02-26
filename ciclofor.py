r = range(0, 11)

lista = []
i = 1
while i <= 10:
    lista.append(i)
    i += 1
print (lista)

print("Stampo la lista")
for i in lista:
    print(i, end = " ")

print("stampo il range")
for i in r:
    print(i end = " ")

print("Il tipo di r è:", type(r))
print("Il tipo di l è:", type(r))