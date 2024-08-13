def coletar_dados_produtos():
    # Cria um dicionário vazio para armazenar os produtos e seus preços
    produtos = {}

    # Loop para coletar dados dos cinco produtos
    for i in range(5):
        # Solicita ao usuário o nome do produto
        nome_produto = input(f"Digite o nome do produto {i + 1}: ")
        
        # Solicita ao usuário o preço do produto
        # Usando float para permitir preços com decimais
        preco_produto = float(input(f"Digite o preço do produto {i + 1} (em reais): "))
        
        # Armazena o produto e o preço no dicionário
        produtos[nome_produto] = preco_produto
    
    return produtos

def calcular_valor_total(produtos):
    # Calcula o valor total somando todos os preços no dicionário
    valor_total = sum(produtos.values())
    return valor_total

def exibir_valor_total(valor_total):
    # Exibe o valor total da compra
    print(f"\nO valor total da compra é: R$ {valor_total:.2f}")

# Coleta os dados dos produtos
produtos = coletar_dados_produtos()

# Calcula o valor total da compra
valor_total = calcular_valor_total(produtos)

# Exibe o valor total da compra
exibir_valor_total(valor_total)
