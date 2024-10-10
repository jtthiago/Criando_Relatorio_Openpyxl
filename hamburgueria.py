import openpyxl

class Hamburgueria:
    def __init__(self):
        self.produtos = []

    
    def cadastrar_produto(self, nome, categoria, preco):
        produto = {
            'Nome': nome,
            'Categoria': categoria,
            'Preço': preco
        }
        self.produtos.append(produto)
        print(f"Produto '{nome}' cadastrado  com sucesso")

    

    def gerar_relatorio(self, nome_arquivo):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = "Relatório de Produtos"



        #Adiciona cabeçalhos
        worksheet['A1'] = "Nome"
        worksheet['B1'] = "Categoria"
        worksheet['C1'] = "Preço"


        # Adicionar produtos na planilha
        for index, produto in enumerate(self.produtos, start=2):
            worksheet[f'A{index}'] = produto['Nome']
            worksheet[f'B{index}'] = produto['Categoria']
            worksheet[f'C{index}'] = produto['Preço']


            #Salva a planilha
            workbook.save(nome_arquivo)
            print(f"Relatório gerado com sucesso em '{nome_arquivo}'!")

        
def main():
    hamburgueria = Hamburgueria()

    while True:
        print("\n----- Menu de Cadastro de Produtos -----")
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto (Ex: Hambúrguer, Bebida, Acompanhamento): ")
        preco = float(input("Digite o preço do produto: R$ "))
        
        hamburgueria.cadastrar_produto(nome, categoria, preco)

        opcao = input("Deseja cadastrar outro produto? (s/n): ")
        if opcao.lower() != 's':
            break

    # Gera o relatório
    hamburgueria.gerar_relatorio("relatorio_hamburgueria.xlsx")

if __name__ == "__main__":
    main()