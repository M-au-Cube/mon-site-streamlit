@echo off
echo ========================================
echo Lancement de app_matthieu.py
echo ========================================
echo.

echo L'application sera accessible a l'adresse: http://localhost:8501
echo.
echo Appuyez sur Ctrl+C pour arreter l'application
echo.

cd /d "%~dp0"
"C:\Users\mattm\AppData\Local\Programs\Python\Python312\python.exe" -m streamlit run app_matthieu.py --server.port 8501 --server.address localhost

pause
