import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tori():
    context = {
        'intro': {
            'profile_path': 'static/images/ToriProfile.jpg',
            'title': 'Victoria M. Neises, Ph.D.',
            'subtitle': 'Animal Physiologist',
            'statement': "Much of my research focuses on how the physiology of an organism shapes its behavior in reponse to environmental change. My research encompasses nutritional and metabolic physiology, quantitative ecology, and foraging behavior."
        }
    }
    return render_template('index.html.j2', cr_years=get_cr_years(), context=context)

def get_cr_years(start=2020):
    current_year = datetime.datetime.now().year
    if current_year > start:
        return f'{start}-{current_year}'

    return f'{start}'

if __name__ == '__main__':
    app.run(threaded=True)
