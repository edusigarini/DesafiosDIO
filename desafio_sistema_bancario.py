def menu():
    menu = """
    ###### Desafio Sistema Bancario DIO ######

                Menu

                [1] - Extrato
                [2] - Depositar
                [3] - Sacar
                [4] - Criar Usuário
                [5] - Nova Conta                
                [6] - Lista de Contas
                [0] - Sair

    ------------------------------------------
    Selecione a sua opção: """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n--- Depósito efetuado com sucesso! ---")
    else:
        print("Operação falou! Valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n--- Operação falhou! Saldo suficiente. ---")

    elif excedeu_limite:
        print("\n--- Operação falhou! O valor do saque excede o limite. ---")

    elif excedeu_saques:
        print("\n--- Operação falhou! Número máximo de saques excedido. ---")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n--- Saque realizado com sucesso! ---")

    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):   
    print("\n------------------- EXTRATO -------------------")
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        extrato
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n-----------------------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Usuário já cadastrado com esse CPF! ---")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo (logradouro, Numero - Bairro - Cidade/UF): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("--- Cadastro realizado com sucesso! ---")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF cadastrado: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Conta cadastrada com sucesso! ---")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n--- Usuário não encontrado ---")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("-" * 100)
        print(linha)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "1":
            exibir_extrato(saldo, extrato = extrato)     

        elif opcao == "2":
            valor = float(input("Informe o valor do depósito: "))

        elif opcao == "3":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUE,
            )
        
        elif opcao == "4":
            criar_usuario(usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor seleciona novamente a operação desejada")

main()