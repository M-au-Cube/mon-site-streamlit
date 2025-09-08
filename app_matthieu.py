import streamlit as st
import os
from datetime import datetime
import json
import numpy as np
import random
import matplotlib.pyplot as plt

# Dictionnaires de traduction
TRANSLATIONS = {
    "fr": {
        "portfolio": "Portfolio",
        "profile": "👤 Profil",
        "expertise": "🎯 Expertises & Services",
        "convergence": "🌱 Projet Convergence",
        "articles": "📝 Articles",
        "tools": "🛠️ Outils",
        "navigation": "Navigation",
        "professional_profile": "👤 Profil professionnel - Matthieu Moreau-Le Breton",
        "profile_photo": "📸 Photo de profil\n\nAjoutez votre photo dans le fichier 'profil.jpg' ou 'profil.JPG'",
        "error_loading_image": "Erreur lors du chargement de l'image :",
        "risk_consultant": "🎯 Consultant en Risques & Entrepreneur",
        "risk_consultant_help": "Expertise en actuariat, finance et ESG",
        "professional_profile_title": "📋 Profil professionnel",
        "professional_profile_desc": "Consultant indépendant spécialisé dans l'analyse des risques financiers et la durabilité ESG. Je combine expertise technique actuarielle et vision stratégique pour créer des solutions innovantes répondant aux enjeux contemporains de la finance responsable.",
        "academic_background": "🎓 Formation académique",
        "actuarial_training": "• Formation en actuariat (membre de l'[Institut des Actuaires](https://www.institutdesactuaires.com/))",
        "data_science": "• Spécialisation en Data Science (diplômé de l'[Université Paris-Saclay](https://www.universite-paris-saclay.fr/))",
        "entrepreneurial_exp": "• Expérience entrepreneuriale et projets innovants : [Convergence](#convergence)",
        "technical_skills": "🌟 Compétences techniques",
        "professional_contact": "📞 Contact professionnel",
        "download_cv": "📄 CV : [Télécharger mon CV](CV_generalist_matthieu_moreau-le_breton.pdf)",
        "networks": "🔗 Réseaux",
        "my_linkedin": "💼 Mon profil LinkedIn",
        "instagram_account": "📊 Compte instagram Statistiques_fr",
        "youtube_channel": "🎥 Chaîne Youtube de Convergence",
        "projects_achievements": "🚀 Projets et réalisations",
        "convergence_project": "🌱 Projet Convergence",
        "convergence_desc": "Plateforme d'analyse ESG automatisée pour entreprises",
        "cac40_esg": "📊 Transparence CAC 40 ESG",
        "cac40_desc": "Analyse des rapports de durabilité avec Python et NLP",
        "financial_modeling": "📈 Modélisation financière",
        "financial_desc": "Développement de modèles financiers avancés",
        "educational_content": "📚 Contenu éducatif",
        "educational_desc": "Création de contenu sur les statistiques et l'analyse de données",
        "my_expertise": "🎯 Mes Expertises & Services",
        "areas_expertise": "📚 Domaines d'Expertise",
        "actuarial_science": "🏦 Actuariat",
        "actuarial_desc": "ALM, épargne-Retraite, Solvabilité II, IFRS 17",
        "finance_risk": "📊 Finance & Risques de marché",
        "finance_desc": "Modélisation financière, Risque de liquidité, Risque de crédit, Bâle III/IV",
        "esg_analysis": "🌱 ESG & Analyse de durabilité",
        "esg_desc": "Évaluation des critères ESG, CSRD, GRI, taxonomie verte, SFDR, reporting durable",
        "data_science_python": "🐍 Data Science & Python",
        "data_desc": "Analyse de données, machine learning, automatisation",
        "services_offered": "💼 Services proposés",
        "rate": "Tarif consulting : 550€ / jour",
        "python_training": "🐍 Formation Python",
        "python_desc": "Cours personnalisés en programmation Python pour tous niveaux",
        "math_support": "📐 Soutien mathématiques",
        "math_desc": "Accompagnement lycée et supérieur, préparation aux examens",
        "scientific_orientation": "🎓 Orientation scientifique",
        "orientation_desc": "Conseil Parcoursup et orientation post-bac",
        "esg_analysis_service": "📊 Analyse ESG",
        "esg_service_desc": "Évaluation et reporting de durabilité pour entreprises",
        "professional_contact_service": "📞 Contact professionnel",
        "freelance_available": "Disponible pour missions freelance et conseil",
        "my_profile": "Mon profil",
        "convergence_project_title": "🌱 Projet Convergence",
        "convergence_subtitle": "Plateforme d'analyse ESG automatisée pour entreprises",
        "convergence_desc_full": """
🌍 Convergence – Donner du sens aux données ESG

Convergence est un projet d’innovation en finance durable, né à Vannes, dont la mission est de rendre l’information ESG (Environnement, Social, Gouvernance) plus accessible, transparente et fiable.

Le projet repose sur trois piliers complémentaires :

• **Coherence** : collecte et structuration automatisée des données ESG publiées par les entreprises.

• **Resilience** : questionnaires destinés aux entreprises et à leurs collaborateurs pour évaluer leur performance ESG, analyse des risques extra-financiers et proposition de solutions via IA générative. Aide à la rédaction automatisée des rapports de durabilité.

• **Evidence** : application à destination des particuliers et des professionnels (Evidence Blue) pour évaluer la durabilité des produits et attribuer une note de durabilité ESG à chaque produit.

Nous commençons par Coherence, en développant des solutions de webscraping et d’extraction intelligente pour transformer les rapports de durabilité et sources publiques en bases de données ESG exploitables.
""",
        "convergence_objectives": "🎯 Objectifs de Convergence :",
        "convergence_obj1": "• Automatiser l'analyse des rapports ESG",
        "convergence_obj2": "• Fournir des scores de durabilité fiables",
        "convergence_obj3": "• Identifier les axes d'amélioration prioritaires",
        "convergence_obj4": "• Faciliter la conformité réglementaire",
        "main_features": "🚀 Fonctionnalités principales :",
        "feature1": "• Analyse automatique de documents ESG",
        "feature2": "• Scoring et benchmarking sectoriel",
        "feature3": "• Tableaux de bord interactifs",
        "feature4": "• Recommandations personnalisées",
        "technologies_used": "📊 Technologies utilisées",
        "ai": "IA",
        "youtube_channel_title": "🎥 Chaîne YouTube",
        "youtube_desc": "Découvrez Convergence en vidéo :",
        "watch_videos": "🎥 Voir les vidéos",
        "youtube_note": "La chaîne YouTube Convergence est en développement – bientôt disponible",
        "impact_results": "📈 Impact et résultats",
        "companies_analyzed": "📊 Entreprises analysées",
        "analysis_accuracy": "📈 Précision d'analyse",
        "time_saved": "⏱️ Temps économisé",
        "add_new_article": "➕ Ajouter un nouvel article",
        "article_title": "📝 Titre de l'article",
        "article_title_placeholder": "Entrez le titre de votre article",
        "description": "📄 Description",
        "description_placeholder": "Court paragraphe de présentation",
        "descriptive_image": "🖼️ Image descriptive",
        "insert_pdf": "📎 Insérer un PDF",
        "publish_article": "🚀 Publier l'article",
        "article_published": "✅ Article publié avec succès !",
        "published_articles": "📚 Articles publiés",
        "view": "👁️ Voir",
        "edit": "✏️ Modifier",
        "delete": "🗑️ Supprimer",
        "displaying_article": "Affichage de l'article :",
        "edit_functionality": "Fonctionnalité de modification à implémenter",
        "article_deleted": "Article supprimé !",
        "no_articles": "📝 Aucun article publié pour le moment. Ajoutez votre premier article !",
        "tools_resources": "🛠️ Outils & Ressources",
        "financial_calculators": "🧮 Calculatrices financières",
        "financial_calc_desc": "Outils de calcul pour l'analyse financière et actuarielle.",
        "profitability_calc": "💰 Calculateur de rentabilité",
        "risk_analysis": "📊 Analyse de risques",
        "feature_dev": "Fonctionnalité en développement",
        "interactive_dashboards": "📈 Dashboards interactifs",
        "dashboard_desc": "Visualisations de données et analyses en temps réel.",
        "esg_dashboard": "📊 Dashboard ESG",
        "financial_indicators": "📈 Indicateurs financiers",
        "python_scripts": "🐍 Scripts Python",
        "scripts_desc": "Ressources et scripts utiles pour vos projets.",
        "data_analysis": "📊 Analyse de données",
        "machine_learning": "🤖 Machine Learning",
        "educational_resources": "📚 Ressources éducatives",
        "educational_desc_tools": "Matériel de cours et ressources d'apprentissage.",
        "python_course": "📖 Cours Python",
        "math_exercises": "📐 Exercices maths",
        "under_development": "🚀 En développement",
        "tools_available_soon": "Ces outils seront bientôt disponibles :",
        "esg_api": "• 🔄 API d'analyse ESG",
        "mobile_app": "• 📱 Application mobile",
        "assistance_chatbot": "• 🤖 Chatbot d'assistance",
        "online_platform": "• 📊 Plateforme de formation en ligne",
        "error_save": "Erreur lors de la sauvegarde :",
        "error_loading": "Erreur lors du chargement :",
        "professional_portfolio": "© 2025 Matthieu Moreau-Le Breton - Portfolio professionnel",
        "developed_with": "Développé avec ❤️ et Streamlit"
    }
}


def save_articles():
    try:
        with open('articles.json', 'w', encoding='utf-8') as f:
            json.dump(st.session_state.articles, f, ensure_ascii=False, indent=2)
    except Exception as e:
        current_lang = st.session_state.get('language', 'fr')
        st.error(f"{TRANSLATIONS[current_lang]['error_save']} {e}")


def load_articles():
    try:
        if os.path.exists('articles.json'):
            with open('articles.json', 'r', encoding='utf-8') as f:
                st.session_state.articles = json.load(f)
    except Exception as e:
        current_lang = st.session_state.get('language', 'fr')
        st.error(f"{TRANSLATIONS[current_lang]['error_loading']} {e}")


def main() -> None:
    # Configuration de la page
    st.set_page_config(
        page_title="Matthieu Moreau-Le Breton - Portfolio",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Couleurs et style
    primary_color = "#001F3F"
    secondary_color = "#0074D9"

    # CSS personnalisé simplifié
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        .main {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            font-family: 'Inter', sans-serif;
        }}
        .stApp {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }}
        h1, h2, h3, h4 {{
            color: {primary_color};
            font-weight: 600;
            margin-bottom: 1rem;
        }}
        h1 {{
            font-size: 2.5rem;
            background: linear-gradient(45deg, {primary_color}, {secondary_color});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .stButton > button {{
            background: linear-gradient(45deg, {primary_color}, {secondary_color});
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 1.5rem;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 31, 63, 0.2);
        }}
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 31, 63, 0.3);
        }}
        .tag {{
            background: #e3f2fd;
            color: #1976d2;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            text-align: center;
            font-size: 0.9rem;
            display: inline-block;
            margin: 0.2rem;
        }}
        .tag-green {{ background: #e8f5e8; color: #2e7d32; }}
        .tag-orange {{ background: #fff3e0; color: #f57c00; }}
        .tag-pink {{ background: #fce4ec; color: #c2185b; }}
        .social-link {{
            display: inline-block;
            margin: 0.5rem;
            font-size: 1.5rem;
            text-decoration: none;
            transition: transform 0.3s ease;
        }}
        .social-link:hover {{
            transform: scale(1.2);
        }}
    </style>
    """, unsafe_allow_html=True)

    # Initialisation de la session state
    if 'articles' not in st.session_state:
        st.session_state.articles = []
    # plus de sélection de langue, français par défaut

    # Chargement des articles au démarrage
    load_articles()

    # Langue fixée en français
    current_lang = 'fr'
    
    # Menu latéral
    st.sidebar.title(TRANSLATIONS[current_lang]["portfolio"])
    menu = [
        TRANSLATIONS[current_lang]["profile"],
        TRANSLATIONS[current_lang]["expertise"],
        TRANSLATIONS[current_lang]["convergence"],
        TRANSLATIONS[current_lang]["articles"],
        TRANSLATIONS[current_lang]["tools"]
    ]
    choice = st.sidebar.selectbox(TRANSLATIONS[current_lang]["navigation"], menu)

    # --- PAGE 1 : Profil ---
    if choice == TRANSLATIONS[current_lang]["profile"]:
        # Utilisation de toute la largeur de la page
        st.title(TRANSLATIONS[current_lang]["professional_profile"])
        st.markdown("---")
        
        # Première ligne : Photo et titre principal
        col1, col2 = st.columns([1, 2])
        
        with col1:
            try:
                if os.path.exists("profil.jpg") or os.path.exists("profil.JPG"):
                    image_path = "profil.jpg" if os.path.exists("profil.jpg") else "profil.JPG"
                    st.image(image_path, width=300, use_container_width=True)
                else:
                    st.info(TRANSLATIONS[current_lang]["profile_photo"])
            except Exception as e:
                st.error(f"{TRANSLATIONS[current_lang]['error_loading_image']} {e}")
        
        with col2:
            st.header(TRANSLATIONS[current_lang]["risk_consultant"], help=TRANSLATIONS[current_lang]["risk_consultant_help"])
            st.markdown(f"**{TRANSLATIONS[current_lang]['professional_profile_title']}**")
            st.write(TRANSLATIONS[current_lang]["professional_profile_desc"])
            
            st.subheader(TRANSLATIONS[current_lang]["academic_background"])
            st.markdown(TRANSLATIONS[current_lang]["actuarial_training"])
            st.markdown(TRANSLATIONS[current_lang]["data_science"])
            st.write(TRANSLATIONS[current_lang]["entrepreneurial_exp"])
                
            st.subheader(TRANSLATIONS[current_lang]["technical_skills"])
            col_tags = st.columns(2)
            with col_tags[0]:
                st.markdown('<div class="tag">Python</div>', unsafe_allow_html=True)
                st.markdown('<div class="tag tag-green">Finance</div>', unsafe_allow_html=True)
            with col_tags[1]:
                st.markdown('<div class="tag tag-orange">ESG</div>', unsafe_allow_html=True)
                st.markdown('<div class="tag tag-pink">Actuarial Science</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Deuxième ligne : Formation et compétences
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(TRANSLATIONS[current_lang]["professional_contact"])
            st.markdown("**📧 Email :** [matt.mlb@icloud.com](mailto:matt.mlb@icloud.com)")
            st.markdown(f"**{TRANSLATIONS[current_lang]['download_cv']}**")
            
        with col2:
            st.subheader(TRANSLATIONS[current_lang]["networks"])
            
            # LinkedIn
            st.markdown("**💼 LinkedIn**")
            st.markdown(f"[{TRANSLATIONS[current_lang]['my_linkedin']}](https://www.linkedin.com/in/matthieu-moreau-le-breton-b0a248184/)")
            
            st.write("")  # Espacement
            
            # Instagram
            st.markdown("**📊 Instagram**")
            st.markdown(f"[{TRANSLATIONS[current_lang]['instagram_account']}](https://www.instagram.com/statistiques_fr?igsh=MTEzZTY1Mm9ycXRzeg%3D%3D&utm_source=qr)")
            
            st.write("")  # Espacement
            
            # YouTube
            st.markdown("**🎥 YouTube**")
            st.markdown(f"[{TRANSLATIONS[current_lang]['youtube_channel']}](https://www.youtube.com/@convergence)")
        


    # --- PAGE 2 : Expertises & Services ---
    elif choice == TRANSLATIONS[current_lang]["expertise"]:
        st.title(TRANSLATIONS[current_lang]["my_expertise"])
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(TRANSLATIONS[current_lang]["areas_expertise"])
            st.markdown(f"**{TRANSLATIONS[current_lang]['actuarial_science']}**")
            st.write(TRANSLATIONS[current_lang]["actuarial_desc"])
            st.markdown(f"**{TRANSLATIONS[current_lang]['finance_risk']}**")
            st.write(TRANSLATIONS[current_lang]["finance_desc"])
            st.markdown(f"**{TRANSLATIONS[current_lang]['esg_analysis']}**")
            st.write(TRANSLATIONS[current_lang]["esg_desc"])
            st.markdown(f"**{TRANSLATIONS[current_lang]['data_science_python']}**")
            st.write(TRANSLATIONS[current_lang]["data_desc"])

        with col2:
            st.subheader(TRANSLATIONS[current_lang]["services_offered"])
            st.success(f"**{TRANSLATIONS[current_lang]['rate']}**")
            st.divider()
            st.markdown(f"**{TRANSLATIONS[current_lang]['professional_contact_service']}**")
            st.markdown("**📧 Email :** [matt.mlb@icloud.com](mailto:matt.mlb@icloud.com)")
            st.markdown(f"**💼 LinkedIn :** [{TRANSLATIONS[current_lang]['my_profile']}](https://www.linkedin.com/in/matthieu-moreau-le-breton-b0a248184/)")
            st.markdown(f"**{TRANSLATIONS[current_lang]['download_cv']}**")

    # --- PAGE 3 : Convergence Project ---
    elif choice == TRANSLATIONS[current_lang]["convergence"]:
        st.title(TRANSLATIONS[current_lang]["convergence_project_title"])
        st.subheader(TRANSLATIONS[current_lang]["convergence_subtitle"])
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write(TRANSLATIONS[current_lang]["convergence_desc_full"])
            
            st.markdown(f"**{TRANSLATIONS[current_lang]['convergence_objectives']}**")
            st.write(f"""
            {TRANSLATIONS[current_lang]['convergence_obj1']}  
            {TRANSLATIONS[current_lang]['convergence_obj2']}  
            {TRANSLATIONS[current_lang]['convergence_obj3']}  
            {TRANSLATIONS[current_lang]['convergence_obj4']}
            """)
            
            st.markdown(f"**{TRANSLATIONS[current_lang]['main_features']}**")
            st.write(f"""
            {TRANSLATIONS[current_lang]['feature1']}  
            {TRANSLATIONS[current_lang]['feature2']}  
            {TRANSLATIONS[current_lang]['feature3']}  
            {TRANSLATIONS[current_lang]['feature4']}
            """)
        
        with col2:
            # Logo Convergence
            try:
                if os.path.exists("Logo_Convergence.png"):
                    st.image("Logo_Convergence.png", use_container_width=True)
            except Exception:
                pass
            st.markdown(f"**{TRANSLATIONS[current_lang]['technologies_used']}**")
            col_tech = st.columns(2)
            with col_tech[0]:
                st.markdown('<div class="tag tag-orange">ESG</div>', unsafe_allow_html=True)
                st.markdown('<div class="tag">Python</div>', unsafe_allow_html=True)
            with col_tech[1]:
                st.markdown(f'<div class="tag tag-orange">{TRANSLATIONS[current_lang]["ai"]}</div>', unsafe_allow_html=True)
                st.markdown('<div class="tag">NLP</div>', unsafe_allow_html=True)
            
            st.divider()
            st.markdown(f"**{TRANSLATIONS[current_lang]['youtube_channel_title']}**")
            st.write(TRANSLATIONS[current_lang]["youtube_desc"]) 
            st.info(TRANSLATIONS[current_lang]["youtube_note"]) 
            if st.button(TRANSLATIONS[current_lang]["watch_videos"], key="convergence_youtube"):
                st.write("")
        
        

    # --- PAGE 4 : Articles ---
    elif choice == TRANSLATIONS[current_lang]["articles"]:
        st.title("📝 Articles")
        
        # Article test sur Convergence
        st.subheader("🌱 Présentation du Projet Convergence")
        st.caption("📅 03/09/2025")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write("""
            **Convergence** est un projet innovant de plateforme d'analyse ESG automatisée pour entreprises. 
            Notre mission est de rendre l'information ESG (Environnement, Social, Gouvernance) plus accessible, 
            transparente et fiable grâce à l'intelligence artificielle et au traitement automatique des données.
            
            Le projet repose sur trois piliers complémentaires :
            • **Coherence** : collecte et structuration automatisée des données ESG
            • **Resilience** : évaluation de la performance ESG et analyse des risques
            • **Evidence** : notation de durabilité pour produits et services
            """)
            
            # Boutons d'action
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
            with col_btn1:
                if st.button("👁️ Voir l'article complet", key="view_convergence"):
                    st.info("Article complet : Présentation du Projet Convergence")
            with col_btn2:
                if st.button("📊 Dashboard ESG", key="dash_convergence"):
                    st.info("Dashboard ESG en cours de développement")
            with col_btn3:
                if st.button("🔗 En savoir plus", key="more_convergence"):
                    st.info("Plus d'informations sur Convergence")
        
        with col2:
            # Image Convergence
            try:
                if os.path.exists("Logo_Convergence.png"):
                    st.image("Logo_Convergence.png", use_container_width=True, caption="Logo Convergence")
                else:
                    st.info("Logo Convergence non trouvé")
            except Exception:
                st.info("Erreur lors du chargement du logo")
        
        st.markdown('<div class="tag tag-orange">ESG</div>', unsafe_allow_html=True)
        st.markdown('<div class="tag">Innovation</div>', unsafe_allow_html=True)
        st.markdown('<div class="tag tag-green">Durabilité</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Section pour articles futurs
        st.subheader("📚 Articles à venir")
        st.info("""
        🔄 **En cours de rédaction :**
        • Analyse des critères ESG dans le CAC 40
        • Guide pratique de la taxonomie verte européenne
        • Impact du reporting durable sur la valorisation des entreprises
        • Introduction aux méthodologies de scoring ESG
        """)

    # --- PAGE 5 : Tools ---
    elif choice == TRANSLATIONS[current_lang]["tools"]:
        st.title(TRANSLATIONS[current_lang]["tools_resources"])
        
        # Outil 1 : Générateur de scénarios économiques
        st.subheader("📊 Générateur de Scénarios Économiques")
        st.write("""
        **En cours de publication** - Outil avancé de simulation économique pour l'analyse de portefeuille 
        et la gestion des risques. Permet de tester différents scénarios macroéconomiques sur vos investissements.
        """)
        
        # Classes d'actifs simulées
        st.markdown("**🏗️ Classes d'actifs simulées :**")
        col_assets = st.columns(4)
        with col_assets[0]:
            st.markdown('<div class="tag tag-green">🏠 Immobilier</div>', unsafe_allow_html=True)
        with col_assets[1]:
            st.markdown('<div class="tag tag-orange">💼 Private Equity</div>', unsafe_allow_html=True)
        with col_assets[2]:
            st.markdown('<div class="tag tag-pink">📜 Obligations</div>', unsafe_allow_html=True)
        with col_assets[3]:
            st.markdown('<div class="tag tag-green">📈 Actions</div>', unsafe_allow_html=True)
        
        st.write("""
        **Fonctionnalités principales :**
        • Simulation de chocs économiques (inflation, taux d'intérêt, croissance)
        • Analyse de corrélation entre classes d'actifs
        • Optimisation de portefeuille sous contraintes
        • Reporting de stress-testing et VaR
        """)
        
        if st.button("🚀 Accéder au Générateur", key="access_scenarios"):
            st.info("🔄 Outil en cours de développement - Disponible prochainement")
        
        st.divider()
        
        # Outil 2 : Cours Python
        st.subheader("🐍 Cours Python - Fondamentaux & Machine Learning")
        st.write("""
        **En cours de publication** - Formation complète en programmation Python, des bases aux applications 
        avancées en data science et machine learning.
        """)
        
        # Modules du cours
        st.markdown("**📚 Modules du cours :**")
        col_modules = st.columns(3)
        
        with col_modules[0]:
            st.markdown("**🔰 Les Bases**")
            st.write("""
            • Syntaxe Python
            • Structures de données
            • Fonctions et classes
            • Gestion des erreurs
            """)
        
        with col_modules[1]:
            st.markdown("**📦 Packages Essentiels**")
            st.write("""
            • NumPy (calculs numériques)
            • Pandas (manipulation de données)
            • Matplotlib/Seaborn (visualisation)
            • Requests (API et web)
            """)
        
        with col_modules[2]:
            st.markdown("**🤖 Introduction ML**")
            st.write("""
            • Scikit-learn
            • Préprocessing des données
            • Modèles de régression
            • Évaluation des performances
            """)
        
        if st.button("🎓 Commencer le Cours", key="start_python_course"):
            st.info("🔄 Cours en cours de préparation - Disponible prochainement")
        
        st.divider()
        
        st.info("💡 **Besoin d'un outil spécifique ?** Contactez-moi pour discuter de vos besoins et voir comment je peux vous aider à développer des solutions sur mesure.")

    # Footer
    st.divider()
    _, col_footer2, _ = st.columns([1, 2, 1])
    with col_footer2:
        st.markdown(f"**{TRANSLATIONS[current_lang]['professional_portfolio']}**")
        st.caption(TRANSLATIONS[current_lang]["developed_with"])


if __name__ == "__main__":
    main()
