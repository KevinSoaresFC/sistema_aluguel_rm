# 🏠 Sistema de Gestão de Locação - Imobiliária R.M

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)

## 📋 Sobre o Projeto
Desenvolvido como projeto prático para o curso de **Análise e Desenvolvimento de Sistemas (UniFECAF)**, este sistema automatiza o processo de orçamento de aluguéis para a Imobiliária R.M. 

O foco principal foi a transposição de uma lógica de negócio robusta em **Python** para uma interface **Web dinâmica**, garantindo que as regras de contrato, descontos e validações de infraestrutura sejam aplicadas de forma impecável.

---

## 🚀 Funcionalidades Principais

- **Cálculo Dinâmico de Aluguel:** Baseado no tipo de imóvel (Apartamento, Casa ou Estúdio).
- **Regras de Negócio Específicas:**
  - Adicionais por quantidade de quartos e vagas de garagem.
  - Cálculo de excedente para vagas extras em Estúdios (R$ 60,00 por vaga).
  - Desconto automático de 5% para apartamentos sem crianças.
- **Gestão de Contrato:** Parcelamento do valor de adesão (R$ 2.000,00) em até 5x.
- **Interface Inteligente:** O formulário Web adapta os campos visíveis de acordo com o tipo de imóvel selecionado (DOM Manipulation).
- **Validação de Dados:** Sistema de mensagens de erro integrado que impede cálculos com dados inconsistentes.

---

## 🛠️ Tecnologias Utilizadas

### **Backend & Lógica**
* **Python**: Processamento de dados, estruturas de repetição (`while`) e tratamento de exceções (`try/except`).
* **CSV**: Estruturação de dados para exportação de orçamentos de 12 meses.

### **Frontend (Web)**
* **HTML5**: Estruturação semântica da interface.
* **CSS3**: Estilização moderna e layout responsivo.
* **JavaScript (Vanilla)**: Lógica de integração, cálculos em tempo real e manipulação dinâmica da interface.

