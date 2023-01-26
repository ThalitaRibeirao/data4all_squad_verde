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
    [1,'Ciclano Sauro',2345678,'Rua Boa',True],
    [2,'Fulano Silva',3478358235,'Rua Top',True],
    [3,'John Doe',3853385267,'MAIOBÃO',True],
    [4, 'Aline Carvalho', 32988427689, 'Rua Roberto Thomazeli', True],
    [5, 'Felipe Cunha', 81998057401, 'Rua General Polidoro', True],
    [6, 'Eduardo Vitor', 12988723166, 'Rua Maria Pereira', True],
    [7, 'Thalita Silva', 11937523634, 'Rua Domingos Maciel', True]
]


while(True): 
    print(menu)
    opcao = input('')
    
    if(opcao=='1'):
        pass
    elif(opcao=='2'):
        pass
    elif(opcao=='3'):
        # Recebendo o ID do Usuário
        while(True):
            user_id = input('Insira o ID do Usuário: ')
            if(not user_id.isnumeric()): print("Insira um ID válido!")
            else: 
                user_id = int(user_id)
                if(user_id < 1 or user_id > len(users)): print("Insira um ID válido!")
                elif(not users[user_id-1][4]): print("Usuário não encontrado!\n")
                else: break
    
        
        
        # Alterando as informacoes
        opcao = input(sub_menu)
        if(opcao == '1'):
            while True:
                new_user_nome= input('Insira o nome: ')
                if not procura_no_sistema(new_user_nome, 1):
                    users[i][1] = new_user_nome  
                    break
                else: print('Usuário já cadastrado.\n ')
        elif(opcao == '2'):
            while True:
                new_user_telefone = input('Insira o telefone: ')
                if not procura_no_sistema(new_user_telefone, 2): 
                    if not new_user_telefone.isnumeric():
                        print('Telefone Inválido.')
                    else: 
                        users[i][2] = new_user_telefone        
                else: print('Telefone já cadastrado.\n')
            
        elif(opcao == '3'):
            users[i][3] = input('Insira o endereço: ')
        else: 
            print('Digite uma opção válida!')
    
    elif(opcao=='4'):
        pass
    elif(opcao=='5'):
        pass
    elif (opcao=='6'): break
    else:
        print('Digite uma opção válida!')

        