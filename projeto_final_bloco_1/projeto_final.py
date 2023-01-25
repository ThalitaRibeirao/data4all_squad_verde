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
    [1,"Ciclano Sauro",'2345678',"Rua Boa",True],
    [2,"Fulano Silva",'3478358235',"Rua Top",True],
    [3,"John Doe",'3853385267',"MAIOBÃO",True],
    [4, "Aline Carvalho", '32988427689', "Rua Roberto Thomazeli", True],
    [5, "Felipe Cunha", '81998057401', "Rua General Polidoro", True],
    [6, "Eduardo Vitor", '12988723166', "Rua Maria Pereira", True],
    [7, "Thalita Silva", '11937523634', "Rua Domingos Maciel", True]
]


while(True): 
    print(menu)
    opcao = input('> ')
    
    if(opcao=='1'):
         #Busca de dados x iguais em y id (0), nome(1), telefone(2)...
         def procura_no_sistema(x, y):
           for i in users:
             if x == i[y]:
               z = True
               break
             else:
               z = False
           return z

         #Inserindo as informações do novo usuário

         while True:
            new_user_nome = input('Insira o nome do usuário: ')
            if not procura_no_sistema(new_user_nome, 1): break  
            else: print('Usuário já cadastrado.\n ')
    
         while True:
            new_user_telefone = input('Insira o telefone do usuário: ')
            if not procura_no_sistema(new_user_telefone, 2): 
                if not new_user_telefone.isnumeric():
                    print('Telefone Inválido.')
                else: break
            else: print('Telefone já cadastrado.\n')

         new_user_endereco = input('Insira o endereço do usuário: ')
       
         #Adicionando novo usuário em users 
         new_user_full = [len(users)+1, new_user_nome, new_user_telefone, new_user_endereco, True]
         users.append(new_user_full)
         
    elif(opcao=='2'):
        pass
    elif(opcao=='3'):
        pass
    elif(opcao=='4'):
        pass
    elif(opcao=='5'):
        pass
    elif (opcao=='6'): break
    else:
        print("Digite uma opção válida!")

        