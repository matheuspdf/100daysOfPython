programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

# adicionando um novo item ao dicionário
programming_dictionary["Loop"] = "The action of doing something over and over again."

# criando um dicionário vazio
dicionario_vazio = {}

# Editando um item no dicionário

programming_dictionary["Bug"] = "A moth in your computer."

# percorrer um dicionário
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
