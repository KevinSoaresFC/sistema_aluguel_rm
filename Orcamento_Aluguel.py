
import os
from colorama import Fore, init
from calculos_csv import orcamento_csv

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





def menu_apartamento():
    limpar_tela()
    print(f"{Fore.CYAN}================= CONFIGURAÇÃO DO APARTAMENTO =================")
    print(f"Valor: {Fore.GREEN}R$ 700.00\n\n")

    valor_aluguel = 700.00
    qtd_quartos = 0
    tem_garagem = ""
    tem_criancas = ""
    num_parcelas = 0
    arquivo_csv = ""

    while qtd_quartos != 2 and qtd_quartos != 1:
        try:
            qtd_quartos = int(input("Deseja um apartamento de 1 ou 2 quartos?: "))
            if qtd_quartos == 2:
                valor_aluguel += 200.00
                print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
            elif qtd_quartos == 1:
                qtd_quartos = 1
                print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
            else:
                print(f"{Fore.RED}Opção INVÁLIDA! Digite apenas 1 ou 2.", end="", flush=True)
                voltar()
                print("\033[F\033[K" * 4, end="", flush=True)
        except ValueError:
            print(f"{Fore.RED}Opção INVÁLIDA! Digite apenas 1 ou 2.",end="", flush=True)
            voltar()
            print("\033[F\033[K" * 4, end="", flush=True)
            
            
            

    while tem_garagem != "s" and tem_garagem != "n":
            tem_garagem = input("Deseja vaga de garagem? (S/N):").lower()
            if tem_garagem == "s":
                valor_aluguel += 300.00
                print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
            elif tem_garagem == "n":
                print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
            else:
                print(f"{Fore.RED}\nOpção INVÁLIDA! Digite apenas 'S' ou 'N'...", end="", flush=True)
                voltar()
                print("\033[F\033[K" * 5, end="", flush=True)

    while tem_criancas !="n" and tem_criancas !="s":
        tem_criancas = input("Possui crianças residindo no imóvel? (S/N):").lower()
        if tem_criancas == "n":
            valor_aluguel *= 0.95 #desconto 5%
            print(f"{Fore.YELLOW}Desconto de 5% aplicado!")
            print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
        elif tem_criancas == "s":
            print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
        else:
            print(f"{Fore.RED}Opção não listada!", end="", flush=True)
            voltar()
            print("\033[F\033[K" * 4, end="", flush=True)

    print(f"Valor aluguel total: {Fore.GREEN}R$ {valor_aluguel:.2f}\n")
    print(f"Contrato: {Fore.GREEN}R$ 2000.00")

    while num_parcelas < 1 or num_parcelas > 5:
            try:
                num_parcelas = int(input("Em quantas vezes quer parcelar o contrato (1-5)?: "))
                if 1 <= num_parcelas <= 5:
                    valor_contrato = 2000.00 / num_parcelas
                else:
                    print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.", end="", flush=True)
                    voltar()
                    print("\033[F\033[K" * 4, end="", flush=True)
            except ValueError:
                print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.", end="", flush=True)
                voltar()
                print("\033[F\033[K" * 4, end="", flush=True)

    if tem_criancas == "n":
            limpar_tela()
            print(f"\n\n{Fore.CYAN}================= ORÇAMENTO DO ALUGUEL💵 =================")
            print(f"""
    Tipo do imóvel: APARTAMENTO
    {Fore.YELLOW}Desconto de 5%!
    {Fore.WHITE}Valor aluguel: {Fore.GREEN}R$ {valor_aluguel:.2f}
    {Fore.WHITE}Valor do parcelamento do Contrato: {Fore.GREEN}x{num_parcelas} de R$ {valor_contrato:.2f}
    """)

    else:
            limpar_tela()
            print(f"\n\n{Fore.CYAN}================= ORÇAMENTO DO ALUGUEL💵  =================")
            print(f"""
    Tipo do imóvel: APARTAMENTO
    {Fore.YELLOW}SEM Desconto
    {Fore.WHITE}Valor aluguel: {Fore.GREEN}R$ {valor_aluguel:.2f}
    {Fore.WHITE}Valor do parcelamento do Contrato: {Fore.GREEN}x{num_parcelas} de R$ {valor_contrato:.2f}
    """)

    while arquivo_csv != "s" and  arquivo_csv != "n":
        arquivo_csv = input(f"Deseja Gerar um arquivo Csv? (S/N):")
        if arquivo_csv == "s":
            orcamento_csv("Apartamento", valor_aluguel, valor_contrato, num_parcelas)
            print(f"{Fore.GREEN}Gerado com Sucesso!✅")
            print(f"\n{Fore.YELLOW}OBRIGADO POR UTILIZAR A IMOBILIÁRIA R.M😊!!!")
        elif arquivo_csv == "n":
            print(f"\n{Fore.YELLOW}OBRIGADO POR UTILIZAR A IMOBILIÁRIA R.M😊!!!")
        else:
            print(f"{Fore.RED}Opção não listada!", end="", flush=True)
            voltar()
            print("\033[F\033[K" * 4, end="", flush=True)
            continue

        voltar()










def menu_Casa():
    limpar_tela()
    print(f"{Fore.CYAN}================= CONFIGURAÇÃO DA CASA =================")
    print(f"Valor: {Fore.GREEN} R$ 900,00\n\n")

    valor_aluguel = 900.00
    tem_garagem = -1
    num_parcelas = 0
    arquivo_csv = ""

    while tem_garagem < 0 or tem_garagem > 3:
            try:
                tem_garagem = int(input("Quantas vagas de garagem deseja? (0-3):")).lower()

                if tem_garagem > 0 and tem_garagem <= 3:
                    valor_aluguel += (tem_garagem * 150.00)
                    print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
                elif tem_garagem == "0":
                    print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
                else:
                    print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.", end="", flush=True)
                    voltar()
                    print("\033[F\033[K" * 5, end="", flush=True)
            except ValueError:
                print(f"{Fore.RED}Opção INVÁLIDA! Digite apenas 1 ou 2.",end="", flush=True)
                voltar()
                print("\033[F\033[K" * 4, end="", flush=True)
            

    while num_parcelas < 1 or num_parcelas > 5:
            try:
                num_parcelas = int(input("Em quantas vezes quer parcelar o contrato (1-5)?: "))
                if 1 <= num_parcelas <= 5:
                    valor_contrato = 2000.00 / num_parcelas
                else:
                    print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.", end="", flush=True)
                    voltar()
                    print("\033[F\033[K" * 4, end="", flush=True)
            except ValueError:
                print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.", end="", flush=True)
                voltar()
                print("\033[F\033[K" * 4, end="", flush=True)



                limpar_tela()
                print(f"\n\n{Fore.CYAN}================= ORÇAMENTO DO ALUGUEL💵  =================")
                print(f"""
        Tipo do imóvel: Casa
        {Fore.WHITE}Valor aluguel: {Fore.GREEN}R$ {valor_aluguel:.2f}
        {Fore.WHITE}Valor do parcelamento do Contrato: {Fore.GREEN}x{num_parcelas} de R$ {valor_contrato:.2f}
        """)

    while arquivo_csv != "s" and  arquivo_csv != "n":
        arquivo_csv = input(f"Deseja Gerar um arquivo Csv? (S/N):")
        if arquivo_csv == "s":
            orcamento_csv("Casa", valor_aluguel, valor_contrato, num_parcelas)
            print(f"{Fore.GREEN}Gerado com Sucesso!✅")
            print(f"\n{Fore.YELLOW}OBRIGADO POR UTILIZAR A IMOBILIÁRIA R.M😊!!!")
        elif arquivo_csv == "n":
            print(f"\n{Fore.YELLOW}OBRIGADO POR UTILIZAR A IMOBILIÁRIA R.M😊!!!")
        else:
            print(f"{Fore.RED}Opção não listada!", end="", flush=True)
            voltar()
            print("\033[F\033[K" * 4, end="", flush=True)
            continue

        voltar()










def menu_estudio():
    limpar_tela()
    print(f"{Fore.CYAN}================= CONFIGURAÇÃO DO ESTÚDIO =================")
    print(f"Valor: {Fore.GREEN}R$ 1200,00\n\n")

    tem_garagem = -1
    num_parcelas = 0
    arquivo_csv = ""

    while tem_garagem < 0 or tem_garagem > 4:
            try:
                tem_garagem = int(input("Quantas vagas de garagem deseja? (0-4):")).lower()

                if tem_garagem > 0 and tem_garagem <= 2:
                    valor_aluguel += 250.00
                    print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
                elif tem_garagem > 2 and tem_garagem <= 4:
                    vagas_extras = tem_garagem - 2
                    valor_aluguel += 250.00 + (vagas_extras * 60.00)
                elif tem_garagem == "0":
                    print(f"Total: {Fore.GREEN}R$ {valor_aluguel:.2f}")
                else:
                    print(f"{Fore.RED}Opção inválida! Escolha de 1 a 4.", end="", flush=True)
                    voltar()
                    print("\033[F\033[K" * 5, end="", flush=True)
            except ValueError:
                print(f"{Fore.RED}Opção INVÁLIDA! Digite apenas de 1 a 4.",end="", flush=True)
                voltar()
                print("\033[F\033[K" * 4, end="", flush=True)


    while num_parcelas < 1 or num_parcelas > 5:
            try:
                num_parcelas = int(input("Em quantas vezes quer parcelar o contrato (1-5)?: "))
                if 1 <= num_parcelas <= 5:
                    valor_contrato = 2000.00 / num_parcelas
                else:
                    print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.", end="", flush=True)
                    voltar()
                    print("\033[F\033[K" * 4, end="", flush=True)
            except ValueError:
                print(f"{Fore.RED}Opção inválida! Escolha de 1 a 5.", end="", flush=True)
                voltar()
                print("\033[F\033[K" * 4, end="", flush=True)


            limpar_tela()
            print(f"\n\n{Fore.CYAN}================= ORÇAMENTO DO ALUGUEL💵 =================")
            print(f"""
    Tipo do imóvel: APARTAMENTO
    {Fore.YELLOW}Desconto de 5%!
    {Fore.WHITE}Valor aluguel: {Fore.GREEN}R$ {valor_aluguel:.2f}
    {Fore.WHITE}Valor do parcelamento do Contrato: {Fore.GREEN}x{num_parcelas} de R$ {valor_contrato:.2f}
    """)

    else:
            limpar_tela()
            print(f"\n\n{Fore.CYAN}================= ORÇAMENTO DO ALUGUEL💵  =================")
            print(f"""
    Tipo do imóvel: APARTAMENTO
    {Fore.YELLOW}SEM Desconto
    {Fore.WHITE}Valor aluguel: {Fore.GREEN}R$ {valor_aluguel:.2f}
    {Fore.WHITE}Valor do parcelamento do Contrato: {Fore.GREEN}x{num_parcelas} de R$ {valor_contrato:.2f}
    """)

    while arquivo_csv != "s" and  arquivo_csv != "n":
        arquivo_csv = input(f"Deseja Gerar um arquivo Csv? (S/N):")
        if arquivo_csv == "s":
            orcamento_csv("Estúdio", valor_aluguel, valor_contrato, num_parcelas)
            print(f"{Fore.GREEN}Gerado com Sucesso!✅")
            print(f"\n{Fore.YELLOW}OBRIGADO POR UTILIZAR A IMOBILIÁRIA R.M😊!!!")
        elif arquivo_csv == "n":
            print(f"\n{Fore.YELLOW}OBRIGADO POR UTILIZAR A IMOBILIÁRIA R.M😊!!!")
        else:
            print(f"{Fore.RED}Opção não listada!", end="", flush=True)
            voltar()
            print("\033[F\033[K" * 4, end="", flush=True)
            continue
        voltar()





    voltar()





menu_principal()
