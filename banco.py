def exibir_menu():
    menu = """
================ BANCO PY ================

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==========================================

Escolha uma opção: """
    return input(menu)


def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Entrada inválida. Use apenas números.")
    return saldo, extrato


def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: R$ "))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print(f"Operação falhou! O saque não pode ultrapassar R$ {limite:.2f}.")
        elif numero_saques >= limite_saques:
            print("Operação falhou! Limite diário de saques atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")
    except ValueError:
        print("Entrada inválida. Use apenas números.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato.strip())
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================\n")



saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = exibir_menu()

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(
        saldo=saldo,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=LIMITE_SAQUES
            )

    elif opcao == "3":
        exibir_extrato(saldo, extrato)

    elif opcao == "4":
        print("Saindo... Obrigado por usar o Banco Py!")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção de 1 a 4.")


