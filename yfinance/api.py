pip install yfinance
import yfinance as yf
import matplotlib.pyplot as plt

# Télécharger les données d'Apple pour l'année 2023
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

# Afficher les premières lignes
print(data.head())

# Visualiser le prix de clôture
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label="Prix de Clôture", color='blue')
plt.title("Évolution du prix d'Apple (AAPL) en 2023")
plt.xlabel("Date")
plt.ylabel("Prix (USD)")
plt.legend()
plt.grid(True)
plt.show()

