nome = "Gustavo"
print(nome.upper()) #Deixando todas as letras maiúsculas
print(nome.lower()) #Deixando todas as letras minúsculas
print(nome.capitalize()) #Deixando a primeira letra maiúscula
print(nome.title()) #Deixando a primeira letra de cada palavra maiúscula
print(nome.count("o")) #Contando quantas vezes uma letra aparece

texto = "   Olá, Mundo!   "
print(texto.strip()) #Removendo espaços desnecessários
print(texto.lstrip())
print(texto.rstrip())   
print(texto.replace("Mundo", "Python")) #Substituindo palavras
print("-".join(["Python", "é", "legal"])) #Juntando strings com um separador
print("Python é legal".split()) #Dividindo uma string em uma lista
print("Python é legal".find("legal")) #Encontrando a posição de uma substring
print("Python é legal".startswith("Python")) #Verificando se começa com uma substring   