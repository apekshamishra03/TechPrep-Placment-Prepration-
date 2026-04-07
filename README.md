# TechPrep

TechPrep is a comprehensive interview preparation platform with sections for Aptitude, Technical, and Interview preparation. Features user authentication, SQLite database, and PyInstaller build for standalone executable.

## Features
- User signup/login
- Aptitude tests
- Technical questions
- Interview preparation resources
- Responsive HTML templates
- Java backend server (optional)

## Quick Start (Development)
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run Flask app:
   ```
   python app.py
   ```
3. Open http://127.0.0.1:5000/

## Build Standalone Executable
Run `build.bat` (Windows):
```
build.bat
```
Output: `dist/techprep.exe`

## Java Backend (Optional)
```
cd backend
javac Server.java
java Server
```
Listens on port 8000.

## Database
SQLite `instance/database.db` - stores users.

## Deployment
Flask app - deploy to Heroku/Vercel/PythonAnywhere or use Docker.

## License
MIT
