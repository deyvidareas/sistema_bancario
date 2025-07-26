def deposit(saldo, valor, extrato):
    if valor <= 0:
        return saldo, extrato, "Valor inválido para depósito!"
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato, "Depósito realizado com sucesso!"

def withdraw(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        return saldo, extrato, "Saldo Insuficiente!"
    elif valor > limite:
        return saldo, extrato, "Valor acima do limite!"
    elif numero_saques >= LIMITE_SAQUES:
        return saldo, extrato, "Número máximo de saques excedido!"
    
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    return saldo, extrato, "Saque realizado com sucesso!"

def get_statement(extrato, saldo):
    return extrato if extrato else "Não foram realizadas movimentações.", saldo

# Initial values
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Example usage
# saldo, extrato, message = deposit(saldo, 100, extrato)
# saldo, extrato, message = withdraw(saldo, 50, extrato, limite, numero_saques, LIMITE_SAQUES)
# statement, saldo = get_statement(extrato, saldo)