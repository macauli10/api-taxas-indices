import sqlite3
import requests
import time
from datetime import datetime

conn = sqlite3.connect('dados_financeiros.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS taxas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        valor REAL,
        data TEXT DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

print("🚀 Iniciando coleta de dados da BrasilAPI...\n")

try:
    while True:
        
        url = 'https://brasilapi.com.br/api/taxas/v1'
        response = requests.get(url)
        dados = response.json()

        
        coleta_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n🕒 Coleta realizada em: {coleta_hora}")
        print("📥 Dados obtidos da API:")

        
        for item in dados:
            nome = item['nome']
            valor = item['valor']
            cursor.execute('INSERT INTO taxas (nome, valor) VALUES (?, ?)', (nome, valor))
            print(f"🔹 {nome}: {valor:.2f}%")

        conn.commit()

        print("✅ Dados salvos no banco de dados!")
        print("⏳ Aguardando 10 segundos para nova coleta...\n")

        time.sleep(10)

except KeyboardInterrupt:
    print("\n🛑 Coleta interrompida pelo usuário.")
    conn.close()
