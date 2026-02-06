
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
        print(f"{Fore.CYAN}================= IMOBILIÁRIA R.M - GERADOR DE ORÇAMENTO =================")
        print(f"\n(1) - Apartamento: {Fore.GREEN}R$ 700.00")
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
            menu_apartamento()





def menu_apartamento():
    limpar_tela()
    print(f"{Fore.CYAN}================= APARTAMENTO =================")
    print(f"Valor: {Fore.GREEN}R$ 700.00\n\n")

    valor_aluguel = 700.00
    qtd_quartos = ""

    while qtd_quartos != 2 and qtd_quartos != 1:
        qtd_quartos = int(input("Deseja um apartamento de 1 ou 2 quartos?: "))
        if qtd_quartos == 2:
            valor_aluguel += 200.00
            print(f"Total: {Fore.GREEN}{valor_aluguel:.2f}")
        elif qtd_quartos == 1:
            print(f"Total: {Fore.GREEN}{valor_aluguel:.2f}")
            pass
        else:
            print(f"{Fore.RED}Opção INVÁLIDA! Digite apenas 1 ou 2.")
            voltar()
        
    





    tem_garagem = input("Deseja vaga de garagem? (S/N):").upper
    if tem_garagem == "s":
        valor_aluguel += 300.00
        print(f"Total: {Fore.GREEN}{valor_aluguel:.2f}")
    elif tem_garagem == "n":
        print(f"Total: {Fore.GREEN}{valor_aluguel:.2f}")
    
        




    tem_criancas = input("Possui crianças residindo no imóvel? (S/N):").upper
    if tem_criancas == "n":
        valor_aluguel * 0.95 #desconto 5%
        print(f"Total: {Fore.GREEN}{valor_aluguel:.2f}")
        print(f"{Fore.YELLOW}Desconto de 5% aplicado!")
    elif tem_criancas == "s":
        print(f"Total: {Fore.GREEN}{valor_aluguel:.2f}")
    else:
        print(f"{Fore.RED}Opção não listada!")
        voltar()




    num_parcelas = int(input("Em quantas vezes quer parcelar o contrato (1-5)?: "))
    if num_parcelas:
        valor_aluguel = 2000.00 / num_parcelas
        print(f"Número de cada parcela: {valor_aluguel:.2f}")
        

    
    
    voltar()















def menu_Casa():
    limpar_tela()
    print(f"{Fore.CYAN}================= CASA =================")
    print(f"Valor: {Fore.GREEN} R$ 900,00\n\n")
    voltar()


def menu_estudio():
    limpar_tela()
    print(f"{Fore.CYAN}================= ESTÚDIO =================")
    print(f"Valor: {Fore.GREEN}R$ 1200,00\n\n")
    voltar()





menu_principal()

class Imovel:
    def __init__(self):
        self.taxa_contrato = 2000.00 
        self.aluguel_final = 0.00

class Apartamento(Imovel):
    def __init__(self):
        super().__init__() 
        self.valor_base = 700.00
    
    def calcular_aluguel(apartamento):
        return 

class Casa(Imovel):
    def __init__(self):
        super().__init__()
        self.valor_base = 900.00

class Estudio(Imovel):
    def __init__(self):
        super().__init__()
        self.valor_base = 1200.00