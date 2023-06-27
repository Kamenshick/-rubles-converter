

import requests
from flask import Flask,render_template, request

class Validation:
    def is_validate(self,string):
        if string.isdigit():
            return int(string)
        else:
            return 0

validate = Validation()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data_valute = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    all_valute = list(data_valute['Valute'].keys())
    if request.method == 'POST':
        count = request.form.get('one-fc')
        form= request.form.get('currency-one')
        try:
            if not validate.is_validate(count):
                raise ValueError('Введённое значение не число')
        except ValueError:
            answer = f"The entered value is not a number"
        else:
            data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            answer = f"{data['Valute'][form]['Value'] * float(count)} rub"
    else:
        answer = ''
    return render_template("index.html", cash=answer, valute=all_valute)

if __name__ == '__main__':
    app.run(debug=True)