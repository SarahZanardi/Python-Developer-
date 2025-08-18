"python"

letra = input("Digite uma letra: ")
if letra.isalpha():
    if letra.lower() in 'aeiou':
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")
else:
    print("Entrada inválida. Por favor, digite uma letra.")