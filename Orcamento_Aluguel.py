
import os
from colorama import Fore, init
import csv 

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'NT' else 'clear')

def voltar():
    input(f"{Fore.YELLOW}\n\nPressione o 'ENTER' para voltar...")


def menu_principal():
    while True:
        limpar_tela()
        print(f"{Fore.CYAN}================= IMOBILIÁRIA R.M - GERADOR DE ORÇAMENTO =================")
        print(f"\n(1) - Apartamento: {Fore.GREEN}R$ 700,00")
        print(f"(2) - Casa: {Fore.GREEN}R$ 900,00")
        print(f"(3) - Estúdio: {Fore.GREEN}R$ 1200,00")
        print(f"{Fore.RED}(0) - Sair\n")
        opcao = input("Escolha uma opcão: ")

        if opcao == "1":
            print(f"{Fore.GREEN}ENTRANDO EM APARTAMENTO...")
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
    print(f"{Fore.CYAN}================= APARTAMENTO =================")
    
    apto = Apartamento()

    print(f"Valor Base: R$ {apto.valor_base}")
    voltar()


def menu_Casa():
    limpar_tela()
    print(f"{Fore.CYAN}================= CASA =================")
    voltar()


def menu_estudio():
    limpar_tela()
    print(f"{Fore.CYAN}================= ESTÚDIO =================")
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