dicionario = {                           # Can have different data types as values and is a combination of key-value pairs
    "chave" : "valor",
    "fruta" : "maçã",
    "nomes" : ["Gabriel", "Maria", "José"],
    "valido" : True
}

print(dicionario["chave"])                 # Prints the value associated with "chave"
print(dicionario.get("fruta", "Chave não encontrada")) # Can only get existing values. If the key doesn't exist, it returns None instead of an error.
                                                       # Can be used with a default value as a second argument (Chave não encontrada)
dicionario["novo"] = "novo valor"  # Adds a new key-value pair to the dictionary
print(dicionario)

del dicionario["valido"]          # Deletes the key-value pair with key "valido"
print(dicionario)

print(dicionario.keys())                 # Returns a view object with all the keys in the dictionary
print(dicionario.values())               # Returns a view object with all the values in the dictionary
print(dicionario.items())                # Returns a view object with all key-value pairs in the dictionary

listacarros = ["BMW", "Audi", "Mercedes", "Fusca"]  # List of cars

cardictionary = {
    "Carro " + str(i+1): carro
    for i, carro in enumerate(listacarros)
    if carro != "Fusca"
}                                        # Create a dict of cars with dictionary comprehensions without Fusquinha

print(list(enumerate(listacarros)))      
    
print(cardictionary)