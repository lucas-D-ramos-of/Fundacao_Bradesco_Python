class Main:
    pass

print("Hello Wolrd: Lucas")

from Cliente import Cliente
from Conta import Conta

cl1 = Cliente("Lucas", "13")
conta = Conta(cl1._nome, 3982, 0)

print(cl1)

print(cl1._nome, "e", cl1._telefone)

print(conta.titular, "Numero:", conta.numero, "Seu Saldo:", conta.saldo)

conta.deposita(100)
conta.saque(50)
conta.extrato()