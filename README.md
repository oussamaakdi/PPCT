### 📊 Explication des Variables - BitcoinHeist Dataset

| Variable | Description | Lien avec le ransomware |
|--|--|--|
| **address** | Adresse Bitcoin (wallet) | Identifiant public du portefeuille recevant ou envoyant des fonds. Les ransomwares utilisent des adresses spécifiques pour collecter les rançons. |
| **length** | Nombre total de transactions liées à cette adresse | Indique si l’adresse est fortement utilisée (recyclage possible dans certaines attaques). |
| **weight** | Indicateur de centralité de l’adresse dans le graphe | Les adresses très connectées sont souvent des **hubs** qui reçoivent des paiements de plusieurs victimes. |
| **count** | Nombre total de transactions entrantes/sortantes | Mesure l’activité de l’adresse, utile pour repérer des adresses de collecte actives. |
| **looped** | 1 si l’adresse réutilise des fonds entre adresses connues, sinon 0 | Le **looping** est une technique pour brouiller les pistes dans le blanchiment. |
| **neighbors** | Nombre d’adresses directement connectées | Faible nombre = adresse dédiée à une seule victime, fort nombre = possible hub de collecte. |
| **income** | Montant total reçu (en satoshis) | Permet d’estimer la valeur des rançons collectées. |
| **label** | Type de ransomware associé ou "princeton" si légitime | C’est la **cible** pour la classification supervisée. |

---

### 🔗 Processus typique d’un ransomware

1. Infection de la victime (fichiers chiffrés).
2. Demande de rançon avec une **adresse Bitcoin spécifique**.
3. La victime paie la rançon.
4. Les attaquants déplacent les fonds vers d’autres adresses (blanchiment via tumbling).
5. L’argent est retiré via des exchanges.

---

### 🎯 Utilisation des Variables

- Entraîner un **modèle ML** pour détecter les adresses suspectes.
- Étudier les **patterns de comportement** des ransomwares (fréquence, montants).
- Créer des **règles métiers** (ex : une adresse qui reçoit > 100 paiements en 1 semaine est suspecte).
- Visualiser le **réseau transactionnel** pour repérer les clusters suspects.

---
`
