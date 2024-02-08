# Import do tkinter e pandas
from tkinter import *
from tkinter import ttk
import pandas as pd

# Criando e configurando título e geometry da janela
janela = Tk()
janela.title("Excel sem stress com pandas")
janela.geometry("1366x768")

# Salvando os dois dataframes
vendas_df = pd.read_excel("C://Users/bruno/Downloads/Lista tkinter.xlsx")
gerentes_df = pd.read_excel("C://Users/bruno/Downloads/Chefes de sessão.xlsx")


# Criando as funções

def tipos_vendas():
    tipos = vendas_df.dtypes
    resultado["text"] = tipos


def cinco():
    cinco_primeiras = vendas_df.head()
    resultado2["text"] = cinco_primeiras


def dez():
    dez_primeiras = vendas_df.head(10)

    resultado3["text"] = dez_primeiras


def produto():
    produtos = vendas_df['Produto']
    resultado4["text"] = produtos


def corredor():
    produtos = vendas_df['Corredor']
    resultado5["text"] = produtos


def valor_final():
    valores = vendas_df['Valor Final']
    resultado6["text"] = valores


def shape():
    shape_vendas = vendas_df.shape
    resultado7["text"] = shape_vendas


def linha_especifica():
    linha1 = vendas_df.loc[1]
    resultado8['text'] = linha1


def linhas_1_5():
    linhas_1a5 = vendas_df.loc[1:5]
    resultado9['text'] = linhas_1a5


def acougue():
    corredor_acougue = [vendas_df['Corredor'].str.contains('Açougue')]
    resultado10['text'] = corredor_acougue


def mercearia():
    corredor_mercearia = [vendas_df['Corredor'].str.contains('Mercearia')]
    resultado11['text'] = corredor_mercearia


def higiene():
    corredor_higiene = [vendas_df['Corredor'].str.contains('Higiene')]
    resultado12['text'] = corredor_higiene


def linha_produto():
    linha_70 = vendas_df.loc[70, 'Produto']
    resultado13['text'] = linha_70


def valor_maior():
    maior_5 = [vendas_df['Valor Final'] > 5]
    resultado14['text'] = maior_5


def criar_comissao():
    vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
    resultado15['text'] = vendas_df


def criar_imposto():
    vendas_df.loc[:, "Imposto"] = 0
    resultado16['text'] = vendas_df


def tirar_comissao():
    resultado17['text'] = vendas_df.drop("Comissão", axis=1)


def tirar_imposto():
    resultado18['text'] = vendas_df.drop("Imposto", axis=1)


def transacoes():
    transacoes_produto = vendas_df['Produto'].value_counts()
    resultado19['text'] = transacoes_produto


def faturamento():
    faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum()
    resultado20['text'] = faturamento_produto


def gerentes():
    resultado21['text'] = gerentes_df


# Widgets das 2 frames e canvas

frame_comandos = Frame(janela, bg='#0000cc', bd=4, relief="solid")
frame_comandos.grid(row=0, column=0, sticky=NW, padx=20, pady=20)  # os pads é distancia da janela

frame_resultados = Frame(janela, bg='#669999', bd=4, relief="solid")
frame_resultados.grid(row=0, column=1, sticky=NW, padx=20, pady=20)

canvas = Canvas(frame_comandos, width=600, height=298, bg="#e60000", bd=4, relief="raised")
canvas.grid(padx=5, pady=170)

frame_canvas_comandos = Frame(canvas, width=80, height=80, bg="#e60000")
frame_canvas_comandos.grid(pady=90, padx=10)

# Textos e botões da frame de comandos
texto_comando = Label(frame_canvas_comandos, text="--------------------------------------------------Comandos"
                                                  "--------------------------------------------------", font="Arial",
                      bg="#e60000"
                      )
texto_comando.grid(row=0, columnspan=3)

botao_tipos_vendas = Button(frame_canvas_comandos, text="Tipos de dados", command=tipos_vendas)
botao_tipos_vendas.grid(row=1, column=0, padx=5, pady=5)

botao_cinco_primeiras = Button(frame_canvas_comandos, text="Cinco primeiros produtos", command=cinco)
botao_cinco_primeiras.grid(row=1, column=1, padx=5, pady=5)

botao_dez_primeiras = Button(frame_canvas_comandos, text="Dez primeiros produtos", command=dez)
botao_dez_primeiras.grid(row=1, column=2, padx=5, pady=5)

# Linha 2
botao_produto = Button(frame_canvas_comandos, text="Coluna de produto", command=produto)
botao_produto.grid(row=2, column=0, padx=5, pady=5)

botao_corredor = Button(frame_canvas_comandos, text="Coluna de corredor", command=corredor)
botao_corredor.grid(row=2, column=1, padx=5, pady=5)

botao_valor_final = Button(frame_canvas_comandos, text="Coluna de valor final", command=valor_final)
botao_valor_final.grid(row=2, column=2, padx=5, pady=5)

# Linha 3
botao_tamanho = Button(frame_canvas_comandos, text="Linhas X Colunas ", command=shape)
botao_tamanho.grid(row=3, column=0, padx=5, pady=5)

botao_loc1 = Button(frame_canvas_comandos, text="Ver a linha do .loc[1]", command=linha_especifica)
botao_loc1.grid(row=3, column=1, padx=5, pady=5)

botao_loc1_5 = Button(frame_canvas_comandos, text="Ver a linha do .loc[1:5]", command=linhas_1_5)
botao_loc1_5.grid(row=3, column=2, padx=5, pady=5)
# Linha 4
botao_acougue = Button(frame_canvas_comandos, text="Produtos de Açougue", command=acougue)
botao_acougue.grid(row=4, column=0, padx=5, pady=5)

botao_mercearia = Button(frame_canvas_comandos, text="Produtos de Mercearia", command=mercearia)
botao_mercearia.grid(row=4, column=1, padx=5, pady=5)

botao_higiene = Button(frame_canvas_comandos, text="Produtos de Higiene", command=higiene)
botao_higiene.grid(row=4, column=2, padx=5, pady=5)
# Linha 5
botao_linha_70 = Button(frame_canvas_comandos, text="Produto da linha 70", command=linha_produto)
botao_linha_70.grid(row=5, column=0, padx=5, pady=5)

botao_descricao = Button(frame_canvas_comandos, text="Preços maiores que R$5", command=valor_maior)
botao_descricao.grid(row=5, column=1, padx=5, pady=5)

botao_comissao = Button(frame_canvas_comandos, text="Criar uma coluna de comissão", command=criar_comissao)
botao_comissao.grid(row=5, column=2, padx=5, pady=5)
# Linha 6
botao_imposto = Button(frame_canvas_comandos, text="Criar uma coluna de imposto", command=criar_imposto)
botao_imposto.grid(row=6, column=0, padx=5, pady=5)

botao_tirar_imposto = Button(frame_canvas_comandos, text="Tirar imposto", command=tirar_imposto)
botao_tirar_imposto.grid(row=6, column=1, padx=5, pady=5)

botao_tirar_comissao = Button(frame_canvas_comandos, text="Tirar comissão", command=tirar_comissao)
botao_tirar_comissao.grid(row=6, column=2, padx=5, pady=5)
# Linha 7
botao_transacoes = Button(frame_canvas_comandos, text="QTD de transações dos produtos", command=transacoes)
botao_transacoes.grid(row=7, column=0, padx=5, pady=5)

botao_faturamento = Button(frame_canvas_comandos, text="Faturamento dos produtos", command=faturamento)
botao_faturamento.grid(row=7, column=1, padx=5, pady=5)

botao_gerentes = Button(frame_canvas_comandos, text="Ver os gerentes", command=gerentes)
botao_gerentes.grid(row=7, column=2, padx=5, pady=5)
# Config da window da frame comandos
canvas.create_window((10, 10), window=frame_canvas_comandos, anchor='nw')

# ------------------------------------------------------
# Criando o canvas da segunda frame
canvas2 = Canvas(frame_resultados, width=600, height=625, bg='#009900')  # precisa ser da frame comandos
canvas2.grid(padx=10, pady=10)

vsb2 = ttk.Scrollbar(frame_resultados, orient="vertical", command=canvas2.yview)
vsb2.grid(row=0, column=6, sticky='ns')

canvas2.config(yscrollcommand=vsb2.set)

canvas2.bind('Configure', lambda e: canvas2.configure(scrollregion=(0, 0, 2000, 5300)))

frame_canvas_resultado = Frame(canvas2, width=80, height=80, bg='#009900')
frame_canvas_resultado.grid(pady=30, padx=30)

# Resultados da frame comandos
texto_resultado = Label(frame_canvas_resultado, text="-------------------------------------------------", bg="#009900")
texto_resultado.grid(row=0, column=0)

texto_resultado = Label(frame_canvas_resultado, text="Resultados", font="Arial", bg="#009900")
texto_resultado.grid(row=0, column=1)

texto_resultado = Label(frame_canvas_resultado, text="-------------------------------------------------", bg="#009900")
texto_resultado.grid(row=0, column=2)
# As labels dos resultados
resultado = Label(frame_canvas_resultado, text="", width=18, bg="#009900")
resultado.grid(columnspan=5, padx=10, pady=10)

resultado2 = Label(frame_canvas_resultado, text="", width=48, bg="#009900")
resultado2.grid(columnspan=5, padx=10, pady=10)

resultado3 = Label(frame_canvas_resultado, text="", width=48, bg="#009900")
resultado3.grid(columnspan=5, padx=10, pady=10)

resultado4 = Label(frame_canvas_resultado, text="", width=40, bg="#009900")
resultado4.grid(columnspan=5, padx=10, pady=10)

resultado5 = Label(frame_canvas_resultado, text="", width=44, bg="#009900")
resultado5.grid(columnspan=5, padx=10, pady=10)

resultado6 = Label(frame_canvas_resultado, text="", width=46, bg="#009900")
resultado6.grid(columnspan=5, padx=10, pady=10)

resultado7 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado7.grid(columnspan=5, padx=10, pady=10)

resultado8 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado8.grid(columnspan=5, padx=10, pady=10)

resultado9 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado9.grid(columnspan=5, padx=10, pady=10)

resultado10 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado10.grid(columnspan=5, padx=10, pady=10)

resultado11 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado11.grid(columnspan=5, padx=10, pady=10)

resultado12 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado12.grid(columnspan=5, padx=10, pady=10)

resultado13 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado13.grid(columnspan=5, padx=10, pady=10)

resultado14 = Label(frame_canvas_resultado, text="", width=60, bg="#009900")
resultado14.grid(columnspan=5, padx=10, pady=10)

resultado15 = Label(frame_canvas_resultado, text="", width=60, bg="#009900")
resultado15.grid(columnspan=5, padx=10, pady=10)

resultado16 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado16.grid(columnspan=5, padx=10, pady=10)

resultado17 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado17.grid(columnspan=5, padx=10, pady=10)

resultado18 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado18.grid(columnspan=5, padx=10, pady=10)

resultado19 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado19.grid(columnspan=5, padx=10, pady=10)

resultado20 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado20.grid(columnspan=5, padx=10, pady=10)

resultado21 = Label(frame_canvas_resultado, text="", width=50, bg="#009900")
resultado21.grid(columnspan=5, padx=10, pady=10)
# Config da window da frame resultados
canvas2.create_window((10, 10), window=frame_canvas_resultado, anchor='nw')
canvas2.config(scrollregion=(0, 0, 2000, 5400))

janela.mainloop()
