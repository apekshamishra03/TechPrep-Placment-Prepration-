@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Installing dependencies if needed...
pip install flask flask_sqlalchemy werkzeug pyinstaller
echo Creating executable...
pyinstaller --onefile --windowed --add-data "templates;templates" --add-data "static;static" --add-data "backend;backend" --hidden-import=flask_sqlalchemy --name techprep app.py
echo Build complete! Check dist/techprep.exe
pause

