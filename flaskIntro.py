from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return "<h1>Kontakta oss!!!</h1>"

@app.route('/about')
def about():
    return "<h1> This is me :D</h1>"

if __name__ == '__main__':
    app.run(debug=True)