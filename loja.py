from models.produto import Produto
from utils.helper import formata_float_moeda
from time import sleep
from typing import List, Dict


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []



def menu() -> None:
    print("=====================================")
    print("========== Bem-vindo(a) ============")
    print("=============== ao =================")
    print("========== SportsCenter =============")
    print("=====================================")

    print("Selecione uma opção no menu abaixo:")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Visualizar carrinho")
    print("5 - Fechar pedido")
    print("6 - Sair do programa")

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produtos()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Fechando o programa...\nVolte sempre!")
        sleep(2)
        exit()
    else:
        print("Opção inválida! Tente Novamente.")
        sleep(2)


def cadastrar_produtos() -> None:
    print("Cadastro de Produto: \n")

    nome: str = input("Digite o nome do produto: ")
    preco: float = float(input("Digite o preço do produto: "))
    estoque: int = int(input("Digite a quantidade do produto: "))

    produto = Produto(nome, preco, estoque)
    produtos.append(produto)

    print(f"\nO produto {produto.nome} foi cadastrado com sucesso!\n")
    sleep(2)


def listar_produtos() -> None:
    if len(produtos) == 0:
        print("Ainda não há produtos cadastrados.\n")
        sleep(2)
    else:
        print("Listagem de Produtos: \n")
        for produto in produtos:
            print(produto)
            sleep(1)
            print("-----------------------------------\n")
        sleep(2)


def comprar_produto() -> None:
    if len(produtos) == 0:
        print("Ainda não há produtos cadastrados.\n")
        sleep(2)
    else:
        print("======== Produtos Disponíveis ========\n")
        for produto in produtos:
            print(produto)
            print("-----------------------------------\n")
            print("Digite o código do produto que deseja comprar: ")
        
        codigo: int = int(input())
        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            quantidade: int = int(input(f"Digite a quantidade de {produto.nome} que deseja comprar: "))
            if produto.estoque < quantidade:
                print(f"\nO produto {produto.nome} está sem estoque suficiente no momento.\n")
                sleep(2)
            else:
                carrinho.append({produto: quantidade})
                atualizar_estoque(produto, quantidade)
                print(f"\n{quantidade} unidade(s) de {produto.nome} adicionada(s) ao carrinho com sucesso!\n")
                sleep(2)
        else:
            print("Produto não encontrado. Tente novamente.\n")
            sleep(2)


def visualizar_carrinho() -> None:
    if carrinho:
        print("Produtos no carrinho: \n")
        for item in carrinho:
            for prod in item.items():
                print(f"{prod[0].nome} - {prod[0].preco}")
                print(f"quantidade: {prod[1]}")
                print("-----------------------------------\n")
        sleep(2)
    else:
        print("Seu carrinho está vazio.\n")
        sleep(2)


def fechar_pedido() -> None:
    if len(carrinho) == 0:
        print("Seu carrinho está vazio. Adicione produtos antes de fechar o pedido.\n")
        sleep(2)
    else:
        print("Produtos no carrinho: \n")
        valor_total: float = 0.0
        for item in carrinho:
            for prod in item.items():
                print(f"{prod[0].nome} - {prod[0].preco}")
                print("quantidade: ", prod[1])
                valor_total += prod[0].preco * prod[1]
                print("-----------------------------------\n")
        print("\n")
        sleep(2)
        print(f"Valor total do pedido: {formata_float_moeda(valor_total)}\n")
        print("Obrigado pela preferência! Volte sempre.\n")
        carrinho.clear()
        sleep(5)

def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    
    return p

def atualizar_estoque(produto: Produto, quantidade: int) -> None:
    produto.estoque -= quantidade


if __name__ == "__main__":
    while True:
        menu()