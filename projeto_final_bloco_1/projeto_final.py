def info_users():
  while True:
    id = int(input('Digite o ID do usuário: '))
    found_user = None
    for user in users:
      if user[0] == id:
        found_user = user
        break
    if found_user == None:
      print('Usuário não encontrado.')
    else:
      print('')
      print(f'Nome: {found_user[1]}')
      print(f'Telefone: {found_user[2]}')  
      print(f'Endereço: {found_user[3]}')
      break     


menu = '''
\nBoas vindas ao nosso sistema:

1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair\n
'''

sub_menu = '''
\nQual informação deseja alterar?
1 - Nome
2 - Tefone
3 - Endereço\n
'''

users = [
    [1,"Ciclano Sauro",2345678,"Rua Boa",True],
    [2,"Fulano Silva",3478358235,"Rua Top",True],
    [3,"John Doe",3853385267,"MAIOBÃO",True],
    [4, "Aline Carvalho", 32988427689, "Rua Roberto Thomazeli", True],
    [5, "Felipe Cunha", 81998057401, "Rua General Polidoro", True],
    [6, "Eduardo Vitor", 12988723166, "Rua Maria Pereira", True],
    [7, "Thalita Silva", 11937523634, "Rua Domingos Maciel", True]
]


while(True): 
    print(menu)
    opcao = input('> ')
    
    if(opcao=='1'):
        pass
    elif(opcao=='2'):
        pass
    elif(opcao=='3'):
        pass
    elif(opcao=='4'):
        info_users()
    elif(opcao=='5'):
        pass
    elif (opcao=='6'): break
    else:
        print("Digite uma opção válida!")
        