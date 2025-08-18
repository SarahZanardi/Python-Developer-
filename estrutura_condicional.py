maior_idade = 18
def verificar_idade(idade):
    if idade < maior_idade:
        return "Você é menor de idade."
    else:
        return "Você é maior de idade."
    print(verificar_idade(20))  # Deve retornar "Você é maior de idade."
    if __name__ == "__main__":
        print(verificar_idade(16))  
# Deve retornar "Você é menor de idade."
        print(verificar_idade(18))  # Deve retornar "Você é maior de idade."