
# 1. Importar as bibliotecas necessárias
import requests
from django.shortcuts import render
import requests
from django.shortcuts import render




# 2. Definir a função para a página inicial
def home(request):
cidade = request.GET.get('cidade')

# Verificar se o usuário fez alguma consulta
if cidade:
# 3. Consultar a API de clima (Neste exemplo, usamos a OpenWeatherMap API)
url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&amp;appid=a6cf52a7b220498046a56aca5754e809'
response = requests.get(url)
data = response.json()

# 4. Obter as informações necessárias da resposta da API
cidade_nome = data['name']
temperatura = round(data['main']['temp'] - 273.15, 2) # Converter Kelvin para Celsius
descricao_clima = data['weather'][0]['description']
humidade = data['main']['humidity']
velocidade_vento = data['wind']['speed']

# 5. Renderizar a página com as informações
return render(request, 'dgclima.html', {'cidade_nome': cidade_nome,
'temperatura': temperatura,
'descricao_clima': descricao_clima,
'humidade': humidade,
'velocidade_vento': velocidade_vento})
else:
# 6. Renderizar a página inicial
return render(request, 'consulta.html')

