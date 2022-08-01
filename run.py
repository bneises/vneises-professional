import datetime
import yaml
from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication


app = Flask(__name__)
# app.debug = True
# app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

@app.route('/')
def tori():
    with open('templates/data.yaml', 'r') as data:
        context = yaml.safe_load(data)
    return render_template('index.html.j2', cr_years=get_cr_years(), context=context)

def get_cr_years(start=2020):
    current_year = datetime.datetime.now().year
    if current_year > start:
        return f'{start}-{current_year}'

    return f'{start}'

if __name__ == '__main__':
    app.run(threaded=True)
