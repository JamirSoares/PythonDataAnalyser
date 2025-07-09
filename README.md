# PythonDataAnalyser

Projeto em Python para coleta, processamento e visualização de dados a partir de uma API externa.

## 📌 Descrição

Este script realiza as seguintes etapas:

1. Coleta dados de eventos entre duas datas definidas
2. Processa os dados, calcula a duração de eventos em minutos
3. Armazena os resultados em um arquivo CSV (`eventos.csv`)
4. Exibe os dados processados no console (função de gráfico comentada para uso posterior)

---

## 🚀 Como executar

### 1. Instale as dependências

Certifique-se de ter o Python instalado (recomenda-se Python 3.9+).  
Instale as bibliotecas com:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` com as seguintes variáveis:

```env
ApiRoute=https://sua-url-da-api.com/rota
berearToken=Bearer eyJ...seu_token...
```

### 2. Execute o script principal

```bash
python seu_script.py
```

> O script irá gerar um arquivo `eventos.csv` com os dados coletados.

---

## 🧠 Bibliotecas utilizadas

- `requests` — Para chamadas HTTP
- `pandas` — Para manipulação e exportação de dados
- `matplotlib` — (comentado, usado para gráfico)
- `dotenv` — Para ler variáveis do arquivo `.env`
- `datetime`, `time`, `os`, `sys` — Utilitários nativos

---

## 📁 Arquivos gerados

- `eventos.csv` — Contém os dados processados dos eventos extraídos
- `print` no console com logs do processo de coleta
- Trecho pronto para gráficos (comentado)

---

## 👨‍💻 Autor

**Jamir Soares Rodrigues**

---

## 📝 Licença

Este projeto ainda **não possui uma licença definida**.