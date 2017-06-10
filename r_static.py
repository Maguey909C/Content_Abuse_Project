from flask import Flask
from flask import render_template
import datetime

date = datetime.date.today().strftime("%m-%d-%y")

app = Flask(__name__)

@app.route('/')
def execute():
    return render_template('r_webpage.html', timestamp=date)

if __name__ == '__main__':

    app.run("0.0.0.0", port=80)
