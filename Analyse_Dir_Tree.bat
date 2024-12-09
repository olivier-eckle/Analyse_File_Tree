@echo off
REM Script batch pour exécuter Analyse_File_Tree.py

REM Spécifiez le chemin de Python si nécessaire (par exemple, si Python n'est pas dans le PATH).
SET PYTHON_EXECUTABLE=python
REM Spécifiez le chemin relatif ou complet de votre script Python.
SET SCRIPT_PATH=.\Analyse_File_Tree.py
echo %PYTHON_EXECUTABLE% %SCRIPT_PATH%

REM Lance le script Python
%PYTHON_EXECUTABLE% %SCRIPT_PATH%

REM Pause pour afficher les éventuels messages avant de fermer
PAUSE
