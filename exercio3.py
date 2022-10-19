tupla = ("Fortaleza", "3.4302", "38.3235")
print(f"A cidade de {tupla[0]} tem lat {tupla[1]} e log {tupla [2]}")


lista = (list(tupla))
lista[0] = "olinda"
lista[1] = "8.034"
lista[2] = "34.5119"
print(lista)

tupla = tuple(lista)
print(tupla)
print(type(tupla))
print(f"A cidade de {tupla[0]} tem lat {tupla[1]} e log {tupla [2]}")