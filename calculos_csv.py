
import csv


def orcamento_csv(tipo_imovel, valor_aluguel, valor_contrato, num_parcelas):
    nome_arquivo = f"orcamento_{tipo_imovel.lower()}.csv"
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            
            writer.writerow(['Imovel', 'Parcela', 'Aluguel', 'Contrato', 'Total Mensal'])
            
            
            for i in range(1, 13):
                total = valor_aluguel + valor_contrato
                writer.writerow([
                    tipo_imovel, 
                    f'Mes {i}', 
                    f'{valor_aluguel:.2f}', 
                    f'{valor_contrato:.2f}', 
                    f'{total:.2f}'
                ])
        return True
    except:
        return False