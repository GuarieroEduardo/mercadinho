import json
lista = []

lista.append({"rafa": "123"})
with open('banco_de_dados.json', 'r') as file:
    lista = json.load(file)


with open('banco_de_dados.json', 'w') as file:
    json.dump(lista, file)
