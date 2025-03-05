import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# --- Configuration générale ---
st.set_page_config(page_title="BitcoinHeist Dashboard", layout="wide")

# --- Chargement des données et modèle ---
@st.cache_resource
def load_model():
    return joblib.load('xgboost_ransomware_model.joblib')

@st.cache_data
def load_data():
    df = pd.read_csv('BitcoinHeistData.csv')
    return df.sample(100000, random_state=42)  # Sample 100k pour alléger

model = load_model()
df = load_data()

# --- Sidebar pour navigation ---
page = st.sidebar.radio("Navigation", ["Dashboard", "Prédiction"])

# --- Dashboard ---
if page == "Dashboard":
    st.title("📊 Dashboard BitcoinHeist")

    # 1️⃣ Head() coloré
    st.write("### Aperçu des données (échantillon 100k)")

    df_display = df.head(10).copy()
    df_display['label'] = df_display['label'].apply(
        lambda x: f'🟢 {x}' if x == 'white' else f'🔴 {x}'
    )
    st.dataframe(df_display)

    # 2️⃣ Evolution des ransomwares par jour (courbe)
    st.write("### Nombre d’adresses ransomwares par jour")

    df_ransom = df[df['label'] != 'white'].copy()
    df_ransom['date'] = pd.to_datetime('2020-01-01') + pd.to_timedelta(df_ransom['day'], unit='D')

    daily_counts = df_ransom.groupby(['year', 'date']).size().reset_index(name='count')

    plt.figure(figsize=(15,6))
    for year in daily_counts['year'].unique():
        subset = daily_counts[daily_counts['year'] == year]
        plt.plot(subset['date'], subset['count'], label=f'Année {year}')

    plt.gca().set_xticks(pd.date_range(start='2020-01-01', end='2020-12-31', freq='MS'))
    plt.gca().set_xticklabels(pd.date_range(start='2020-01-01', end='2020-12-31', freq='MS').strftime('%B'))

    plt.xlabel('Mois')
    plt.ylabel('Nombre d’adresses ransomwares')
    plt.title('Nombre d’adresses ransomwares par jour')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # 3️⃣ Distribution des montants reçus (log scale)
    st.write("### Distribution des montants reçus par les ransomwares (log scale)")

    plt.figure(figsize=(10,5))
    sns.histplot(df_ransom['income'], bins=50, log_scale=True)
    plt.title("Montants reçus par les ransomwares")
    plt.xlabel("Montant reçu (satoshis)")
    st.pyplot(plt)

    # 4️⃣ Top 5 montants les plus fréquents
    st.write("### Top 5 des montants les plus fréquents (ransomwares)")
    top5_incomes = df_ransom['income'].value_counts().head(5)
    st.write(top5_incomes)

# --- Prédiction ---
if page == "Prédiction":
    st.title("🔎 Prédiction sur une transaction")

    with st.form("transaction_form"):
        st.write("### Entrer les caractéristiques de la transaction")

        length = st.number_input("Nombre total de transactions (length)", min_value=0)
        weight = st.number_input("Poids de la transaction (weight)", min_value=0.0, step=0.01, format="%.5f")
        count = st.number_input("Nombre total d’inputs/outputs (count)", min_value=0)
        looped = st.number_input("Nombre de boucles (looped)", min_value=0)
        neighbors = st.number_input("Nombre de voisins (neighbors)", min_value=0)
        income = st.number_input("Montant reçu (income)", min_value=0.0,format="%.12f")

        duration = st.number_input("Durée d’activité (en jours)", min_value=1, value=30)
        transactions_per_day = length / duration

        submitted = st.form_submit_button("Prédire si cette transaction est suspecte")

    if submitted:
        new_transaction = pd.DataFrame({
            'length': [length],
            'weight': [weight],
            'count': [count],
            'looped': [looped],
            'neighbors': [neighbors],
            'income': [income],
            'transactions_per_day': [transactions_per_day]
        })

        prediction = model.predict(new_transaction)[0]

        if prediction == 1:
            st.error("🚨 Cette transaction est classée comme **ransomware suspect** !")
        else:
            st.success("✅ Cette transaction est classée comme **légitime (white)**.")
