from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contador')
def contador():
    # Data inicial de 26 de março de 2025
    data_inicial = datetime(2025, 3, 26)
    
    # Data final de 17 de abril de 2025
    data_final = datetime(2025, 4, 17)
    
    # Obter a data atual automaticamente
    data_atual = datetime.now()
    
    # Calcular os dias faltantes entre a data inicial e a data final
    dias_faltantes = (data_final - data_atual).days

    if data_atual > data_final:
        mensagem = "Chegou ao fim seu ciclo."
    else:
        mensagem = f'Faltam apenas {dias_faltantes} dias para o fim do aviso.'
    
    # Retornar a mensagem
    return jsonify({'mensagem': mensagem})

if __name__ == '__main__':
    app.run(debug=True)
