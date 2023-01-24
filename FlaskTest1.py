from flask import Flask
Nutzerzahl = 0
nutzer = '0'
app = Flask(__name__)

@app.route('/')
def index():
    global Nutzerzahl
    global nutzer 
    Nutzerzahl = Nutzerzahl + 1
    nutzer = str(Nutzerzahl)
    return nutzer

app.run(host='0.0.0.0', port=5001)
