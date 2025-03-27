from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contador')
def contador():
    # Obter a data atual automaticamente
    data_atual = datetime.now()
    
    # Definir a data final (23 de abril de 2025)
    data_final = datetime(2025, 4, 17)
    
    # Calcular os dias faltantes
    dias_faltantes = (data_final - data_atual).days

    # Retornar o número de dias faltantes
    return jsonify({'mensagem': f'Faltam apenas {dias_faltantes} dias para o fim do aviso.'})

if __name__ == '__main__':
    app.run(debug=True)
