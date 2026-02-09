
import os
from colorama import Fore, init
import csv 

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar():
    input(f"{Fore.YELLOW}\n\nPressione o 'ENTER' para voltar...")


def menu_principal():
    while True:
        limpar_tela()
        print(f"{Fore.CYAN}================= IMOBILIÁRIA R.M - GERADOR DE ORÇAMENTO 🏠 =================")
        print(f"{Fore.YELLOW}Bem-Vindo a IMOBILIÁRIA R.M😊!!!")
        print(f"\n(1) - Apartamento: {Fore.GREEN}R$ 700.00 {Fore.YELLOW}('SEM Crianças residindo no imóvel ganha Desconto de 5%')")
        print(f"(2) - Casa: {Fore.GREEN}R$ 900.00")
        print(f"(3) - Estúdio: {Fore.GREEN}R$ 1200.00")
        print(f"{Fore.RED}(0) - Sair\n")
        opcao = input("Escolha uma opcão: ")

        if opcao == "1":
            menu_apartamento()
        elif opcao == "2":
            menu_Casa()
        elif opcao == "3":
            menu_estudio()
        elif opcao == "0":
            print(f"{Fore.RED}SAINDO...")
            break
        else:
            print(f"{Fore.RED}opção INVÁLIDA!...")
            voltar()
            menu_principal()
            





def menu_apartamento():
    limpar_tela()
    print(f"{Fore.CYAN}================= CONFIGURAÇÃO DO APARTAMENTO =================")
    print(f"Valor: {Fore.GREEN}R$ 700.00\n\n")

    valor_aluguel = 700.00
    qtd_quartos = ""
    tem_garagem = ""

    while qtd_quartos != 2 and qtd_quartos != 1:
        try:
            qtd_quartos = int(input("Deseja um apartamento de 1 ou 2 quartos?: "))
            if qtd_quartos == 2:
                valor_aluguel += 200.00
                print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
            elif qtd_quartos == 1:
                print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
            else:
                print(f"{Fore.RED}Opção INVÁLIDA! Digite apenas 1 ou 2.")
                voltar() 
                menu_apartamento()
        except ValueError:
            print(f"{Fore.RED}Opção INVÁLIDA! Digite apenas 1 ou 2.")
            voltar()
            menu_apartamento()

    while tem_garagem != "s" and tem_garagem != "n":
            tem_garagem = input("Deseja vaga de garagem? (S/N):").lower()
            if tem_garagem == "s":
                valor_aluguel += 300.00
                print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
            elif tem_garagem == "n":
                print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
            else:
                print(f"{Fore.RED}\nOpção INVÁLIDA! Digite apenas 'S' ou 'N'...")
                voltar()
                menu_apartamento()


    tem_criancas = input("Possui crianças residindo no imóvel? (S/N):").lower()
    if tem_criancas == "n":
        valor_aluguel *= 0.95 #desconto 5%
        print(f"{Fore.YELLOW}Desconto de 5% aplicado!")
        print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
    elif tem_criancas == "s":
        print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
    else:
        print(f"{Fore.RED}Opção não listada!")
        voltar()
        menu_apartamento()

    print(f"Valor aluguel total: {Fore.GREEN}R$ {valor_aluguel:.2f}\n")
    print(f"Contrato: {Fore.GREEN}R$ 2000.00")

    num_parcelas = 0
    while num_parcelas < 1 or num_parcelas > 5:
            try:
                num_parcelas = int(input("Em quantas vezes quer parcelar o contrato (1-5)?: "))
                if 1 <= num_parcelas <= 5:
                    valor_contrato = 2000.00 / num_parcelas
                else:
                    print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.")
                    voltar()
                    menu_apartamento()
            except ValueError:
                print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.")
                voltar()
                menu_apartamento()

    if tem_criancas == "n":
        print(f"\n\n{Fore.CYAN}================= ORÇAMENTO DO ALUGUEL💵 =================")
        print(f"""
Tipo do imóvel: APARTAMENTO
{Fore.YELLOW}Desconto de 5%!
{Fore.WHITE}Valor aluguel: {Fore.GREEN}R$ {valor_aluguel:.2f}
{Fore.WHITE}Valor do parcelamento do Contrato: {Fore.GREEN}x{num_parcelas} de R$ {valor_contrato:.2f}

{Fore.YELLOW}OBRIGADO POR UTILIZAR A IMOBILIÁRIA R.M😊!!!
""")
        
    else:
        print(f"\n\n{Fore.CYAN}================= ORÇAMENTO DO ALUGUEL💵  =================")
        print(f"""
Tipo do imóvel: APARTAMENTO
{Fore.YELLOW}SEM Desconto
{Fore.WHITE}Valor aluguel: {Fore.GREEN}{valor_aluguel:.2f}
{Fore.WHITE}Valor do parcelamento do Contrato: {Fore.GREEN}x{num_parcelas} de R$ {valor_contrato:.2f}

{Fore.YELLOW}OBRIGADO POR UTILIZAR A IMOBILIÁRIA R.M😊!!!
""")
    
    voltar()
    menu_principal()











def menu_Casa():
    limpar_tela()
    print(f"{Fore.CYAN}================= CONFIGURAÇÃO DA CASA =================")
    print(f"Valor: {Fore.GREEN} R$ 900,00\n\n")
    voltar()










def menu_estudio():
    limpar_tela()
    print(f"{Fore.CYAN}================= CONFIGURAÇÃO DO ESTÚDIO =================")
    print(f"Valor: {Fore.GREEN}R$ 1200,00\n\n")
    voltar()





menu_principal()
