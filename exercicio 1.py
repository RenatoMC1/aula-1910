contador = 0
Lista = []
pergunta1 = input("Olá, seja bem vindo! O que você deseja fazer?\n[1] Cadastrar usuário\n[2] Visualizar cadastro\n[3] Atualizar cadastro\n[4] Deletar usuário\n[5] Sair\n")

while True:
    nome = input(f"Digite o nome do usuário: ")
    Lista.append(nome)
    pergunta2 = int(input("Deseja continuar cadastrando novos usuários?\n[1] Sim\n[2] Nao\n"))

    if pergunta2 == 1:
        contador = contador + 1
    elif pergunta2 == 2:
        pergunta3 = int(input("Então, o que você deseja fazer?\n[1] Visualizar cadastro\n[2] Atualizar cadastro\n[3] Deletar usuário\n"))
        if pergunta3 == 1:
            print(f"Os usuários cadastrados são: {Lista}")
            break
        elif pergunta3 == 2:
            print(f"Então,qual usuário você deseja atualizar?\n{Lista}")
            resposta = input("Digite usuário da lista: ")
            indice = Lista.index(resposta)


            Lista[indice] = resposta
            print(Lista)











