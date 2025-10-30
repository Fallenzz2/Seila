from flask import Flask, render_template, jsonify, request
from datetime import datetime
import os


app = Flask(__name__)


# Config básica (pode usar python-dotenv para carregar .env)
app.config['APP_NAME'] = os.getenv('APP_NAME', 'Relatórios Financeiros')


# Página inicial (template simples)
@app.route('/')
def index():
return render_template('index.html', app_name=app.config['APP_NAME'])


# API exemplo: retorna relatório financeiro fictício
@app.route('/api/reports', methods=['GET'])
def get_reports():
# parâmetros opcionais
periodo = request.args.get('period', 'mensal')


# dados mock — substitua pela lógica real/BD
reports = [
{
'id': 1,
'title': 'Relatório de Vendas',
'period': periodo,
'generated_at': datetime.utcnow().isoformat() + 'Z'
},
{
'id': 2,
'title': 'Relatório de Despesas',
'period': periodo,
'generated_at': datetime.utcnow().isoformat() + 'Z'
}
]
return jsonify(reports)


if __name__ == '__main__':
# Em desenvolvimento: debug=True. Em produção, use um WSGI server (gunicorn/uvicorn)
app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
