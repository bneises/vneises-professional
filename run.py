import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tori():
   return render_template('index.html', cr_years=get_cr_years())

def get_cr_years(start=2020):
   current_year = datetime.datetime.now().year
   if current_year > start:
      return f'{start}-{current_year}'

   return f'{start}'

if __name__ == '__main__':
    app.run(threaded=True)
    