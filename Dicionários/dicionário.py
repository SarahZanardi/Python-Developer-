dicionário ={"nome":"Sara","idade":21,"cidade":"São Paulo"}
print(dicionário)
print(dicionário["nome"])
print(dicionário["idade"])
print(dicionário["cidade"])
dicionário["idade"] = 22
print(dicionário)
dicionário["profissão"] = "Desenvolvedora"
print(dicionário)
del dicionário["cidade"]
print(dicionário)