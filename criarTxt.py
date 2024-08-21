def criar_arquivos(nome_arquivo, conteudo):
  try:
      
    with open(nome_arquivo, 'w') as arquivo:
      arquivo.write(conteudo)
      print('o arquivo foi criado \n')

      
  except Exception as e:
    print('erro ao criar o arquivo \n')

nome = input('digite o nome do arquivo: ')
criar_arquivos(nome+'.txt', input('digite o conteúdo do arquivo: '))

dados = open(nome+'.txt', 'r')
conteudo = dados.read()

print('o nome do arquivo é: ', nome)
print('e o conteúdo é:', conteudo, ', consulte-o no Gerenciador de Arquivos \n')
input("Pressione ENTER para encerrar")
dados.close()
