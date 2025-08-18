saldo = 1000

saque = 200 

limite = 500    

conta_especial = True 

print(True if saldo >= saque else False)

pode_sacar = (saldo >= saque) and (saque <= limite or conta_especial)  
print(pode_sacar)