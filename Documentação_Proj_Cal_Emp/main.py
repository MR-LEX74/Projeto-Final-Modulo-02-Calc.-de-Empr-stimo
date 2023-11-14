def calcular_emprestimo():
    """Esta função calcula o valor das parcelas de um empréstimo com base nos valores fornecidos pelo usuário.

    A função pega os valores inseridos nos campos de entrada e realiza os cálculos necessários para determinar se o
    empréstimo é aprovado ou negado. A taxa de juros é de 0.12 para parcelas até 12 vezes e 0.20 acima de 12 vezes

    O número de parcelas disponível para empréstimo é de até 20 vezes. Se o número de parcelas for superior a 20, a função exibe uma mensagem informando que o número máximo de parcelas é
    de 20.

    Se a parcela exceder 30% do salário, o empréstimo é negado.

    Caso contrário, o empréstimo é aprovado e a função exibe o total a ser pago e o valor de cada parcela.
    """
return: None
    """ # Obtém os valores dos campos de entrada
    valor_emprestimo = float(locale.atof(e_emprestimo.get()))
    parcelas = int(e_numero.get())
    salario = float(locale.atof(e_salario.get()))

    # Adicione a condição para limitar o número de parcelas a 20
    if parcelas > 20:
        resultado = "Número máximo de parcelas em até 20 vezes."
        l_resultado_texto.config(text=resultado)
        return

    # Calcula a taxa de juros com base no número de parcelas
    taxa_juros = 0.12 if parcelas == 12 else 0.20

    # Calcula o valor de cada parcela
    valor_parcela = (valor_emprestimo * (1 + taxa_juros)) / parcelas

    # Calcula o limite de parcela baseado no salário
    limite_salario = salario * 0.3

    if valor_parcela > limite_salario:
        resultado = "Empréstimo negado. A parcela excede 30% do salário."
    else:
        total_pago = valor_parcela * parcelas
        resultado = f"Empréstimo aprovado!\nTotal a pagar: {locale.currency(total_pago, grouping=True)}\nValor da parcela: {locale.currency(valor_parcela, grouping=True)}"

    l_resultado_texto.config(text=resultado)
    """
def resetar_campos():
    """Esta função limpa os campos de entrada e o rótulo de resultado.

    """# Configuração da interface gráfica
    # Importando os módulos necessários
from tkinter import *
from tkinter import ttk
import locale

# Configura o locale para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Definição das cores
co0 = '#ffffff'  # branca / white
co1 = '#444466'  # preta / black
co2 = '#4065a1'  # azul / blue
co3 = '#ADD8E6'  # azul claro / LightBlue
