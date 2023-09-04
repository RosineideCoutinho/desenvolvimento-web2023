from tkinter import*
from tkinter import ttk
import requests
import tkinter as tk
from tkinter  import messagebox
# sem django e pycharm
def obter_clima():
cidade = entrada_cidade.get()

# Verifica se o campo da cidade está vazio
if not cidade:
messagebox.showerror("Erro", "Digite uma cidade antes de consulter o clima.")
return

# Configura a chave de API e a URL da API
chave_api = "a6cf52a7b220498046a56aca5754e809"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&amp;appid={chave_api}"

try:
# Faz a requisição à API de clima
resposta = requests.get(url)
dados_clima = resposta.json()

# Verifica se a cidade foi encontrada
if dados_clima["cod"] != "404":
# Extrai as informações do clima
nome_cidade = dados_clima["name"]
temperatura = dados_clima["main"]["temp"]
descricao_clima = dados_clima["weather"][0]["description"]
humidade = dados_clima["main"]["humidity"]
velocidade_vento = dados_clima["wind"]["speed"]

# Mostra as informações na interface de usuário
texto_resultado.config(text=f"Cidade: {nome_cidade}\nTemperatura: {temperatura} °C\nDescrição: {descricao_clima}\nUmidade: {humidade}%\nVelocidade do Vento: {velocidade_vento} m/s")
else:
# Caso a cidade não seja encontrada
messagebox.showerror("Erro", "Cidade não encontrada.")
except requests.exceptions.RequestException:
messagebox.showerror("Erro de conexão", "Não foi possível se conectar à API de clima.")

# Configuração da interface de usuário
janela = tk.Tk()
janela.title("Consultar Clima")
janela.geometry("400x300")

label_cidade = tk.Label(janela, text="Digite o nome da cidade:")
label_cidade.pack()

entrada_cidade = tk.Entry(janela)
entrada_cidade.pack()

botao_consultar = tk.Button(janela, text="Consultar", command=obter_clima)
botao_consultar.pack()

texto_resultado = tk.Label(janela, text="")
texto_resultado.pack()

janela.mainloop()
```