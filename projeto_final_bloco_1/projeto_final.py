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

         new_user_nome = str(input('Insira o nome do usuário: '))
         z = procura_no_sistema(new_user_nome, 1)

         if z == True:
           while z == True:
             new_user_nome = str(input('Usuário já cadastrado no sistema, tente novamente: '))
             z = procura_no_sistema(new_user_nome, 1)
    
         else:
           pass

         new_user_telefone = int(input('Insira o telefone do usuário: '))
         z = procura_no_sistema(new_user_telefone, 2)

         if z == True:
           while z == True:
             new_user_telefone = int(input('telefone já cadastrado no sistema, tente novamente: '))
             z = procura_no_sistema(new_user_telefone, 2)
    
         else:
           pass

         new_user_endereco = str(input('Insira o endereço do usuário: '))

         #ID para o novo usuario
         new_user_id0 = 0
         for i in users:
           if new_user_id0 <= i[0]:
             new_user_id0 = i[0]
           else:
             pass
         new_user_id = new_user_id0 + 1
         
         #Adicionando novo usuário em users 
         new_user_full = [new_user_id, new_user_nome, new_user_telefone, new_user_endereco, True]
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

        