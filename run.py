from eve import Eve
from flask import render_template, Flask, send_from_directory
import os

static_folder = 'static/dist/static'
template_folder = 'static/dist'

app = Eve(__name__, static_folder=static_folder,
          template_folder=template_folder)


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
