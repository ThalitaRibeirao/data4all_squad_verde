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
        id_users = []
        for user in users:
            if(user[4]==True):
                id_users.append(user[0])
            
        id_user_excluir = int(input('Por favor, digite o ID do usuário que deseja excluir: '))
                
        while(id_user_excluir not in id_users):
            id_user_excluir = int(input('Usuário não encontrado!\nInsira o ID do usuário:'))                  
        for user in users:
            if(user[0] == id_user_excluir):
                user[4] = False
        print('Usuário excluído!')
    elif(opcao=='3'):
        pass
    elif(opcao=='4'):
        pass
    elif(opcao=='5'):
        print('\nUsuários cadastrados\n')
        for user in users:
            if(user[4] == True):
                print(f'ID: {user[0]}\nNome: {user[1]}\nTelefone: {user[2]}\nEndereço: {user[3]}\n\n')
    elif (opcao=='6'): break
    else:
        print("Digite uma opção válida!")

        
