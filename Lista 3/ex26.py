'''
26. Inverta os elementos de uma lista sem usar o m´etodo reverse.
'''

lista = ["ao", "contrario", 'de', "um"]

print(lista)

n = len(lista)

for i in range(0, n - 1):
    reclycle = lista.pop(0)
    lista.append(reclycle)
    
print(lista.reverse)


