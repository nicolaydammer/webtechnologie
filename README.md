# webtechnologie
Dit is een repo voor de webtechnologie project in periode 3.

Hoe zet je een dev applicatie op?

### maak een venv aan in de root folder

python3 -m venv venv

### activeer de venv, installeer de requirements en run de applicatie.

. venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=filmfan.py

export FLASK_ENV=development

flask run