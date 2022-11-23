saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_MAX = 500

menu = """
==== MENU ====
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>
"""

while True:
    opcao = input(menu)

    if opcao == "d":
        print("==== DEPÓSITO ====")

        try:
            deposito = float(input("Valor a ser depositado: "))
            saldo += deposito
            print(f"Depósito de R${deposito} realizado com sucesso")
            extrato += (f"Depósito de R${deposito} \n")
        except ValueError:
            print("Digite um valor válido!")

    if opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print(
                f"Quatidade de saques excede o limite diário permitido de {LIMITE_SAQUES}")
            continue
        print("==== SAQUE ====")
        print(f"Saldo atual R${saldo}")
        try:
            saque = float(input("Valor a ser sacado: "))
            if float(saque) > float(LIMITE_MAX):
                print(f"Valor excede o limite permitido de R${LIMITE_MAX}")
            elif float(saque) > float(saldo):
                print(f"Valor excede o saldo de {saldo}")
            else:
                print(f"Saque no valor de R${saque} efetuado com sucesso")
                saldo -= saque
                numero_saques += 1

                extrato += (f"Saque de R${saque} \n")

        except ValueError:
            print("Digite um valor válido!")

    if opcao == "e":
        print("==== EXTRATO ====")
        print(extrato)
        print(f"Saldo atual: R${saldo}")

    if opcao == "q":
        print("==== ENCERRADO ====")
        break
