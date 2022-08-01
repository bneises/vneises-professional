import datetime
import yaml
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tori():
    context = {}
    try:
        with open('data.yaml', 'r') as data:
            context = yaml.safe_load(data)
        output = render_template('index.html.j2', cr_years=get_cr_years(), context=context)
    except Exception as e:
        output = render_template(e)
    return output

def get_cr_years(start=2020):
    current_year = datetime.datetime.now().year
    if current_year > start:
        return f'{start}-{current_year}'

    return f'{start}'

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
