#!/bin/bash

# Définir des couleurs
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
CYAN='\e[36m'
RESET='\e[0m'

echo -e "🛠️ Creating a virtualenv... 🛠️"
python3 -m venv django_venv

if [ -d "django_venv" ]; then
    echo -e "✅ ${GREEN}Django_venv is created !${RESET}"
else
    echo -e "❌ ${RED}Failed to create django_venv${RESET}"
    exit 1
fi

echo "================================================================"
echo "Activate virtualenv..."
source django_venv/bin/activate

if [ "$VIRTUAL_ENV" != "" ]; then
    echo -e "✅ ${GREEN}Django_venv is activated!${RESET}"
else
    echo -e "❌ ${RED}Failed to activate django_venv${RESET}"
    exit 1
fi

echo "================================================================"
echo "🔄 Verifying if pip is updated... 🔄"

current_pip_version=$(pip --version | awk '{print $2}')
updated_pip_version=$(pip install --upgrade pip | grep "Requirement already satisfied: pip in" | awk '{print $7}' | tr -d '()')

if [ $current_pip_version = $updated_pip_version ]; then
    echo -e "✅ ${GREEN}Pip is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}Pip is outdated! Updating...${RESET}"
    pip install --upgrade pip
    echo -e "🚀 ${YELLOW}Pip updated to $updated_pip_version!${RESET}"
fi

echo "================================================================"
echo "🚀 Installing Django..."
pip install django

if pip show django > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}Django is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install Django${RESET}"
    exit 1
fi

# Get the installed version of Django
installed_version=$(pip show django | grep Version | awk '{print $2}')
# Get the latest version of Django from PyPI
latest_version=$(pip install django --upgrade | grep "Requirement already satisfied: django in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}Django is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}Django is outdated! Updating...${RESET}"
    pip install --upgrade django
    echo -e "🚀 ${YELLOW}Django updated to $latest_version!${RESET}"
fi

echo "================================================================"
echo "🚀 Installing psycopg2..."
pip install psycopg2-binary

test=$(pip show psycopg2-binary > /dev/null 2>&1)
echo $test

if pip show psycopg2-binary > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}psycopg2 is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install psycopg2${RESET}"
    exit 1
fi

# Get the installed version of psycopg2
installed_version=$(pip show psycopg2-binary | grep Version | awk '{print $2}')
# Get the latest version of psycopg2 from PyPI
latest_version=$(pip install psycopg2-binary --upgrade | grep "Requirement already satisfied: psycopg2-binary in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}psycopg2 is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}psycopg2 is outdated! Updating...${RESET}"
    pip install --upgrade psycopg2
    echo -e "🚀 ${YELLOW}psycopg2 updated to $latest_version!${RESET}"
fi

echo "================================================================"
echo "🚀 Installing markdown..."
pip install markdown

test=$(pip show markdown > /dev/null 2>&1)
echo $test

if pip show markdown > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}markdown is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install markdown${RESET}"
    exit 1
fi

# Get the installed version of Markdown
installed_version=$(pip show markdown | grep Version | awk '{print $2}')
# Get the latest version of Markdown from PyPI
latest_version=$(pip install markdown --upgrade | grep "Requirement already satisfied: markdown in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}markdown is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}markdown is outdated! Updating...${RESET}"
    pip install --upgrade markdown
    echo -e "🚀 ${YELLOW}markdown updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing python-dotenv..."
pip install python-dotenv

test=$(pip show python-dotenv > /dev/null 2>&1)
echo $test

if pip show python-dotenv > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}python-dotenv is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install python-dotenv${RESET}"
    exit 1
fi

# Get the installed version of Dotenv
installed_version=$(pip show python-dotenv | grep Version | awk '{print $2}')
# Get the latest version of Dotenv from PyPI
latest_version=$(pip install python-dotenv --upgrade | grep "Requirement already satisfied: python-dotenv in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}python-dotenv is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}python-dotenv is outdated! Updating...${RESET}"
    pip install --upgrade python-dotenv
    echo -e "🚀 ${YELLOW}python-dotenv updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing django-bootstrap-v5..."
pip install django-bootstrap-v5

test=$(pip show django-bootstrap-v5 > /dev/null 2>&1)
echo $test

if pip show django-bootstrap-v5 > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}django-bootstrap-v5 is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install django-bootstrap-v5${RESET}"
    exit 1
fi
# Get the installed version of django-bootstrap-v5
installed_version=$(pip show django-bootstrap-v5 | grep Version | awk '{print $2}')
# Get the latest version of django-bootstrap-v5 from PyPI
latest_version=$(pip install django-bootstrap-v5 --upgrade | grep "Requirement already satisfied: django-bootstrap-v5 in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}django-bootstrap-v5 is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}django-bootstrap-v5 is outdated! Updating...${RESET}"
    pip install --upgrade django-bootstrap-v5
    echo -e "🚀 ${YELLOW}django-bootstrap-v5 updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing celery..."
pip install celery

test=$(pip show celery > /dev/null 2>&1)
echo $test

if pip show celery > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}celery is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install celery${RESET}"
    exit 1
fi
# Get the installed version of celery
installed_version=$(pip show celery | grep Version | awk '{print $2}')
# Get the latest version of celery from PyPI
latest_version=$(pip install celery --upgrade | grep "Requirement already satisfied: celery in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}celery is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}celery is outdated! Updating...${RESET}"
    pip install --upgrade celery
    echo -e "🚀 ${YELLOW}celery updated to $latest_version!${RESET}"
fi

echo "================================================================"
echo "🚀 Installing Pillow..."
pip install Pillow

test=$(pip show Pillow > /dev/null 2>&1)
echo $test

if pip show Pillow > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}Pillow is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install Pillow${RESET}"
    exit 1
fi
# Get the installed version of Pillow
installed_version=$(pip show Pillow | grep Version | awk '{print $2}')
# Get the latest version of Pillow from PyPI
latest_version=$(pip install Pillow --upgrade | grep "Requirement already satisfied: Pillow in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}Pillow is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}Pillow is outdated! Updating...${RESET}"
    pip install --upgrade Pillow
    echo -e "🚀 ${YELLOW}Pillow updated to $latest_version!${RESET}"
fi

echo "================================================================"
echo "📝 Creating a requirements.txt..."
pip freeze > requirements.txt
echo -e "✅ ${GREEN}requirements.txt is created!${RESET}"
echo "================================================================"

echo "🎉 All tasks completed successfully! 🎉"