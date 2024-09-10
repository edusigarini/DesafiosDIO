menu = """
###### Desafio Sistema Bancario DIO ######

                Menu

                [1] - Extrato
                [2] - Depositar
                [3] - Sacar
                [0] - Sair

------------------------------------------
Selecione a sua opção: """

saldo = 0
deposito = 0
extrato = ""
saque = 0
limite = 500
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\n------------------- EXTRATO -------------------")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            extrato
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n-----------------------------------------------")

    elif opcao == "2":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falou! Valor inválido.")

    elif opcao == "3":
        valor = float(input("Informe o valor do saque: "))
        sem_saldo = valor > saldo
        excedeu_limite = valor > limite
        limite_diario = saque >= LIMITE_SAQUE

        if sem_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("O valor do saque excedeu o limite!")
        elif limite_diario:
            print("Número de saques diários excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saque += 1

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor seleciona novamente a operação desejada")