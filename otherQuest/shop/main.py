class Main:
    pass

from cliente import Cliente
from conta import Conta




print('\n--- Login ---\n')

c1 = Cliente('caio', '123456caio')
conta = Conta(c1.nome, 6565, '')


c1_login = input('Digite seu nome\n=================\n')
c1_login2 = input('\nDigite a senha\n===============\n')

if(c1_login == 'caio' or c1_login == 'Caio'):
    if(c1_login2 == '123456caio'):
         print('\n***Login Bem-sucedido***\n')
    
         res = input('Deseja depositar, sacar ou acessar o extrato?\n')
    
         if(res == 'depositar' or res == 'Depositar'):
          valor =input('\nQuanto deseja depositar?\n==============\n')
          conta.deposita(valor)
          print('\n\n---- Depositamento realizado ----\n\n')

         elif(res == 'sacar' or res == 'Sacar'):
           valor = input('\nQuanto deseja sacar?\n')
           conta.saque(valor)

         elif(res == 'extrato' or res == 'Extrato'):
             conta.extrato()
   
    else:
       print('\nxxx Senha inválida xxx\n')

else:
   print('\nxx Nome de usuário inválido xx\n')

