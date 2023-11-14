from tkinter import *
from tkinter import ttk
import locale

# Configura o locale para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# cor
co0 = '#ffffff'  # branca / white
co1 = '#444466'  # preta / black
co2 = '#4065a1'  # azul / blue
co3 = '#ADD8E6'  # azul claro / LightBlue

# Função para calcular empréstimo
def calcular_emprestimo():
    valor_emprestimo = float(locale.atof(e_emprestimo.get()))
    parcelas = int(e_numero.get())
    salario = float(locale.atof(e_salario.get()))

    # Adicione a condição para limitar o número de parcelas a 20
    if parcelas > 20:
        resultado = "Número máximo de parcelas em até 20 vezes."
        l_resultado_texto.config(text=resultado)
        return

    taxa_juros = 0.12 if parcelas == 12 else 0.20
    valor_parcela = (valor_emprestimo * (1 + taxa_juros)) / parcelas
    limite_salario = salario * 0.3

    if valor_parcela > limite_salario:
        resultado = "Empréstimo negado. A parcela excede 30% do salário."
    else:
        total_pago = valor_parcela * parcelas
        resultado = f"Empréstimo aprovado!\nTotal a pagar: {locale.currency(total_pago, grouping=True)}\nValor da parcela: {locale.currency(valor_parcela, grouping=True)}"

    l_resultado_texto.config(text=resultado)

# Função para resetar os campos de entrada
def resetar_campos():
    e_emprestimo.delete(0, END)
    e_numero.delete(0, END)
    e_salario.delete(0, END)
    l_resultado_texto.config(text='')

# Criação da janela
janela = Tk()
janela.title("Calculadora de Empréstimo")
janela.geometry('356x240')

# Dividindo a janela em duas partes
frame_cima = Frame(janela, width=356, height=60, bg=co3, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=356, height=262, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Configurando os campos de entrada
l_emprestimo = Label(frame_cima, text='Valor do Empréstimo (R$):', padx=0, relief='flat', anchor='center', font=('Ivy 10'),
                     bg=co3, fg=co1)
l_emprestimo.grid(row=0, column=0, sticky=NSEW, pady=5, padx=3)
e_emprestimo = Entry(frame_cima, width=26, relief='solid', font=('Ivy 10'), justify='center')
e_emprestimo.grid(row=0, column=1, sticky=NSEW, pady=5, padx=3)

l_numero = Label(frame_cima, text='Numero de Parcelas:', padx=0, relief='flat', anchor='center', font=('Ivy 10'), bg=co3,
                 fg=co1)
l_numero.grid(row=1, column=0, sticky=NSEW, pady=5, padx=3)
e_numero = Entry(frame_cima, width=26, relief='solid', font=('Ivy 10'), justify='center')
e_numero.grid(row=1, column=1, sticky=NSEW, pady=5, padx=3)

l_salario = Label(frame_cima, text='Valor do Salário (R$):', padx=0, relief='flat', anchor='center', font=('Ivy 10'),
                  bg=co3, fg=co1)
l_salario.grid(row=2, column=0, sticky=NSEW, pady=5, padx=3)
e_salario = Entry(frame_cima, width=26, relief='solid', font=('Ivy 10'), justify='center')
e_salario.grid(row=2, column=1, sticky=NSEW, pady=5, padx=3)

# Botão para calcular
b_calcular = Button(frame_cima, text='CALCULAR', width=34, height=1, overrelief=SOLID, relief='raised', anchor='center',
                    font=('Ivy 10 bold '), bg=co2, fg=co0, command=calcular_emprestimo)
b_calcular.grid(row=3, column=0, sticky=NSEW, pady=5, padx=3, columnspan=3)

# Botão para resetar
b_resetar = Button(frame_cima, text='NOVO CÁLCULO', width=34, height=1, overrelief=SOLID, relief='raised',
                   anchor='center', font=('Ivy 10 bold '), bg=co2, fg=co0, command=resetar_campos)
b_resetar.grid(row=4, column=0, sticky=NSEW, pady=5, padx=3, columnspan=3)

# Configuração do rótulo de resultado
l_resultado_texto = Label(frame_baixo, text='', width=43, height=2, padx=0, pady=12, relief='flat', anchor='center',
                         font=('Ivy 10'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=0)

janela.resizable(False, False)

janela.mainloop()
