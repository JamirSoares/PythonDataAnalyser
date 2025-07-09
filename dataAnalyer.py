import requests
import sys
import time
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()
eventos = []
API_ROUTE = os.getenv('ApiRoute')
BEARER = os.getenv('berearToken')
def get_excel():

    contador = 0
    pontos = '.' * (contador % 4)
    dataisrt = '2025-07-01'
    datafsrt = '2025-07-09'

    datai = datetime.strptime(dataisrt, '%Y-%m-%d')
    dataf = datetime.strptime(datafsrt, '%Y-%m-%d')
    mensagem = f"\rIniciando a coleta de dados{pontos}"
    print(mensagem)
    while datai <= dataf:
        

        time.sleep(0.5)
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

        if response.status_code == 200:
            data = response.json()

            for hora, lista_eventos in data.items():
                for evento in lista_eventos:      
                    if 'ending' in evento:                        
                        data_str = evento.get('beginning')
                        data_str = evento.get('beginning') 
                        print(f"Adicionando items da data: {data_str}")                                    
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
        datai += timedelta(days=1)  # Avança a data
        contador += 1

    print("\nColeta finalizada!")

    df = pd.DataFrame(eventos)
    df.to_csv("eventos.csv", index=False)
    return eventos


def get_graph():
    
    # df = 
    print(pd.read_csv("eventos.csv", usecols=['beginning', 'horas_Apontadas']))

    # df['beginning'] = pd.to_datetime(df['beginning'])

    # df = df.sort_values(by='beginning')
    # df.plot(x='beginning', y='horas_Apontadas', kind='line', figsize=(10, 5))
    # plt.xlabel('Data')
    # plt.ylabel('horas_Apontadas')
    # plt.show()


get_excel()
get_graph()
