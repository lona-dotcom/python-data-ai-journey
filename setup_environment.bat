@echo off
echo ========================================
echo Configuration de l'environnement Python
echo ========================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe!
    echo Veuillez installer Python depuis https://python.org
    pause
    exit /b 1
)

REM Créer l'environnement virtuel
if not exist "venv" (
    echo Creation de l'environnement virtuel...
    python -m venv venv
    echo Environnement virtuel cree avec succes!
) else (
    echo Environnement virtuel existe deja.
)

REM Activer l'environnement virtuel
echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Mettre à jour pip
echo Mise a jour de pip...
python -m pip install --upgrade pip

REM Installer les dépendances
if exist "requirements.txt" (
    echo Installation des dependances depuis requirements.txt...
    pip install -r requirements.txt
) else (
    echo ATTENTION: requirements.txt non trouve!
    echo Installation des dependances de base...
    pip install numpy pandas matplotlib seaborn scikit-learn jupyter ipython
)

REM Créer les dossiers nécessaires
echo Creation de la structure de dossiers...
mkdir data\raw 2>nul
mkdir data\processed 2>nul
mkdir data\interim 2>nul
mkdir data\external 2>nul
mkdir data\samples 2>nul
mkdir logs 2>nul
mkdir reports 2>nul
mkdir images 2>nul
mkdir temp 2>nul
mkdir notebooks\exploration 2>nul
mkdir notebooks\modelisation 2>nul
mkdir notebooks\presentations 2>nul
mkdir notebooks\templates 2>nul
mkdir scripts 2>nul
mkdir utils 2>nul

REM Créer un fichier .env (si pas existant)
if not exist ".env" (
    echo # Variables d'environnement > .env
    echo # Ajoutez vos variables ici >> .env
    echo Fichier .env cree.
)

echo.
echo ========================================
echo Configuration terminee avec succes!
echo ========================================
echo.
echo Pour activer l'environnement manuellement:
echo   call venv\Scripts\activate
echo.
echo Pour desactiver:
echo   deactivate
echo.
pause