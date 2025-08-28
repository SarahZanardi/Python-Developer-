numeros  = {1, 2, 3, 4, 5}
print(numeros)
numeros.add(6)
print(numeros)
numeros.remove(3)
print(numeros)
print(3 in numeros) # Verifica se o 3 está no conjunto
print(len(numeros)) # Tamanho do conjunto           
numeros.clear() # Limpa o conjunto
print(numeros)  # Conjunto vazio
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
uniao = conjunto_a.union(conjunto_b)
print("União:", uniao) # {1, 2, 3, 4, 5}
intersecao = conjunto_a.intersection(conjunto_b)
print("Interseção:", intersecao) # {3}