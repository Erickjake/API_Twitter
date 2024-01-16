# Importando as bibliotecas necessárias
from flask import Flask, render_template
import plotly.express as px
import tweepy
import os

# Configurando as chaves de acesso do Twitter
consumer_key = 'Insira uma Chave'
consumer_secret = 'Insira uma Chave'
access_token = 'Insira uma Chave'
access_token_secret = 'Insira uma Chave'

# Configurando a autenticação com o Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Inicializando o Flask
app = Flask(__name__)

# Rota para exibir o dashboard
@app.route('/')
def dashboard():
    # Coletando dados do Twitter (exemplo: tweets sobre "python")
    tweets = api.search(q='python', count=100)

    # Criando um gráfico com Plotly Express
    fig = px.histogram(tweets, x='created_at', title='Número de Tweets ao longo do tempo')

    # Salvando o gráfico como arquivo HTML
    fig.write_html('templates/dashboard.html')

    # Renderizando o template HTML
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
