''''Objetivo: Realizar o backlog do sistema, definindo as atividades com maior prioridade, e criar as sprints correspondentes. 
Desenvolver o algoritmo em Python e subir todas as alterações no GitHub. 

Tarefas: 
Cadastro de Usuário: 
Permitir que novos usuários se cadastrem no sistema fornecendo informações como nome, e-mail e senha. 

Login de Usuário: 
Autenticar usuários cadastrados para acessar o sistema. 

Catálogo de Produtos: 
Exibir uma lista de produtos disponíveis para compra, incluindo nome do produto, preço e descrição. 

Adicionar Produtos ao Carrinho: 
Permitir que os usuários adicionem produtos ao carrinho de compras. 

Remover Produtos do Carrinho: 
Fornecer uma opção para remover produtos do carrinho de compras. 

Visualização de Carrinho: 
Mostrar ao usuário os produtos atualmente no carrinho de compras, incluindo o valor total. 

Processo de Compra: 
Peritir que o usuário finalize a compra dos itens no carrinho, inserindo informações de pagamento. 

Histórico de Compras: 
Manter um registro das compras anteriores do usuário para consulta futura. 

Administração de Estoque: 
Permitir que administradores atualizem a quantidade de produtos no estoque. 
Permitir que administradores adicionem novos produtos ao estoque. 
'''

# Dados iniciais
usuarios = [{"nome": "Admin", "email": "admin", "senha": "admin", "historico_compras": []}]
produtos = [
    {"id": 1, "nome": "Maçã", "preco": 0.50, "quantidade": 100},
    {"id": 2, "nome": "Banana", "preco": 0.30, "quantidade": 100},
    {"id": 3, "nome": "Leite", "preco": 2.50, "quantidade": 100},
    {"id": 4, "nome": "Pão", "preco": 1.20, "quantidade": 100}
]
carrinho = []

# Funções
def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    for usuario in usuarios:
        if usuario['email'] == email:
            print("Este e-mail já está cadastrado.")
            return
    usuarios.append({"nome": nome, "email": email, "senha": senha, "historico_compras": []})
    print("Cadastro realizado com sucesso!")

def fazer_login():
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            print(f"Bem-vindo, {usuario['nome']}!")
            return usuario
    print("E-mail ou senha incorretos.")
    return None

def exibir_produtos():
    print("\nProdutos Disponíveis:")
    for produto in produtos:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def adicionar_ao_carrinho():
    exibir_produtos()
    produto_id = int(input("Digite o ID do produto que deseja adicionar ao carrinho: "))
    quantidade = int(input("Digite a quantidade: "))
    
    for produto in produtos:
        if produto["id"] == produto_id:
            if produto["quantidade"] >= quantidade:
                carrinho.append({"nome": produto["nome"], "preco": produto["preco"], "quantidade": quantidade})
                produto["quantidade"] -= quantidade
                print(f"{quantidade} x {produto['nome']} adicionado(s) ao carrinho.")
            else:
                print("Quantidade insuficiente no estoque.")
            return
    print("Produto não encontrado.")

def remover_do_carrinho():
    visualizar_carrinho()
    produto_nome = input("Digite o nome do produto que deseja remover do carrinho: ")

    for item in carrinho:
        if item["nome"] == produto_nome:
            carrinho.remove(item)
            for produto in produtos:
                if produto["nome"] == produto_nome:
                    produto["quantidade"] += item["quantidade"]
                    print(f"{item['quantidade']} x {produto_nome} removido(s) do carrinho.")
            return
    print("Produto não encontrado no carrinho.")

def visualizar_carrinho():
    if not carrinho:
        print("Seu carrinho está vazio.")
        return
    print("\nItens no Carrinho:")
    total = sum(item['preco'] * item['quantidade'] for item in carrinho)
    for item in carrinho:
        print(f"{item['quantidade']} x {item['nome']} - R${item['preco'] * item['quantidade']:.2f}")
    print(f"Total: R${total:.2f}")

def finalizar_compra(usuario):
    if not carrinho:
        print("Seu carrinho está vazio.")
        return
    visualizar_carrinho()
    if input("Deseja finalizar a compra? (s/n): ").lower() == 's':
        print("Métodos de Pagamento:\n1. Dinheiro\n2. PIX\n3. Cartão de Débito\n4. Cartão de Crédito")
        metodo_pagamento = input("Escolha o método de pagamento: ")
        metodos = {
            "1": "Dinheiro",
            "2": "PIX",
            "3": "Cartão de Débito",
            "4": "Cartão de Crédito"
        }
        if metodo_pagamento in metodos:
            total = sum(item['preco'] * item['quantidade'] for item in carrinho)
            usuario['historico_compras'].append({
                "itens": carrinho.copy(),
                "metodo_pagamento": metodos[metodo_pagamento],
                "total": total
            })
            print(f"Compra finalizada com sucesso! Total a pagar: R${total:.2f} via {metodos[metodo_pagamento]}")
            carrinho.clear()
        else:
            print("Método de pagamento inválido.")
    else:
        print("Compra não finalizada.")

def atualizar_produto():
    exibir_produtos()
    produto_id = int(input("Digite o ID do produto que deseja atualizar: "))
    nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
    novo_preco = float(input("Digite o novo preço: "))

    for produto in produtos:
        if produto["id"] == produto_id:
            produto.update({"quantidade": nova_quantidade, "preco": novo_preco})
            print(f"Produto {produto['nome']} atualizado.")
            return
    print("Produto não encontrado.")

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    novo_id = max(produto["id"] for produto in produtos) + 1 if produtos else 1
    produtos.append({"id": novo_id, "nome": nome, "preco": preco, "quantidade": quantidade})
    print("Produto adicionado com sucesso!")

def menu_administrador():
    while True:
        opcao = input("\nMenu do Administrador\n1. Atualizar produtos\n2. Adicionar produto\n3. Voltar\nEscolha uma opção: ")
        if opcao == "1":
            atualizar_produto()
        elif opcao == "2":
            adicionar_produto()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_usuario(usuario):
    while True:
        opcao = input("\nMenu do Usuário\n1. Visualizar produtos\n2. Adicionar ao carrinho\n3. Remover do carrinho\n4. Visualizar carrinho\n5. Finalizar compra\n6. Histórico de compras\n7. Sair\nEscolha uma opção: ")
        if opcao == "1":
            exibir_produtos()
        elif opcao == "2":
            adicionar_ao_carrinho()
        elif opcao == "3":
            remover_do_carrinho()
        elif opcao == "4":
            visualizar_carrinho()
        elif opcao == "5":
            finalizar_compra(usuario)
        elif opcao == "6":
            visualizar_historico(usuario)
        elif opcao == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

def visualizar_historico(usuario):
    if not usuario['historico_compras']:
        print("Você não tem histórico de compras.")
        return
    print("\nHistórico de Compras:")
    for i, compra in enumerate(usuario['historico_compras'], 1):
        print(f"Compra {i}:")
        total = compra['total']
        for item in compra['itens']:
            print(f"  {item['quantidade']} x {item['nome']} - R${item['preco'] * item['quantidade']:.2f}")
        print(f"  Total: R${total:.2f}")
        print(f"  Método de Pagamento: {compra['metodo_pagamento']}")

def menu_principal():
    while True:
        opcao = input("\nMenu Principal\n1. Cadastro\n2. Login\n3. Sair\nEscolha uma opção: ")
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = fazer_login()
            if usuario:
                if usuario["email"] == "admin":
                    menu_administrador()
                else:
                    menu_usuario(usuario)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
