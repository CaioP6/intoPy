from cliente import Cliente

class Conta:
    def __init__(self, titular, numero, saldo):
        
        self.titular = titular
        self.numero = numero 
        self.saldo = float(100)
    

    def deposita(self, valor):
        self.saldo += valor
        print('Valor depositado com sucesso: ', valor)


    def saque(self, valor):
        
        if(self.saldo > valor):
            self.saldo -= valor
            print('Saque realizado com Sucesso: ', valor)
        else:
            print('Saldo insuficiente')
        

    def extrato(self):
        print('Cliente: ', self.titular, '\nSaldo Atual: ', self.saldo)


    




