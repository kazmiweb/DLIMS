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
```bash
python -m pip install virtualenv
```

## Project Setup
```bash
git clone <repository-url>
cd project-folder
virtualenv .venv
# Activate virtual environment
source .venv/bin/activate

pip install -r requirements
```

## Run Project
```bash
python manage.py runserver
```

**Admin**
- URL: localhost:8000/admin
- Username: root
- Password: root

**URLS**
- http://localhost:8000/license/verify
- http://localhost:8000/license/verify/save
