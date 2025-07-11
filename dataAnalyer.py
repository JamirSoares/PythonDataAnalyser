import requests
import sys
import time
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import ast
import os

load_dotenv()
eventos = []
API_ROUTE = os.getenv('ApiRoute')
BEARER = os.getenv('berearToken')
def get_excel():
    print("Coletando dados...")
    dataisrt = '2025-07-01'
    datafsrt = '2025-07-09'

    datai = datetime.strptime(dataisrt, '%Y-%m-%d')
    dataf = datetime.strptime(datafsrt, '%Y-%m-%d')
    
    while datai <= dataf:
        dataAnterior = '2025-01-01'        
        data_formatada = datai.strftime('%Y-%m-%d')
        url = API_ROUTE

        headers = {
            "authorization": BEARER,
            "content-type": "application/json",
        }

        

        payload = {
            "id": 1006984,
            "current_date": f"{data_formatada}T11:25:57.327Z"
        }

        response = requests.post(url, headers=headers, json=payload)

        try:
            response.raise_for_status()  
        except ValueError:
            print("Resposta de texto:", response.text)
        if  datai.strftime('%Y-%m-%d') != dataAnterior:
            dataAnterior = datai.strftime('%Y-%m-%d')
            print(f"Coletando dados para a data: {datai.strftime('%Y-%m-%d')}")
        if response.status_code == 200:
            data = response.json()

            for hora, lista_eventos in data.items():
                for evento in lista_eventos:      
                    if 'ending' in evento:                        
                        data_str = evento.get('beginning')
                        data_str = evento.get('beginning')                                  
                        eventos.append({
                            'hora': hora,
                            'beginning': datetime.fromisoformat(evento.get('beginning')).strftime('%Y-%m-%d-%H:%M:%S'),
                            'ending': datetime.fromisoformat(evento.get('ending')).strftime('%Y-%m-%d-%H:%M:%S'),
                            'description': evento.get('description'),
                            'url_id': evento.get('url_id'),
                            'horas_Apontadas': (datetime.fromisoformat(evento.get('ending')) - datetime.fromisoformat(evento.get('beginning'))).total_seconds()/60

                        })

        else:
            print("Erro ao obter dados:", response.status_code)
        datai += timedelta(days=1) 
    print("\nColeta finalizada!")
    return eventos


def get_graph(eventos):
    eventos_lista = eventos

    # Extrair datas únicas (YYYY-MM-DD)
    beginning_array = [datetime.fromisoformat(item['beginning']).strftime('%Y-%m-%d') for item in eventos_lista]

    dias_unicos = sorted(set(beginning_array))

    horas_por_dia = []

    for dia in dias_unicos:
        soma_minutos = 0
        for i, data in enumerate(beginning_array):
            if data == dia:
                soma_minutos += eventos_lista[i]['horas_Apontadas']  # soma direto o valor numérico em minutos
        tempo_total = timedelta(minutes=soma_minutos)
        horas_formatadas = str(tempo_total)[:-3]  # Remove os últimos 3 caracteres para tirar os segundos
        horas_por_dia.append((dia, horas_formatadas))

    # Exibir o resultado
    for dia, horas in horas_por_dia:
        print(f"{dia} - {horas} horas")
    dias = [dia for dia, _ in horas_por_dia]
    valores = [minutos for _, minutos in horas_por_dia]

    plt.figure(figsize=(10, 5))
    plt.bar(dias, valores, color='cornflowerblue')
    plt.title('Tempo total por dia (em minutos)')
    plt.xlabel('Data')
    plt.ylabel('Minutos apontados')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

get_excel()

get_graph(eventos)
