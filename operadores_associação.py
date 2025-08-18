frutas = ('maçã', 'banana', 'laranja')
print('maçã' in frutas)  # True, 'maçã' está na tupla frutas
print('uva' not in frutas)  # True, 'uva' não está na tupla frutas
print('banana' in frutas)  # True, 'banana' está na tupla frutas
print('pera' not in frutas)  # True, 'pera' não está na tupla frutas
print('laranja' in frutas)  # True, 'laranja' está na tupla frutas
print('abacaxi' not in frutas)  # True, 'abacaxi'   não está na tupla frutas
# operadores de identidade
a = [1, 2, 3]
b = a
c = [1, 2, 3]   
print(a is b)  # True, a e b referenciam o mesmo objeto
print(a is not c)  # True, a e c referenciam objetos diferentes
print(b is a)  # True, b e a referenciam o mesmo objeto
print(c is not b)  # True, c e b referenciam objetos diferentes
print(a is c)  # False, a e c referenciam objetos diferentes
print(c is not a)  # True, c e a referenciam objetos diferentes