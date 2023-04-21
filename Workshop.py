# -*- coding: utf-8 -*-
"""VUT_workshop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14_nztiXzr9oXFnPpDsRxkNqGzhFADabL
"""

a = 1
b = 2
c = a + b
print(c)

def calculator():
    num1 = float(input("Zadej první číslo: "))
    num2 = float(input("Zadej druhé číslo: "))
    operation = input("Vyber operaci (+, -, *, /): ")

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        print("Nesprávná volba operace")

calculator()

import random

time_series = []

for i in range(100):
    time_series.append(random.random())

print(time_series)

import plotly.graph_objects as go
import random

time_series = []

for i in range(100):
    time_series.append(random.random())

fig = go.Figure(data=go.Scatter(y=time_series))
fig.show()

import plotly.graph_objects as go
import random
import datetime

time_series = []
dates = []

# Generování dat a náhodných čísel pro časovou řadu
for i in range(100):
    time_series.append(random.random())
    dates.append(datetime.date.today() + datetime.timedelta(days=i))

# Vytvoření grafu s daty na ose x
fig = go.Figure(data=go.Scatter(x=dates, y=time_series))
fig.show()

import plotly.graph_objects as go
import random
import datetime

time_series = []
dates = []

# Generování dat a náhodných čísel pro časovou řadu s růstovým trendem
for i in range(100):
    time_series.append(100 + 10 * i + random.random() * 10)
    dates.append(datetime.date.today() + datetime.timedelta(days=i))

# Vytvoření grafu s daty na ose x a časovou řadou s růstovým trendem
fig = go.Figure(data=go.Scatter(x=dates, y=time_series))
fig.update_layout(title='Růstový trend', xaxis_title='Datum', yaxis_title='Hodnota')
fig.show()

import plotly.graph_objects as go
import random
import datetime

time_series = []
dates = []

# Generování dat a náhodných čísel pro časovou řadu s růstovým trendem
for i in range(100):
    time_series.append(100 + 10 * i + random.random() * 10)
    dates.append(datetime.date.today() + datetime.timedelta(days=i))

# Vytvoření grafu s daty na ose x a časovou řadou s růstovým trendem se sníženou šířkou
fig = go.Figure(data=go.Scatter(x=dates, y=time_series))
fig.update_layout(title='Růstový trend', xaxis_title='Datum', yaxis_title='Hodnota')
fig.update_layout(width=600)
fig.show()

import yfinance as yf
import plotly.graph_objects as go

# Stáhne historická data ceny akcií společnosti Tesla
tesla_data = yf.download('TSLA', start='2022-01-01', end='2022-12-31')

# Vytvoří graf pomocí knihovny Plotly
fig = go.Figure(data=go.Scatter(x=tesla_data.index, y=tesla_data['Close']))
fig.update_layout(title='Cena akcií společnosti Tesla', xaxis_title='Datum', yaxis_title='Cena')
fig.show()

import yfinance as yf
import plotly.graph_objects as go
import datetime

# Vypočítá datum před 10 lety pro začátek historických dat
start_date = datetime.datetime.now() - datetime.timedelta(days=365 * 10)

# Stáhne historická data ceny akcií společnosti Tesla od začátku roku 2012
tesla_data = yf.download('TSLA', start=start_date.strftime('%Y-%m-%d'))

# Vytvoří graf pomocí knihovny Plotly
fig = go.Figure(data=go.Scatter(x=tesla_data.index, y=tesla_data['Close']))
fig.update_layout(title='Cena akcií společnosti Tesla', xaxis_title='Datum', yaxis_title='Cena')
fig.show()

import yfinance as yf
import plotly.graph_objects as go
import datetime

# Vypočítá datum před 10 lety pro začátek historických dat
start_date = datetime.datetime.now() - datetime.timedelta(days=365 * 10)

# Stáhne historická data ceny akcií společnosti Tesla od začátku roku 2012
tesla_data = yf.download('TSLA', start=start_date.strftime('%Y-%m-%d'))

# Vypočítá denní procentuální změnu ceny akcií
tesla_data['Daily Change'] = tesla_data['Close'].pct_change()

# Vytvoří graf pomocí knihovny Plotly
fig = go.Figure(data=go.Scatter(x=tesla_data.index, y=tesla_data['Daily Change']))
fig.update_layout(title='Denní procentuální změna ceny akcií společnosti Tesla', xaxis_title='Datum', yaxis_title='Procentuální změna')
fig.show()

import yfinance as yf
import datetime

# Vypočítá datum před 10 lety pro začátek historických dat
start_date = datetime.datetime.now() - datetime.timedelta(days=365 * 10)

# Stáhne historická data ceny akcií společnosti Tesla od začátku roku 2012
tesla_data = yf.download('TSLA', start=start_date.strftime('%Y-%m-%d'))

# Vypočítá denní procentuální změnu ceny akcií
tesla_data['Daily Change'] = tesla_data['Close'].pct_change()

# Určí, kolikrát došlo k dennímu poklesu/zvýšení o více než 10 %
num_big_changes = len(tesla_data[abs(tesla_data['Daily Change']) > 0.1])

print(f"Počet dnů s denní změnou o více než 10 %: {num_big_changes}")

import yfinance as yf
import plotly.graph_objects as go
import datetime

# Vypočítá datum před 6 lety pro začátek historických dat
start_date = datetime.datetime.now() - datetime.timedelta(days=365 * 6)

# Stáhne historická data ceny akcií společností Adobe, Tesla, Microsoft a McDonald's od roku 2015
adobe_data = yf.download('ADBE', start=start_date.strftime('%Y-%m-%d'))
tesla_data = yf.download('TSLA', start=start_date.strftime('%Y-%m-%d'))
microsoft_data = yf.download('MSFT', start=start_date.strftime('%Y-%m-%d'))
mcdonald_data = yf.download('MCD', start=start_date.strftime('%Y-%m-%d'))

# Vytvoří graf pomocí knihovny Plotly
fig = go.Figure()

# Přidá data o cenách akcií společnosti Adobe
fig.add_trace(go.Scatter(x=adobe_data.index, y=adobe_data['Close'], name='Adobe'))

# Přidá data o cenách akcií společnosti Tesla
fig.add_trace(go.Scatter(x=tesla_data.index, y=tesla_data['Close'], name='Tesla'))

# Přidá data o cenách akcií společnosti Microsoft
fig.add_trace(go.Scatter(x=microsoft_data.index, y=microsoft_data['Close'], name='Microsoft'))

# Přidá data o cenách akcií společnosti McDonald's
fig.add_trace(go.Scatter(x=mcdonald_data.index, y=mcdonald_data['Close'], name="McDonald's"))

fig.update_layout(title='Historie cen akcií', xaxis_title='Datum', yaxis_title='Cena')
fig.show()

import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Vypočítá datum před 6 lety pro začátek historických dat
start_date = datetime.datetime.now() - datetime.timedelta(days=365 * 6)

# Stáhne historická data ceny akcií společností Adobe, Tesla, Microsoft a McDonald's od roku 2015
adobe_data = yf.download('ADBE', start=start_date.strftime('%Y-%m-%d'))
tesla_data = yf.download('TSLA', start=start_date.strftime('%Y-%m-%d'))
microsoft_data = yf.download('MSFT', start=start_date.strftime('%Y-%m-%d'))
mcdonald_data = yf.download('MCD', start=start_date.strftime('%Y-%m-%d'))

# Vykreslí 4 grafy pomocí knihovny Seaborn a Matplotlib v jednom řádku
fig, axes = plt.subplots(1, 4, figsize=(15,5))

sns.lineplot(ax=axes[0], x=adobe_data.index, y=adobe_data['Close'], color='blue')
sns.lineplot(ax=axes[1], x=tesla_data.index, y=tesla_data['Close'], color='orange')
sns.lineplot(ax=axes[2], x=microsoft_data.index, y=microsoft_data['Close'], color='green')
sns.lineplot(ax=axes[3], x=mcdonald_data.index, y=mcdonald_data['Close'], color='red')

# Nastaví názvy os a titulek
axes[0].set(title='Historie cen akcií společnosti Adobe', xlabel='Datum', ylabel='Cena')
axes[1].set(title='Historie cen akcií společnosti Tesla', xlabel='Datum', ylabel='Cena')
axes[2].set(title='Historie cen akcií společnosti Microsoft', xlabel='Datum', ylabel='Cena')
axes[3].set(title='Historie cen akcií společnosti McDonald\'s', xlabel='Datum', ylabel='Cena')

plt.show()

import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# získání dat z YFinance
symbols = ['MSFT', 'AAPL', 'MMM', 'MCD']
start_date = '2010-01-01'
end_date = '2022-01-01'
data = yf.download(symbols, start=start_date, end=end_date)['Adj Close']

# vytvoření DataFrame s daty
df = pd.DataFrame(data, columns=symbols)

# vytvoření heatmapy korelací
sns.heatmap(df.corr(), annot=True)
plt.show()

import yfinance as yf
import pandas as pd

# získání informací o společnosti Tesla pomocí funkce yf.Ticker()
tsla = yf.Ticker("TSLA")

# uložení fundamentálních dat do DataFrame
fundamentals = tsla.info
df = pd.DataFrame.from_dict(fundamentals, orient='index', columns=['Value'])

# výpis základních fundamentálních dat
#print(df.loc[['marketCap', 'enterpriseValue', 'trailingPE', 'forwardPE', 'pegRatio']])
df

import yfinance as yf

# stáhnutí dat o cenách bitcoinu v USD pomocí symbolu "BTC-USD"
btc = yf.download("BTC-USD", start="2018-01-01")

# vybrání ceny uzavíracího kurzu (Adj Close) pro každý den
btc_price = btc['Adj Close']

# cena 1 bitcoinu na začátku roku 2018
initial_price = btc_price['2018-01-01']

# počet bitcoinů zakoupených za 1 USD
num_btc = 1 / initial_price

# aktuální cena bitcoinu
current_price = btc_price[-1]

# hodnota portfolia v USD
portfolio_value = num_btc * current_price

print("Hodnota portfolia: $", round(portfolio_value, 2))

# investice na začátku roku
initial_investment = 10000

# cena 1 bitcoinu na začátku roku
initial_price = btc_price['2018-01-01']

# počet bitcoinů koupených za počáteční investici
num_btc = initial_investment / initial_price

# aktuální cena bitcoinu
current_price = btc_price[-1]

# hodnota portfolia v USD
portfolio_value = num_btc * current_price

print("Hodnota portfolia: $", round(portfolio_value, 2))

# investice na začátku roku
btc_investment = 5000
eth_investment = 5000

# stáhnutí dat o cenách Bitcoinu a Etheru
crypto = yf.download(["BTC-USD", "ETH-USD"], start="2018-01-01")

# vybrání ceny uzavíracího kurzu (Adj Close) pro každý den
btc_price = crypto['Adj Close']['BTC-USD']
eth_price = crypto['Adj Close']['ETH-USD']

# počet Bitcoinů koupených za počáteční investici
num_btc = btc_investment / btc_price['2018-01-01']

# aktuální cena Bitcoinu
current_btc_price = btc_price[-1]

# hodnota Bitcoin portfolia v USD
btc_portfolio_value = num_btc * current_btc_price

# počet Etherů koupených za počáteční investici
num_eth = eth_investment / eth_price['2018-01-01']

# aktuální cena Etheru
current_eth_price = eth_price[-1]

# hodnota Ether portfolia v USD
eth_portfolio_value = num_eth * current_eth_price

# celková hodnota portfolia v USD
total_portfolio_value = btc_portfolio_value + eth_portfolio_value

print("Hodnota Bitcoin portfolia: $", round(btc_portfolio_value, 2))
print("Hodnota Ether portfolia: $", round(eth_portfolio_value, 2))
print("Celková hodnota portfolia: $", round(total_portfolio_value, 2))

import numpy as np
import matplotlib.pyplot as plt

num_investors = 30
total_assets = 500000000

# vygenerování náhodných vah pro rozdělení aktiv mezi investory
weights = np.random.dirichlet(np.ones(num_investors), size=1)[0]

# výpočet alokace pro každého investora
allocation = weights * total_assets

# vytvoření seznamu názvů investorů
investors = ["Investor " + str(i+1) for i in range(num_investors)]

# vytvoření koláčového grafu pro zobrazení alokace aktiv
plt.pie(allocation, labels=investors)
plt.title("Rozdělení aktiv mezi investory")
plt.show()

import backtrader as bt
import yfinance as yf

class MovingAverageStrategy(bt.Strategy):
    params = (
        ("sma_period", 50),  # délka klouzavého průměru
        ("printlog", False),  # výstup logů
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.sma_period
        )

    def next(self):
        if self.position.size == 0 and self.data.close[0] > self.sma[0]:
            self.buy(size=1)
        elif self.position.size > 0 and self.data.close[0] < self.sma[0]:
            self.close()

# definice datového zdroje
data = bt.feeds.PandasData(dataname=yf.download("SPY", start="2010-01-01"))

# inicializace Cerebro enginu
cerebro = bt.Cerebro()

# přidání dat do enginu
cerebro.adddata(data)

# přidání strategie do enginu
cerebro.addstrategy(MovingAverageStrategy)

# nastavení počátečního kapitálu
cerebro.broker.setcash(1000000)

# spuštění simulace
print("Počáteční kapitál: $%.2f" % cerebro.broker.getvalue())
cerebro.run()
print("Konečný kapitál: $%.2f" % cerebro.broker.getvalue())

class MovingAverageStrategy(bt.Strategy):
    params = (
        ("sma_period", 50),  # délka klouzavého průměru
        ("printlog", False),  # výstup logů
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.sma_period
        )

    def next(self):
        cash = self.broker.getcash()
        if cash <= 0:
            return

        max_shares = int(cash / self.data.close[0])

        if self.position.size == 0 and self.data.close[0] > self.sma[0]:
            self.buy(size=max_shares)
        elif self.position.size > 0 and self.data.close[0] < self.sma[0]:
            self.close()

# inicializace Cerebro enginu
cerebro = bt.Cerebro()

# přidání dat do enginu
cerebro.adddata(data)

# přidání strategie do enginu
cerebro.addstrategy(MovingAverageStrategy)

# nastavení počátečního kapitálu
cerebro.broker.setcash(10000)

# spuštění simulace
print("Počáteční kapitál: $%.2f" % cerebro.broker.getvalue())
cerebro.run()
print("Konečný kapitál: $%.2f" % cerebro.broker.getvalue())