import yfinance as yf
import prophet
import prophet.plot
import plotly_express as px
from fbprophet import Prophet

# Your code using Prophet goes here
modelo = Prophet()


ticker = input("Digite o código da Ação desejada: ")
pp = input("Deseja previsão de quantos dias? ")
dados = yf.Ticker(ticker).history("2y")

dados.Close.plot()

#REsetando o indice do DataFrame
treinamento = dados.reset_index()

#Removendo TimeZone da coluna data
treinamento["Date"] = treinamento["Date"].dt.tz_localize(None)

#Selecionando colunas data e valor de fechamento

treinamento = treinamento[["Date", "Close"]]

#Renomeando as colunas
treinamento.columns = ["ds", "y"]

# TREINANDO O MODELO #

#Criando o modelo
modelo = Prophet()

#Treinando o modelo com dados selecionados
modelo.fit(treinamento)

#Especificando o periodo das previsões
periodo = modelo.make_future_dataframe(periods=pp)

#Gerando as previsões
previsoes = modelo.predict(periodo)

fx(modelo, previsoes, xlabel="período", ylabel="valor")
