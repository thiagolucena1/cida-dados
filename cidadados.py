import requests
from tkinter import *
import customtkinter as ctk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
import tkinter.ttk as ttk



dados = [
  {"nome": "Ana Clara", "idade": 7, "cidade": "São Paulo"},
  {"nome": "Eduardo", "idade": 28, "cidade": "Rio de Janeiro"},
  {"nome": "Lara", "idade": 18, "cidade": "São Paulo"},
  {"nome": "Roberto", "idade": 36, "cidade": "Belo Horizonte"},
  {"nome": "Patrícia", "idade": 42, "cidade": "Salvador"},
  {"nome": "Marcelo", "idade": 10, "cidade": "Rio de Janeiro"},
  {"nome": "Beatriz", "idade": 5, "cidade": "São Paulo"},
  {"nome": "Renan", "idade": 63, "cidade": "Curitiba"},
  {"nome": "Tatiane", "idade": 22, "cidade": "Campinas"},
  {"nome": "Vinícius", "idade": 17, "cidade": "Fortaleza"},
  {"nome": "Giovana", "idade": 40, "cidade": "Recife"},
  {"nome": "Caio", "idade": 12, "cidade": "Belo Horizonte"},
  {"nome": "Elaine", "idade": 51, "cidade": "São Luís"},
  {"nome": "Fernando", "idade": 27, "cidade": "Salvador"},
  {"nome": "Nicole", "idade": 3, "cidade": "São Paulo"},
  {"nome": "Otávia", "idade": 31, "cidade": "Curitiba"},
  {"nome": "Bruno", "idade": 46, "cidade": "Florianópolis"},
  {"nome": "Danilo", "idade": 23, "cidade": "Campinas"},
  {"nome": "Milena", "idade": 66, "cidade": "Vitória"},
  {"nome": "Sérgio", "idade": 9, "cidade": "João Pessoa"},
  {"nome": "Daniel", "idade": 23, "cidade": "Campinas"},
  {"nome": "Marta", "idade": 66, "cidade": "Vitória"},
]



clientesOrdemAlfabetica = sorted(dados, key=lambda pessoas: pessoas["nome"] )

somaClientes= 0

for number in dados:
     somaClientes += 1


cidades = []
somaCidade = 0

for cidadee in dados:
     if ( cidadee["cidade"] not in cidades):
        cidades.append(cidadee["cidade"])
        somaCidade +=1


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Thiago\OneDrive\Área de Trabalho\thi\ProjectsPy\CidaDados\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

ctk.set_appearance_mode("light")  
window = ctk.CTk()

window.geometry("1000x550")
window.configure(bg = "#708090")


def processar_nome(nome):
    if not nome:
          messagebox.showerror("erro" "Erro nome inválido")
          return
    if len(nome) < 2:
          messagebox.showerror("erro" "Nome inválido")

    encontrado = None

    for names in dados: 
        if names["nome"].lower() == nome.lower():
             encontrado = names
             break
        
    if encontrado:
        texto = f"Nome: {encontrado['nome']}\nIdade: {encontrado['idade']}\n Cidade: {encontrado['cidade']}"
        label_resultado.configure(text= texto)
        

    else: 
         label_resultado.configure(text = "Cliente não encontrado ")

         
             
    


def janelaNome ():
    dialog = ctk.CTkInputDialog(text= "Escreva o nome do cliente", title="Filtre pelo nome dos clientes")

    nome = dialog.get_input()
    processar_nome(nome)


def processarMediaIdade():    # Função que processa a média dos clientes ao clicar no botão
     somaIdade = 0
     for idade in dados:
          if(idade['idade'] > 0):
            somaIdade += idade['idade']
            

     texto = f"A média da idade dos clientes são de {somaIdade/somaClientes}"
     label_resultado.configure(text=texto)
     print(texto)

def janelaCidade():
     janelaCidade = ctk.CTkToplevel(window)
     janelaCidade.title("Filtrar Todas as cidades Existentes cadastradas")
     janelaCidade.geometry("1000x550")
     
     tabela = ttk.Treeview(janelaCidade, selectmode="browse", columns= ("cidade", ), show="headings")
     tabela.column("cidade", width=300, anchor="w")
     tabela.heading("cidade", text="Cidades")
     tabela.pack(fill="both", expand=True, padx=20, pady=20)


     for names in cidades:
          tabela.insert("", "end", values=(names, ))
     

def processarCidade():
     
    janelaPerguntarCidade = ctk.CTkInputDialog(text= "Escreva o nome da cidade" , title="Nome da cidade?")
    nomeCidade = janelaPerguntarCidade.get_input()

    janelaClientePorCidade(nomeCidade)

    
    
     
def janelaClientePorCidade(nomeCidade):
    JanelaClientePorCidade = ctk.CTkToplevel(window)
    JanelaClientePorCidade.title(f"Clientes de {nomeCidade.title()}")
    JanelaClientePorCidade.geometry("600x400")

    tabelacompleta = ttk.Treeview(
        JanelaClientePorCidade,
        selectmode="browse",
        columns=("nome", "idade", "cidade"),
        show='headings'
    )

    tabelacompleta.heading("nome", text="Nome")
    tabelacompleta.heading("idade", text="Idade")
    tabelacompleta.heading("cidade", text="Cidade")
    tabelacompleta.column("nome", width=200, anchor="w")
    tabelacompleta.column("idade", width=80, anchor="center")
    tabelacompleta.column("cidade", width=200, anchor="w")
    tabelacompleta.pack(fill="both", expand=True, padx=20, pady=20)

    nomelocalizado = False 

    for inf in dados:
        if inf['cidade'].lower() == nomeCidade.lower(): 
             tabelacompleta.insert("", "end", values=(inf["nome"], inf["idade"], inf["cidade"]))
             nomelocalizado = True


    if not nomeLocalizado:
         tabelacompleta.insert("", "end", values=("Nenhum cliente com esse nome encontrado", "", ""))
            
               



canvas = Canvas(
    window, 
    bg = "#708090",
    height = 550,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    500.0000000350189,
    31.00000001376559,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    63.00000003501892,
    34.000000013765586,
    image=image_image_2
)

canvas.create_text(                 #logo
    92.00000003501893,
    18.00000001376559,                  
    anchor="nw",
    text="CidaDados",
    fill="#000000",
    font=("Inter Bold", 30 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    176.00000003501893,
    157.0000000137656,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    347.00000003501896,
    275.0000000137656,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))  #Retângulo do filtrar nome
image_5 = canvas.create_image(
    347.00000003501896,
    341.0000000137656,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png")) 
image_6 = canvas.create_image(
    136.00000003501893,
    341.0000000137656,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    136.00000003501893,
    275.0000000137656,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))     #Quadrado grande aonde fica as informações
image_8 = canvas.create_image(
    798.000000035019,
    307.0000000137656,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    462.0000000350189,
    158.0000000137656,
    image=image_image_9
)

canvas.create_text(
    83.00000003501893,
    130.0000000137656,
    anchor="nw",
    text= "Clientes Cadastrados",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    77.00000003501893,
    266.0000000137656,
    anchor="nw",
    text="Filtrar nome",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    67.00000003501893,
    332.0000000137656,
    anchor="nw",
    text="Filtrar Cidades",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    284.0000000350189,
    270.0000000137656,
    anchor="nw",
    text="Media de idade",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    272.0000000350189,
    326.0000000137656,
    anchor="nw",
    text="Filtrar clientes por cidade",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    377.0000000350189,
    130.0000000137656,
    anchor="nw",
    text="Cidades Cadastradas",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    357.0000000350189,
    142.0000000137656,
    image=image_image_10
)

canvas.create_text(
    147.00000003501893,
    149.0000000137656,
    anchor="nw",
    text=somaClientes,
    fill="#000000",
    font=("Inter Bold", 36 * -1)
)

canvas.create_text(
    441.0000000350189,
    150.0000000137656,
    anchor="nw",
    text=somaCidade,
    fill="#000000",
    font=("Inter Bold", 36 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    67.00000003501893,
    140.0000000137656,
    image=image_image_11
)

buttonFiltrarNome = ctk.CTkButton(window, text= "Filtrar Nome", width=120, height=30, fg_color="transparent", bg_color="#D9D9D9" ,border_width=0, hover_color="#D9D9D9", command=janelaNome, text_color="#000000", font=("Inter Bold", 16 * -1))
buttonFiltrarNome.place(x=77, y=266)

buttonFiltrarMedia = ctk.CTkButton(window, text= "Filtrar media Idade",  width=120, height=30, fg_color="transparent", bg_color="#D9D9D9" ,border_width=0, hover_color="#D9D9D9", command=processarMediaIdade, text_color="#000000", font=("Inter Bold", 16 * -1))
buttonFiltrarMedia.place(x= 284.0000000350189, y= 270.0000000137656)

buttonFiltrarCidade = ctk.CTkButton(window, text= "Filtrar cidade",  width=120, height=30, fg_color="transparent", bg_color="#D9D9D9" ,border_width=0, hover_color="#D9D9D9", command= janelaCidade, text_color="#000000", font=("Inter Bold", 16 * -1))
buttonFiltrarCidade.place( x= 67.00000003501893, y = 332.0000000137656)

buttonFiltrarClientesPorCidade = ctk.CTkButton(window, text="Filtrar clientes por cidade", width=120, height=30, fg_color="transparent", bg_color="#D9D9D9" ,border_width=0, hover_color="#D9D9D9", command=processarCidade, text_color="#000000", font=("Inter Bold", 16 * -1))
buttonFiltrarClientesPorCidade.place(x= 272.0000000350189, y= 326.0000000137656)


label_resultado = ctk.CTkLabel(window, text="Resultado")
label_resultado.place(x = 798.000000035019, y= 200)


window.resizable(False, False)
window.mainloop()
