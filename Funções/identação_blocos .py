def sacar (valor, saldo):
    if valor <= 0:
        return "Valor inválido. O valor deve ser maior que zero."
    if valor > saldo:
        return "Saldo insuficiente para realizar o saque."
    return saldo - valor 
sacar(100, 500)  # Exemplo de uso da função 
print(sacar(100, 500))  # Deve retornar 400