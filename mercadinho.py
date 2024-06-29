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
import json
lista = []

def leitura():
    
    with open('banco_de_dados.json', 'r') as file:
        x = json.load(file)
    return x
        
   
    


def add():
    Nome = input("Digite um nome: ")
    Senha = input("Digite a senha: ")

    lista.append({"Nome": Nome, "Senha": Senha})

    with open('banco_de_dados.json', 'w') as file:
        json.dump(lista, file)

    
    

print(leitura)
add()
print(leitura)

