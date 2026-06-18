def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print ("Saldo {}".format(conta["saldo"]))


minha_conta = cria_conta(123, "Lucas", 100.0, 1000.0)

deposita(minha_conta, 50.0)
extrato(minha_conta)

saca(minha_conta, 20.00)
extrato(minha_conta)