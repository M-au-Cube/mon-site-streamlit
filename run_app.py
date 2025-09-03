#!/usr/bin/env python3
"""
Script de lancement simple pour l'application Streamlit
"""

import subprocess
import sys
import os

def main():
    # Chemin vers Python
    python_path = r"C:\Users\mattm\AppData\Local\Programs\Python\Python312\python.exe"
    
    # Vérifier que Python existe
    if not os.path.exists(python_path):
        print(f"Erreur: Python introuvable à {python_path}")
        sys.exit(1)
    
    # Commande pour lancer Streamlit
    cmd = [python_path, "-m", "streamlit", "run", "app_matthieu.py", "--server.port", "8501"]
    
    print("Lancement de l'application Streamlit...")
    print(f"Commande: {' '.join(cmd)}")
    print("L'application sera accessible à l'adresse: http://localhost:8501")
    print("Appuyez sur Ctrl+C pour arrêter l'application")
    
    try:
        # Lancer l'application
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nApplication arrêtée par l'utilisateur")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du lancement: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
