from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    f1Logo = url_for('static', filename='f1Logo2.jpg')
    return render_template('home.html', f1Logo=f1Logo)

@app.route('/temporada2021')
def temporada2021():
    return render_template('temporada2021.html')

@app.route('/temporada2022')
def temporada2022():
    return render_template('temporada2022.html')

@app.route('/apoia-se')
def apoia_se():
    return render_template('apoia_se.html')

