# webtechnologie
Dit is een repo voor de webtechnologie project in periode 3.

Hoe zet je een dev applicatie op?

### maak een venv aan in de root folder

python3 -m venv venv

### activeer de venv, installeer de requirements en run de applicatie.

mac/linux: . venv/bin/activate
windows: .\venv\Scripts\activate

pip install -r requirements.txt

windows:
SET FLASK_APP=filmfan.py
SET FLASK_ENV=development

linux/mac:
export FLASK_APP=filmfan.py
export FLASK_ENV=development

flask run