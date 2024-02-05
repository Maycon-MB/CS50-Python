# main.py
from conversor import Conversor

def main():
    print("Bem-vindo ao Conversor de Arquivos!")

    # Instanciando o objeto Conversor
    conversor = Conversor()

    # Menu de opções
    while True:
        print("\nSelecione uma opção:")
        print("1. Converter PDF para CSV")
        print("2. Converter CSV para PDF")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            pdf_arquivo = input("Digite o nome do arquivo PDF a ser convertido: ")
            csv_arquivo = input("Digite o nome do arquivo CSV de saída: ")
            conversor.converter_pdf_para_csv(pdf_arquivo, csv_arquivo)
        elif opcao == "2":
            csv_arquivo = input("Digite o nome do arquivo CSV a ser convertido: ")
            pdf_arquivo = input("Digite o nome do arquivo PDF de saída: ")
            conversor.converter_csv_para_pdf(csv_arquivo, pdf_arquivo)
        elif opcao == "3":
            print("Obrigado por usar o Conversor de Arquivos! Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
