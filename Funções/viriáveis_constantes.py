# 💳 Simulação simples de cadastro e operação bancária

# Dados do usuário
nome = "Rebeca"
idade = 24

# Informações bancárias
limite_saque_diario = 1000
valor_sacado = 1000

# Exibição dos dados
print("🧾 Cadastro do Cliente")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")

print("\n🏦 Operação Bancária")
print(f"Limite de saque diário: R$ {limite_saque_diario}")
print(f"Valor sacado hoje: R$ {valor_sacado}")

# Verificando se o saque está dentro do limite
if valor_sacado <= limite_saque_diario:
    print("\n✅ Saque realizado com sucesso!")
else:
    print("\n⚠️ Valor excede o limite de saque diário.")