# 🌱 Site MMLB - Plateforme ESG & Outils Financiers

## 📋 Description du Projet

**Site MMLB** est une plateforme web interactive développée avec Streamlit, présentant les services et outils de **Matthieu Moreau-Le Breton** dans les domaines de l'analyse ESG (Environnement, Social, Gouvernance) et des outils financiers.

### 🎯 Objectifs
- Présenter le projet **Convergence** - Plateforme d'analyse ESG automatisée
- Offrir des outils financiers et éducatifs
- Fournir des ressources et articles sur la durabilité et l'investissement responsable

## 🚀 Fonctionnalités Principales

### 📝 Section Articles
- **Article Convergence** : Présentation complète du projet ESG avec ressources
- **Articles à venir** : Pipeline de contenu en préparation
- Interface moderne avec tags et boutons d'action

### 🛠️ Section Outils
- **Générateur de Scénarios Économiques** (en développement)
  - Simulation de classes d'actifs : Immobilier, Private Equity, Obligations, Actions
  - Analyse de stress-testing et VaR
  - Optimisation de portefeuille

- **Cours Python - Fondamentaux & Machine Learning** (en développement)
  - Module 1 : Les Bases (syntaxe, structures, fonctions)
  - Module 2 : Packages Essentiels (NumPy, Pandas, Matplotlib)
  - Module 3 : Introduction ML (Scikit-learn, modèles)

## 🛠️ Technologies Utilisées

- **Backend** : Python 3.12+
- **Framework Web** : Streamlit 1.28+
- **Visualisation** : Plotly, Matplotlib, Seaborn
- **Traitement de données** : Pandas, NumPy
- **Interface** : HTML/CSS personnalisé

## 📦 Installation

### Prérequis
- Python 3.12 ou supérieur
- pip (gestionnaire de packages Python)

### Étapes d'installation

1. **Cloner le projet**
   ```bash
   git clone https://github.com/M-au-Cube/mon-site-streamlit.git
   cd mon-site-streamlit
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Lancement de l'Application

### Méthode 1 : Commande directe
```bash
python -m streamlit run app_matthieu.py
```

### Méthode 2 : Avec paramètres spécifiques
```bash
python -m streamlit run app_matthieu.py --server.port 8501 --server.address localhost
```

### Méthode 3 : Script batch (Windows)
Double-cliquez sur `lancer_app_matthieu.bat`

## 🌐 Accès à l'Application

Une fois lancée, l'application sera accessible à l'adresse :
- **URL locale** : http://localhost:8501
- **URL réseau** : http://[VOTRE_IP]:8501

## 📁 Structure du Projet

```
Site_MMLB_streamlit/
├── app_matthieu.py          # Application principale Streamlit
├── requirements.txt         # Dépendances Python
├── README.md                # Documentation du projet
├── Logo_Convergence.png     # Logo du projet Convergence
├── CV_generalist_matthieu_moreau-le_breton.pdf  # CV associé
├── articles.json            # Base de données des articles
└── lancer_app_matthieu.bat  # Script de lancement Windows
```

## 🔧 Configuration

### Variables d'environnement
L'application utilise les paramètres par défaut de Streamlit. Vous pouvez les personnaliser en créant un fichier `.streamlit/config.toml` (déjà présent pour le déploiement Cloud) :

```toml
[server]
port = 8501
address = "0.0.0.0"
headless = true

[browser]
gatherUsageStats = false
```

### Ports
- **Port par défaut** : 8501
- **Port alternatif** : 8502 (si 8501 est occupé)

## 📚 Utilisation

### Navigation
1. **Accueil** : Présentation générale et CV
2. **Expertises** : Services et compétences
3. **Formation** : Parcours académique et certifications
4. **Articles** : Contenu Convergence et articles à venir
5. **Outils** : Générateur de scénarios et cours Python

### Fonctionnalités Interactives
- Boutons d'action pour chaque article
- Navigation entre sections
- Interface multilingue
- Tags et catégorisation

## 🚧 Développement

### Ajout de nouveaux articles
Modifiez directement le code dans `app_matthieu.py` dans la section Articles.

### Ajout de nouveaux outils
Ajoutez vos outils dans la section Outils du fichier principal.

### Personnalisation du style
Modifiez les variables CSS dans la fonction `local_css()`.

## 🐛 Résolution de Problèmes

### Erreur "Port déjà utilisé"
```bash
# Windows
taskkill /f /im python.exe

# Linux/Mac
pkill -f streamlit
```

### Erreur "Module non trouvé"
```bash
pip install -r requirements.txt
```

### Application qui se ferme immédiatement
- Vérifiez que Python est dans votre PATH
- Utilisez le chemin complet vers Python
- Vérifiez les permissions du dossier

## 📞 Support

Pour toute question ou problème :
- **Email** : matt.mlb@icloud.com
- **LinkedIn** : https://www.linkedin.com/in/matthieu-moreau-le-breton-b0a248184/
- **GitHub** : https://github.com/M-au-Cube

## 📄 Licence

Ce projet est sous licence MIT.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## 📈 Roadmap

- [ ] Intégration de l'API ESG
- [ ] Déploiement sur serveur de production
- [ ] Application mobile
- [ ] Chatbot d'assistance
- [ ] Plateforme de formation en ligne

---

**Développé avec ❤️ par Matthieu Moreau-Le Breton**

*Dernière mise à jour : Septembre 2025*
