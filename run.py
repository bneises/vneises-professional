import datetime
import yaml
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tori():
    with open('data.json', 'r') as data:
        context = yaml.safe_load(data)
    return render_template('index.html.j2', cr_years=get_cr_years(), context=context)

def get_cr_years(start=2020):
    current_year = datetime.datetime.now().year
    if current_year > start:
        return f'{start}-{current_year}'

    return f'{start}'

if __name__ == '__main__':
    app.run(threaded=True)
