import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
   # valutes.pop(0)
    return valutes


app = Flask(__name__)


def create_html(valutes):
    tablefmt = "grid"
    text = '<h1>Курс валют</h1>'
    text += '<h2> Код | Множитель |  Название | Продажа | Покупка</h2>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        del valute['ID']
        del valute['CharCode']
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
