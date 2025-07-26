menu = """  

  [S] sacar
  [D] depositar
  [E] extrato
  [Q] sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().upper()

    if opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Saldo Insuficiente!")
        elif valor > limite:
            print("Valor acima do limite!")
        elif numero_saques > LIMITE_SAQUES:
            print("Numero máximo de saques excedido!")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

    elif opcao == "D":
        valor = float(input("Informe o valor do Depósito:"))
        if valor <= 0:
            print("Valor inválido para depósito!")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

    elif opcao == "E":
        print("Extrato: ")
        print("Não foram realizadas movimentações." if not extrato else extrato) 
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "Q":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")