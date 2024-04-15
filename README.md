# DLIMS

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python
- virtualenv (optional, but recommended)
- Git (optional, but recommended)

## Django Installation (Optional)
```bash
python -m pip install Django
```

## Virtual Environment
Windows:
```bash
python -m pip install virtualenv
```

Ubuntu:
```bash
apt install python3-virtualenv
```

## Project Setup
```bash
git clone <repository-url>
cd project-folder
virtualenv .venv

# Activate virtual environment

# Windows
./.venv/Scripts/activate # Command Prompt
./.venv/Scripts/activate.ps1 # PowerShell
source ./.venv/Scripts/activate.ps1 # GitBash

# Ubuntu
source .venv/bin/activate

# Install the requirements.txt
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

## Run Project
Windows:
```bash
python manage.py runserver
```

Ubuntu:
```bash
python3 manage.py runserver
```

**Admin**
- URL: localhost:8000/admin
- Username: root
- Password: root
