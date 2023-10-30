from flask import Flask, render_template, request
app = Flask(__name__)

#Rota: HOME ou Principal
@app.route('/', methods=['GET', 'POST'])
def index():
  nome = None
  if request.method == 'POST' and 'nome' in request.form:
    nome = request.form['nome']
  return render_template('index.html', nome=nome)

app.run(debug=True)